# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 463)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 591, 391))
        self.Main = QVBoxLayout(self.verticalLayoutWidget)
        self.Main.setObjectName(u"Main")
        self.Main.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.Main.addWidget(self.label)

        self.motherLayout = QVBoxLayout()
        self.motherLayout.setObjectName(u"motherLayout")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.motherLayout.addWidget(self.label_12)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.IDinput = QLineEdit(self.verticalLayoutWidget)
        self.IDinput.setObjectName(u"IDinput")

        self.verticalLayout_6.addWidget(self.IDinput)

        self.AgeInput = QLineEdit(self.verticalLayoutWidget)
        self.AgeInput.setObjectName(u"AgeInput")

        self.verticalLayout_6.addWidget(self.AgeInput)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_6.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_6.addWidget(self.lineEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_11)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.GravidityBox = QComboBox(self.verticalLayoutWidget)
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.setObjectName(u"GravidityBox")

        self.verticalLayout_8.addWidget(self.GravidityBox)

        self.ParityBox = QComboBox(self.verticalLayoutWidget)
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.setObjectName(u"ParityBox")

        self.verticalLayout_8.addWidget(self.ParityBox)

        self.diabetesBool = QCheckBox(self.verticalLayoutWidget)
        self.diabetesBool.setObjectName(u"diabetesBool")

        self.verticalLayout_8.addWidget(self.diabetesBool)

        self.hypertensionBool = QCheckBox(self.verticalLayoutWidget)
        self.hypertensionBool.setObjectName(u"hypertensionBool")

        self.verticalLayout_8.addWidget(self.hypertensionBool)

        self.preeclampsiaBool = QCheckBox(self.verticalLayoutWidget)
        self.preeclampsiaBool.setObjectName(u"preeclampsiaBool")

        self.verticalLayout_8.addWidget(self.preeclampsiaBool)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.motherLayout.addLayout(self.horizontalLayout_2)

        self.motherLayout.setStretch(1, 1)

        self.Main.addLayout(self.motherLayout)

        self.FetusLayout = QVBoxLayout()
        self.FetusLayout.setObjectName(u"FetusLayout")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.FetusLayout.addWidget(self.label_13)


        self.Main.addLayout(self.FetusLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_3.addWidget(self.lineEdit_4)

        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)


        self.Main.addLayout(self.horizontalLayout_3)

        self.sexLayout = QHBoxLayout()
        self.sexLayout.setObjectName(u"sexLayout")
        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.sexLayout.addWidget(self.label_17)

        self.sexBox = QComboBox(self.verticalLayoutWidget)
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.sexBox.setObjectName(u"sexBox")

        self.sexLayout.addWidget(self.sexBox)


        self.Main.addLayout(self.sexLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_18)

        self.dateEdit = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_6.addWidget(self.dateEdit)


        self.Main.addLayout(self.horizontalLayout_6)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 420, 141, 31))
        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 420, 171, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Please enter the following information", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Mother's Inoformation", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ID *", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Age * ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Weight (Kg)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Height (cm)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"BMI", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Gravidity", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Parity", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Diabetes", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Hypertension", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Preeclampsia", None))
        self.GravidityBox.setItemText(0, QCoreApplication.translate("Form", u"Unknown", None))
        self.GravidityBox.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.GravidityBox.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.GravidityBox.setItemText(3, QCoreApplication.translate("Form", u"3", None))
        self.GravidityBox.setItemText(4, QCoreApplication.translate("Form", u"4", None))
        self.GravidityBox.setItemText(5, QCoreApplication.translate("Form", u"5", None))
        self.GravidityBox.setItemText(6, QCoreApplication.translate("Form", u">5", None))

        self.ParityBox.setItemText(0, QCoreApplication.translate("Form", u"Unknown", None))
        self.ParityBox.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.ParityBox.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.ParityBox.setItemText(3, QCoreApplication.translate("Form", u"3", None))
        self.ParityBox.setItemText(4, QCoreApplication.translate("Form", u"4", None))
        self.ParityBox.setItemText(5, QCoreApplication.translate("Form", u"5", None))
        self.ParityBox.setItemText(6, QCoreApplication.translate("Form", u">5", None))

        self.diabetesBool.setText("")
        self.hypertensionBool.setText("")
        self.preeclampsiaBool.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Fetus's Information", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"GA*", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"D", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"W", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Sex", None))
        self.sexBox.setItemText(0, QCoreApplication.translate("Form", u"Unknown", None))
        self.sexBox.setItemText(1, QCoreApplication.translate("Form", u"Male", None))
        self.sexBox.setItemText(2, QCoreApplication.translate("Form", u"Female", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"EDD*: ", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Done", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Feilds with * are mandatory.", None))
    # retranslateUi

