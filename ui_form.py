# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 735)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(1084, 16777215))
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.centralwidget.setAutoFillBackground(True)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 1061, 685))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PatientLayout = QHBoxLayout()
        self.PatientLayout.setObjectName(u"PatientLayout")

        self.verticalLayout_2.addLayout(self.PatientLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Buttons = QVBoxLayout()
        self.Buttons.setSpacing(20)
        self.Buttons.setObjectName(u"Buttons")
        self.logoUNIVPM = QGraphicsView(self.verticalLayoutWidget)
        self.logoUNIVPM.setObjectName(u"logoUNIVPM")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logoUNIVPM.sizePolicy().hasHeightForWidth())
        self.logoUNIVPM.setSizePolicy(sizePolicy2)

        self.Buttons.addWidget(self.logoUNIVPM)

        self.newSub_Button = QPushButton(self.verticalLayoutWidget)
        self.newSub_Button.setObjectName(u"newSub_Button")

        self.Buttons.addWidget(self.newSub_Button)

        self.loadImage_Button = QPushButton(self.verticalLayoutWidget)
        self.loadImage_Button.setObjectName(u"loadImage_Button")
        self.loadImage_Button.setEnabled(False)

        self.Buttons.addWidget(self.loadImage_Button)

        self.predict_Button = QPushButton(self.verticalLayoutWidget)
        self.predict_Button.setObjectName(u"predict_Button")
        self.predict_Button.setEnabled(False)

        self.Buttons.addWidget(self.predict_Button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pixelSizeText = QLineEdit(self.verticalLayoutWidget)
        self.pixelSizeText.setObjectName(u"pixelSizeText")

        self.horizontalLayout_2.addWidget(self.pixelSizeText)

        self.unit = QLabel(self.verticalLayoutWidget)
        self.unit.setObjectName(u"unit")

        self.horizontalLayout_2.addWidget(self.unit)


        self.Buttons.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.Buttons)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.HCtextLabel = QLabel(self.verticalLayoutWidget)
        self.HCtextLabel.setObjectName(u"HCtextLabel")
        font = QFont()
        font.setPointSize(10)
        self.HCtextLabel.setFont(font)
        self.HCtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HCtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.HCtextLabel)

        self.BPDtextLabel = QLabel(self.verticalLayoutWidget)
        self.BPDtextLabel.setObjectName(u"BPDtextLabel")
        self.BPDtextLabel.setFont(font)
        self.BPDtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BPDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.BPDtextLabel)

        self.OFDtextLabel = QLabel(self.verticalLayoutWidget)
        self.OFDtextLabel.setObjectName(u"OFDtextLabel")
        self.OFDtextLabel.setFont(font)
        self.OFDtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.OFDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.OFDtextLabel)

        self.GAtextLabel = QLabel(self.verticalLayoutWidget)
        self.GAtextLabel.setObjectName(u"GAtextLabel")
        self.GAtextLabel.setFont(font)
        self.GAtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GAtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.GAtextLabel)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.save_Button = QPushButton(self.verticalLayoutWidget)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(False)

        self.verticalLayout.addWidget(self.save_Button)

        self.exit_Button = QPushButton(self.verticalLayoutWidget)
        self.exit_Button.setObjectName(u"exit_Button")

        self.verticalLayout.addWidget(self.exit_Button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.graphicsView)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.contactUs_Layout = QHBoxLayout()
        self.contactUs_Layout.setObjectName(u"contactUs_Layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.contactUs_Layout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)


        self.contactUs_Layout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.contactUs_Layout)

        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1095, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.newSub_Button.setText(QCoreApplication.translate("MainWindow", u"New Subject", None))
        self.loadImage_Button.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.predict_Button.setText(QCoreApplication.translate("MainWindow", u"Make Prediction", None))
        self.unit.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.HCtextLabel.setText(QCoreApplication.translate("MainWindow", u"HC: mm", None))
        self.BPDtextLabel.setText(QCoreApplication.translate("MainWindow", u"BPD: mm", None))
        self.OFDtextLabel.setText(QCoreApplication.translate("MainWindow", u"OFD: mm", None))
        self.GAtextLabel.setText(QCoreApplication.translate("MainWindow", u"PGA: W; D", None))
        self.save_Button.setText(QCoreApplication.translate("MainWindow", u"Save Prediction", None))
        self.exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contact Us:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Professor: Laura Burattini", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"l.burattini@univpm.it", None))
    # retranslateUi

