# This Python file uses the following encoding: utf-8
import sys
import os
import cv2
import numpy as np
import pandas as pd
import math
from PIL import Image

from skimage.transform import resize
from skimage.morphology import binary_erosion, binary_dilation
from skimage.measure import label, regionprops
from skimage.transform import resize
from skimage.morphology import binary_erosion, binary_dilation
from skimage.measure import label, regionprops

import matplotlib.patches as patches
import pydicom

from tensorflow.keras.models import load_model

from pydicom.pixel_data_handlers.util import convert_color_space
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog,  QGraphicsScene, QGraphicsEllipseItem
from PySide6.QtGui import QRegularExpressionValidator ,QIcon, QPixmap, QImage, QPen, QColor
from PySide6.QtCore import QRectF, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

def set_dark_theme():
    app.setStyleSheet("""
        QWidget {
            background-color: #333;
            color: white;
        }
        QPushButton {
            background-color: #2FA572;
            color: white;
            border: 1px solid #777;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #106A43;
        }
    """)

class MainWindow(QMainWindow):

    def create_DB(self):
        if not os.path.exists('training_set_pixel_size_and_HC.csv') or not os.path.exists('test_set_pixel_size.csv'):
                self.pixelSizesDB = pd.DataFrame()
                return
        df1 = pd.read_csv('training_set_pixel_size_and_HC.csv')
        df1.drop(columns=['head circumference (mm)'], inplace=True)
        df2 = pd.read_csv('test_set_pixel_size.csv')
        self.pixelSizesDB = pd.concat([df1, df2], ignore_index=True)


    def showImage(self, numpyImage, ellipse_params=None):
        """
        Displays the image in the graphics view and optionally draws an ellipse.

        :param numpyImage: Grayscale image as a NumPy array
        :param ellipse_params: Tuple containing ellipse parameters:
                               ((center_x, center_y), (width, height), angle)
        """
        # Convert the NumPy image to QImage
        height, width = numpyImage.shape
        bytes_per_line = width
        qimage = QImage(numpyImage.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

        # Convert QImage to QPixmap and display in the QGraphicsView
        pixmap = QPixmap.fromImage(qimage)
        scene = self.ui.graphicsView.scene()
        if scene is None:
            scene = QGraphicsScene()
            self.ui.graphicsView.setScene(scene)

        scene.clear()  # Clear any existing items in the scene
        pixmap_item = scene.addPixmap(pixmap)

        # Draw the ellipse if parameters are provided
        if ellipse_params is not None:
            center = ellipse_params[0]  # (center_x, center_y)
            size = ellipse_params[1]    # (width, height)
            angle = ellipse_params[2]   # Rotation angle

            # Calculate the rectangle bounding the ellipse
            rect = QRectF(
                center[0] - size[0] / 2,  # Top-left x
                center[1] - size[1] / 2,  # Top-left y
                size[0],                 # Width
                size[1]                  # Height
            )

            # Create and configure the QGraphicsEllipseItem
            ellipse_item = QGraphicsEllipseItem(rect)
            ellipse_item.setPen(QPen(QColor('#2ecc71'), 1.5, Qt.SolidLine))
            ellipse_item.setTransformOriginPoint(rect.center())
            ellipse_item.setRotation(angle)

            # Add the ellipse to the scene
            scene.addItem(ellipse_item)


    def select_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Use Qt dialog instead of native dialog
        # Set file filters to allow only PNG and DCM files
        filters = "PNG Files (*.png);;DCM Files (*.dcm)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Select image file (PNG or DCM)", "", filters, options=options)
        if file_path:
            if (os.path.basename(file_path)[-3:].lower() == "dcm"): #Dicom Files
                print("TO DO")
            else: #PNG
                self.fileName = os.path.basename(file_path)
                self.imageNumpy = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                self.showImage(self.imageNumpy)
                if self.modelFlag:
                    self.ui.predict_Button.setEnabled(True)
                    self.ui.save_Button.setEnabled(False)
                self.reset()

                filtered_df = self.pixelSizesDB[self.pixelSizesDB['filename'] == self.fileName]
                if not filtered_df.empty:
                    pixel_size = filtered_df.loc[:, 'pixel size(mm)'].iloc[0]
                    self.ui.pixelSizeText.setText(str(pixel_size))

    def load_the_network(self):
        try:
            self.model = load_model("network.h5", compile=False)
            self.modelFlag = True
        except:
            self.modelFlag = False
            print("NO MODEL IS LOADED!")

    def reset(self):
        self.ui.HCtextLabel.setText(f"HC: {0.00:.2f} mm")
        self.ui.GAtextLabel.setText(f"GA: {0}w {0}d")
        self.ui.OFDtextLabel.setText(f"OFD: {0.00:.2f} mm")
        self.ui.BPDtextLabel.setText(f"BPD: {0.00:.2f} mm")

    def make_prediction(self):
        self.reset()

        try:
            imageNumpyRes = np.array(resize(self.imageNumpy.squeeze(), (256,256), mode="reflect"))
            predictions = self.model.predict(np.expand_dims(imageNumpyRes, axis=0))
            # print(f"prediction_shape: {predictions.shape}")

            predicted_image_array = (predictions[0] * 255).astype(np.uint8).reshape(256, 256)

            original_height = np.shape(self.imageNumpy)[0]
            original_width = np.shape(self.imageNumpy)[1]

            resize_factor = (original_height / 256, original_width / 256)

            resized_predictions = np.array(resize(predicted_image_array.squeeze(), (original_height, original_width), mode='reflect'))

            threshold_value = 0.5
            binary_predictions = (resized_predictions > threshold_value).astype(np.uint8)

            def apply_morphological_operations(binary_mask):
                # Erosion followed by dilation
                eroded_mask = binary_erosion(binary_mask)
                refined_mask = binary_dilation(eroded_mask)
                return refined_mask

            refined_predictions = np.array(apply_morphological_operations(binary_predictions))

            def keep_largest_connected_component(binary_mask):
                labeled_mask, num_features = label(binary_mask, connectivity=2, return_num=True)
                props = regionprops(labeled_mask)
                largest_area = 0
                largest_label = 0
                for prop in props:
                    if prop.area > largest_area:
                        largest_area = prop.area
                        largest_label = prop.label
                largest_component_mask = (labeled_mask == largest_label).astype(np.uint8)
                return largest_component_mask

            largest_component_predictions = np.array(keep_largest_connected_component(refined_predictions))

            # print(f"Largest component predictions shape: {largest_component_predictions.shape}")

            # display_image(largest_component_predictions)

            ellipse_parameters = []
            contours, _ = cv2.findContours(largest_component_predictions.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                self.ellipse_params = cv2.fitEllipse(contours[0])
                # display_image_with_ellipse(resized_test_images, ellipse_params)
                pixel_size_input = self.ui.pixelSizeText.text()

                if pixel_size_input and pixel_size_input.replace('.', '', 1).isdigit():
                    pixel_size_value = float(pixel_size_input)

                else:
                    pixel_size_value = 1.0

                semi_major_axis = self.ellipse_params[1][0] / 2.0
                semi_minor_axis = self.ellipse_params[1][1] / 2.0

                circumference_pixels = math.pi * math.sqrt(2 * (semi_major_axis**2 + semi_minor_axis**2))
                BPD = semi_major_axis * pixel_size_value * 2
                OFD = semi_minor_axis * pixel_size_value * 2
                HC = math.pi * (BPD + OFD) / 2

                circumference_desired_unit = circumference_pixels * pixel_size_value


                if pixel_size_value != 0:
                    GA_poly = 1.49*(HC/10)+0.13*(HC/10)**2+73.38
                    # print(f"GA_poly: {GA_poly}")
                    # Convert to weeks and days
                    weeks_poly = int(GA_poly // 7)
                    remaining_days_poly = round(GA_poly % 7)
                else:
                    weeks_poly = 0
                    remaining_days_poly = 0
                # print(f"{int(weeks)} weeks and {remaining_days:.4f} days")

                self.ui.HCtextLabel.setText(f"HC: {HC:.2f} mm")
                self.ui.GAtextLabel.setText(f"GA: {weeks_poly}w {remaining_days_poly}d")
                self.ui.OFDtextLabel.setText(f"OFD: {OFD:.2f} mm")
                self.ui.BPDtextLabel.setText(f"BPD: {BPD:.2f} mm")

                self.showImage(self.imageNumpy, self.ellipse_params)
                self.ui.save_Button.setEnabled(True)


        except Exception as e:
            print("Error making prediction:", str(e))

    def savePrediction(self):
        HC = self.ui.HCtextLabel.text()
        GA = self.ui.GAtextLabel.text()
        OFD = self.ui.OFDtextLabel.text()
        BPD = self.ui.BPDtextLabel.text()

        # Example dictionary
        data = {
            "HC": HC,
            "GA": GA,
            "OFD": OFD,
            "BPD": BPD
        }
        # Save the dictionary as a text file
        with open(self.fileName + "_metaData.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

        # Draw the ellipse on the image
        cv2.ellipse(self.imageNumpy, self.ellipse_params, (0, 255, 0), 2)  # Green ellipse with thickness of 2

        # Save the image as a JPEG file
        cv2.imwrite(self.fileName + "annotation.jpeg",  self.imageNumpy)



    def __init__(self, parent=None):
        self.modelFlag = False
        self.imageNumpy = np.array([])
        self.pixelSize = 0
        self.model = None
        self.pixelSizesDB = pd.DataFrame()
        self.fileName = None
        self.ellipse_params = None

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Reset
        self.reset()


        # Create a QGraphicsScene and set it for the QGraphicsView
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # Set the window title
        self.setWindowTitle("Automatic Fetal Head Biometry Estimation - Br3in UNIVPM")

        # Set window icon
        self.setWindowIcon(QIcon('3.png'))

        # Load csv files
        self.create_DB()

        # load the model
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        self.load_the_network()

        self.ui.exit_Button.clicked.connect(self.close)
        self.ui.predict_Button.clicked.connect(self.make_prediction)
        self.ui.loadImage_Button.clicked.connect(self.select_files)
        self.ui.save_Button.clicked.connect(self.savePrediction)
        self.ui.pixelSizeText.setPlaceholderText("Pixel Size")

        # Validator to constrain input
        validator = QRegularExpressionValidator("[0-9.]+")
        self.ui.pixelSizeText.setValidator(validator)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Set dark theme
    set_dark_theme()

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


