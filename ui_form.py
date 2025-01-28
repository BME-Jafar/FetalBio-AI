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
        self.Buttons = QVBoxLayout()
        self.Buttons.setSpacing(20)
        self.Buttons.setObjectName(u"Buttons")
        self.newSub_Button = QPushButton(self.horizontalLayoutWidget)
        self.newSub_Button.setObjectName(u"newSub_Button")

        self.Buttons.addWidget(self.newSub_Button)

        self.loadImage_Button = QPushButton(self.horizontalLayoutWidget)
        self.loadImage_Button.setObjectName(u"loadImage_Button")

        self.Buttons.addWidget(self.loadImage_Button)

        self.predict_Button = QPushButton(self.horizontalLayoutWidget)
        self.predict_Button.setObjectName(u"predict_Button")
        self.predict_Button.setEnabled(False)

        self.Buttons.addWidget(self.predict_Button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pixelSizeText = QLineEdit(self.horizontalLayoutWidget)
        self.pixelSizeText.setObjectName(u"pixelSizeText")

        self.horizontalLayout_2.addWidget(self.pixelSizeText)

        self.unit = QLabel(self.horizontalLayoutWidget)
        self.unit.setObjectName(u"unit")

        self.horizontalLayout_2.addWidget(self.unit)


        self.Buttons.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.Buttons)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.HCtextLabel = QLabel(self.horizontalLayoutWidget)
        self.HCtextLabel.setObjectName(u"HCtextLabel")
        font = QFont()
        font.setPointSize(10)
        self.HCtextLabel.setFont(font)
        self.HCtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HCtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.HCtextLabel)

        self.BPDtextLabel = QLabel(self.horizontalLayoutWidget)
        self.BPDtextLabel.setObjectName(u"BPDtextLabel")
        self.BPDtextLabel.setFont(font)
        self.BPDtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BPDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.BPDtextLabel)

        self.OFDtextLabel = QLabel(self.horizontalLayoutWidget)
        self.OFDtextLabel.setObjectName(u"OFDtextLabel")
        self.OFDtextLabel.setFont(font)
        self.OFDtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.OFDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.OFDtextLabel)

        self.GAtextLabel = QLabel(self.horizontalLayoutWidget)
        self.GAtextLabel.setObjectName(u"GAtextLabel")
        self.GAtextLabel.setFont(font)
        self.GAtextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GAtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.GAtextLabel)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.save_Button = QPushButton(self.horizontalLayoutWidget)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(False)

        self.verticalLayout.addWidget(self.save_Button)

        self.exit_Button = QPushButton(self.horizontalLayoutWidget)
        self.exit_Button.setObjectName(u"exit_Button")

        self.verticalLayout.addWidget(self.exit_Button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy2)

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
        self.newSub_Button.setText(QCoreApplication.translate("MainWindow", u"New Subject", None))
        self.loadImage_Button.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.predict_Button.setText(QCoreApplication.translate("MainWindow", u"Make Predictions", None))
        self.unit.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.HCtextLabel.setText(QCoreApplication.translate("MainWindow", u"HC: mm", None))
        self.BPDtextLabel.setText(QCoreApplication.translate("MainWindow", u"BPD: mm", None))
        self.OFDtextLabel.setText(QCoreApplication.translate("MainWindow", u"OFD: mm", None))
        self.GAtextLabel.setText(QCoreApplication.translate("MainWindow", u"PGA: W; D", None))
        self.save_Button.setText(QCoreApplication.translate("MainWindow", u"Save Pridections", None))
        self.exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

