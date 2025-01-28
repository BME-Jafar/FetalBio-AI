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
        MainWindow.resize(1095, 712)
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
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 1051, 651))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ControlPanelLabel = QLabel(self.horizontalLayoutWidget)
        self.ControlPanelLabel.setObjectName(u"ControlPanelLabel")
        self.ControlPanelLabel.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ControlPanelLabel.sizePolicy().hasHeightForWidth())
        self.ControlPanelLabel.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.ControlPanelLabel.setFont(font)
        self.ControlPanelLabel.setScaledContents(False)
        self.ControlPanelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ControlPanelLabel.setIndent(1)

        self.verticalLayout.addWidget(self.ControlPanelLabel)

        self.Buttons = QVBoxLayout()
        self.Buttons.setSpacing(20)
        self.Buttons.setObjectName(u"Buttons")
        self.loadImage_Button = QPushButton(self.horizontalLayoutWidget)
        self.loadImage_Button.setObjectName(u"loadImage_Button")

        self.Buttons.addWidget(self.loadImage_Button)

        self.predict_Button = QPushButton(self.horizontalLayoutWidget)
        self.predict_Button.setObjectName(u"predict_Button")
        self.predict_Button.setEnabled(False)

        self.Buttons.addWidget(self.predict_Button)

        self.save_Button = QPushButton(self.horizontalLayoutWidget)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(False)

        self.Buttons.addWidget(self.save_Button)

        self.exit_Button = QPushButton(self.horizontalLayoutWidget)
        self.exit_Button.setObjectName(u"exit_Button")

        self.Buttons.addWidget(self.exit_Button)

        self.pixelSizeText = QLineEdit(self.horizontalLayoutWidget)
        self.pixelSizeText.setObjectName(u"pixelSizeText")

        self.Buttons.addWidget(self.pixelSizeText)


        self.verticalLayout.addLayout(self.Buttons)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.HCtextLabel = QLabel(self.horizontalLayoutWidget)
        self.HCtextLabel.setObjectName(u"HCtextLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.HCtextLabel.setFont(font1)
        self.HCtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HCtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.HCtextLabel)

        self.GAtextLabel = QLabel(self.horizontalLayoutWidget)
        self.GAtextLabel.setObjectName(u"GAtextLabel")
        self.GAtextLabel.setFont(font1)
        self.GAtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GAtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.GAtextLabel)

        self.BPDtextLabel = QLabel(self.horizontalLayoutWidget)
        self.BPDtextLabel.setObjectName(u"BPDtextLabel")
        self.BPDtextLabel.setFont(font1)
        self.BPDtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BPDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.BPDtextLabel)

        self.OFDtextLabel = QLabel(self.horizontalLayoutWidget)
        self.OFDtextLabel.setObjectName(u"OFDtextLabel")
        self.OFDtextLabel.setFont(font1)
        self.OFDtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.OFDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.OFDtextLabel)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.graphicsView)

        self.horizontalLayout.setStretch(1, 1)
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
        self.ControlPanelLabel.setText(QCoreApplication.translate("MainWindow", u"    Control Panel", None))
        self.loadImage_Button.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.predict_Button.setText(QCoreApplication.translate("MainWindow", u"Make Predictions", None))
        self.save_Button.setText(QCoreApplication.translate("MainWindow", u"Save Pridections", None))
        self.exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.HCtextLabel.setText(QCoreApplication.translate("MainWindow", u"HC: [mm]", None))
        self.GAtextLabel.setText(QCoreApplication.translate("MainWindow", u"GA: W; D", None))
        self.BPDtextLabel.setText(QCoreApplication.translate("MainWindow", u"BPD: [mm]", None))
        self.OFDtextLabel.setText(QCoreApplication.translate("MainWindow", u"OFD: [mm]", None))
    # retranslateUi

