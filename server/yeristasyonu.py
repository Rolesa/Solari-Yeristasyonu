# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonhalimqrLls.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)
import istasyon_icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1066, 719)
        MainWindow.setMinimumSize(QSize(1066, 719))
        MainWindow.setStyleSheet(u"#ust_baslik_widget{\n"
"	\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"#home_btn{\n"
"	padding-left: 15px;\n"
"	padding-top: 5px;\n"
"	padding-bottom:5 px;\n"
"}\n"
"#menu_widget QPushButton {\n"
"	border:none;\n"
"	text-align: left;\n"
"}\n"
"#menu_widget QPushButton:hover, #veriler_widget:hover,#sensor_widget:hover{\n"
"	\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"#menu_widget QPushButton:disabled {\n"
"	background-color: rgb(222, 222, 222);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"#sensorler_alt_widget QPushButton, #veriler_alt_widget QPushButton{\n"
"	padding-left: 40px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"#start_btn:hover , #stop_btn:hover, #close_btn:hover{\n"
"	background-color: rgb(222,222,222);\n"
"	color:rgb(0,0,0)\n"
"}\n"
"#menu_widget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: solid 1px rgb(0,0,0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(200, 200))
        self.scrollArea.setMaximumSize(QSize(200, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 672))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_widget = QWidget(self.scrollAreaWidgetContents)
        self.menu_widget.setObjectName(u"menu_widget")
        self.verticalLayout_3 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.home_widget = QWidget(self.menu_widget)
        self.home_widget.setObjectName(u"home_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.home_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.home_btn = QPushButton(self.home_widget)
        self.home_btn.setObjectName(u"home_btn")
        icon = QIcon()
        icon.addFile(u":/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.home_btn)


        self.verticalLayout_3.addWidget(self.home_widget)

        self.sensor_widget = QWidget(self.menu_widget)
        self.sensor_widget.setObjectName(u"sensor_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.sensor_widget)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 5, 15, 5)
        self.sensor_pixmap = QLabel(self.sensor_widget)
        self.sensor_pixmap.setObjectName(u"sensor_pixmap")
        self.sensor_pixmap.setMaximumSize(QSize(16, 15))
        self.sensor_pixmap.setPixmap(QPixmap(u":/icons/radio.svg"))
        self.sensor_pixmap.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.sensor_pixmap)

        self.sensor_btn = QPushButton(self.sensor_widget)
        self.sensor_btn.setObjectName(u"sensor_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensor_btn.setIcon(icon1)
        self.sensor_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.sensor_btn)


        self.verticalLayout_3.addWidget(self.sensor_widget)

        self.sensorler_alt_widget = QWidget(self.menu_widget)
        self.sensorler_alt_widget.setObjectName(u"sensorler_alt_widget")
        self.verticalLayout = QVBoxLayout(self.sensorler_alt_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lidar_btn = QPushButton(self.sensorler_alt_widget)
        self.lidar_btn.setObjectName(u"lidar_btn")

        self.verticalLayout.addWidget(self.lidar_btn)

        self.mesafe_btn = QPushButton(self.sensorler_alt_widget)
        self.mesafe_btn.setObjectName(u"mesafe_btn")

        self.verticalLayout.addWidget(self.mesafe_btn)

        self.kamera_btn = QPushButton(self.sensorler_alt_widget)
        self.kamera_btn.setObjectName(u"kamera_btn")

        self.verticalLayout.addWidget(self.kamera_btn)


        self.verticalLayout_3.addWidget(self.sensorler_alt_widget)

        self.veriler_widget = QWidget(self.menu_widget)
        self.veriler_widget.setObjectName(u"veriler_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.veriler_widget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 5, 15, 5)
        self.veriler_pixmap = QLabel(self.veriler_widget)
        self.veriler_pixmap.setObjectName(u"veriler_pixmap")
        self.veriler_pixmap.setMaximumSize(QSize(16, 16))
        self.veriler_pixmap.setPixmap(QPixmap(u":/icons/eye.svg"))
        self.veriler_pixmap.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.veriler_pixmap)

        self.veriler_btn = QPushButton(self.veriler_widget)
        self.veriler_btn.setObjectName(u"veriler_btn")
        self.veriler_btn.setIcon(icon1)
        self.veriler_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.veriler_btn)


        self.verticalLayout_3.addWidget(self.veriler_widget)

        self.veriler_alt_widget = QWidget(self.menu_widget)
        self.veriler_alt_widget.setObjectName(u"veriler_alt_widget")
        self.verticalLayout_2 = QVBoxLayout(self.veriler_alt_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.goruntu_btn = QPushButton(self.veriler_alt_widget)
        self.goruntu_btn.setObjectName(u"goruntu_btn")

        self.verticalLayout_2.addWidget(self.goruntu_btn)

        self.veriler_sensor_btn = QPushButton(self.veriler_alt_widget)
        self.veriler_sensor_btn.setObjectName(u"veriler_sensor_btn")

        self.verticalLayout_2.addWidget(self.veriler_sensor_btn)

        self.hareket_btn = QPushButton(self.veriler_alt_widget)
        self.hareket_btn.setObjectName(u"hareket_btn")

        self.verticalLayout_2.addWidget(self.hareket_btn)


        self.verticalLayout_3.addWidget(self.veriler_alt_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.menu_widget, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(60, 60))
        self.widget_2.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icons/system-customer-service-line-svgrepo-com.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)
        self.anasema_widget = QWidget(self.splitter)
        self.anasema_widget.setObjectName(u"anasema_widget")
        self.verticalLayout_4 = QVBoxLayout(self.anasema_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ust_baslik_widget = QWidget(self.anasema_widget)
        self.ust_baslik_widget.setObjectName(u"ust_baslik_widget")
        self.ust_baslik_widget.setMinimumSize(QSize(60, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.ust_baslik_widget)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.home_icon = QLabel(self.ust_baslik_widget)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setMinimumSize(QSize(30, 30))
        self.home_icon.setMaximumSize(QSize(30, 30))
        self.home_icon.setPixmap(QPixmap(u":/icons/home.svg"))
        self.home_icon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.home_icon)

        self.anasayfa_baslik_text = QLabel(self.ust_baslik_widget)
        self.anasayfa_baslik_text.setObjectName(u"anasayfa_baslik_text")
        font1 = QFont()
        font1.setFamilies([u"Quicksand"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.anasayfa_baslik_text.setFont(font1)

        self.horizontalLayout_5.addWidget(self.anasayfa_baslik_text)

        self.horizontalSpacer_3 = QSpacerItem(718, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.ust_baslik_widget)

        self.sayfalar_scrollarea = QScrollArea(self.anasema_widget)
        self.sayfalar_scrollarea.setObjectName(u"sayfalar_scrollarea")
        self.sayfalar_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 857, 602))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sayfalar = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.sayfalar.setObjectName(u"sayfalar")
        self.sayfalar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.anasayfa = QWidget()
        self.anasayfa.setObjectName(u"anasayfa")
        self.anasayfa.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.anasayfa)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.anasayfa)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setTabletTracking(False)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 300))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 4, 1, 1, 1)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(False)

        self.gridLayout_6.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 5, 1, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 6, 0, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 6, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 7, 1, 1, 1, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 300))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_27 = QLabel(self.frame_10)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 5, 0, 1, 1)

        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 3, 1, 1, 1)

        self.label_22 = QLabel(self.frame_10)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_7.addWidget(self.label_22, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 0, 0, 1, 1)

        self.dht11_veriable = QLabel(self.frame_10)
        self.dht11_veriable.setObjectName(u"dht11_veriable")

        self.gridLayout_7.addWidget(self.dht11_veriable, 4, 1, 1, 1)

        self.dht11_label = QLabel(self.frame_10)
        self.dht11_label.setObjectName(u"dht11_label")

        self.gridLayout_7.addWidget(self.dht11_label, 4, 0, 1, 1)

        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_21 = QLabel(self.frame_10)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_23 = QLabel(self.frame_10)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_10)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 5, 1, 1, 1)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_10)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_29 = QLabel(self.frame_10)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 6, 0, 1, 1)

        self.label_30 = QLabel(self.frame_10)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 6, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.frame_10, 0, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_9)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.anasayfa)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 400))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_4)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_11.addWidget(self.textEdit)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.sayfalar.addWidget(self.anasayfa)
        self.kamera = QWidget()
        self.kamera.setObjectName(u"kamera")
        self.kamera.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"#start_btn:hover , #stop_btn:hover, #close_btn:hover{\n"
"	background-color: rgb(222,222,222);\n"
"	color:rgb(0,0,0)\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.kamera)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.kamera)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.top_frame = QFrame(self.frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 9)
        self.start_btn = QPushButton(self.top_frame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMinimumSize(QSize(100, 32))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.start_btn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.top_frame)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(100, 32))
        font3 = QFont()
        font3.setBold(False)
        self.stop_btn.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.stop_btn)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(100, 32))
        self.close_btn.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.close_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addWidget(self.top_frame, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.camera_frame = QFrame(self.frame_3)
        self.camera_frame.setObjectName(u"camera_frame")
        sizePolicy.setHeightForWidth(self.camera_frame.sizePolicy().hasHeightForWidth())
        self.camera_frame.setSizePolicy(sizePolicy)
        self.camera_frame.setStyleSheet(u"")
        self.camera_frame.setFrameShape(QFrame.StyledPanel)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.camera_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.viewData = QLabel(self.camera_frame)
        self.viewData.setObjectName(u"viewData")
        self.viewData.setStyleSheet(u"*{\n"
"border: 1px solid black;\n"
"}")

        self.horizontalLayout_8.addWidget(self.viewData)


        self.horizontalLayout_7.addWidget(self.camera_frame)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 500))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bilgiler = QFrame(self.frame_5)
        self.bilgiler.setObjectName(u"bilgiler")
        self.bilgiler.setStyleSheet(u"")
        self.bilgiler.setFrameShape(QFrame.StyledPanel)
        self.bilgiler.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.bilgiler)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sayi_label = QLabel(self.bilgiler)
        self.sayi_label.setObjectName(u"sayi_label")

        self.gridLayout_4.addWidget(self.sayi_label, 1, 0, 1, 1)

        self.isim_Label = QLabel(self.bilgiler)
        self.isim_Label.setObjectName(u"isim_Label")

        self.gridLayout_4.addWidget(self.isim_Label, 0, 1, 1, 1)

        self.konum_label = QLabel(self.bilgiler)
        self.konum_label.setObjectName(u"konum_label")

        self.gridLayout_4.addWidget(self.konum_label, 2, 0, 1, 1)

        self.isim_label = QLabel(self.bilgiler)
        self.isim_label.setObjectName(u"isim_label")

        self.gridLayout_4.addWidget(self.isim_label, 0, 0, 1, 1)

        self.sayi_Label = QLabel(self.bilgiler)
        self.sayi_Label.setObjectName(u"sayi_Label")

        self.gridLayout_4.addWidget(self.sayi_Label, 1, 1, 1, 1)

        self.konum_Label = QLabel(self.bilgiler)
        self.konum_Label.setObjectName(u"konum_Label")

        self.gridLayout_4.addWidget(self.konum_Label, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.bilgiler)

        self.goruntu_frame = QFrame(self.frame_5)
        self.goruntu_frame.setObjectName(u"goruntu_frame")
        self.goruntu_frame.setStyleSheet(u"")
        self.goruntu_frame.setFrameShape(QFrame.StyledPanel)
        self.goruntu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.goruntu_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tespit_goruntu_label = QLabel(self.goruntu_frame)
        self.tespit_goruntu_label.setObjectName(u"tespit_goruntu_label")
        self.tespit_goruntu_label.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.tespit_goruntu_label)


        self.verticalLayout_7.addWidget(self.goruntu_frame)


        self.horizontalLayout_7.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame)

        self.sayfalar.addWidget(self.kamera)
        self.sensorler = QWidget()
        self.sensorler.setObjectName(u"sensorler")
        self.label_4 = QLabel(self.sensorler)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 210, 54, 17))
        self.sayfalar.addWidget(self.sensorler)

        self.gridLayout.addWidget(self.sayfalar, 0, 0, 1, 1)

        self.sayfalar_scrollarea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.sayfalar_scrollarea)

        self.splitter.addWidget(self.anasema_widget)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1066, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sensor_btn.toggled.connect(self.sensorler_alt_widget.setVisible)
        self.veriler_btn.toggled.connect(self.veriler_alt_widget.setVisible)

        self.sayfalar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"    Anasayfa", None))
        self.sensor_pixmap.setText("")
        self.sensor_btn.setText(QCoreApplication.translate("MainWindow", u"Sensorler", None))
        self.lidar_btn.setText(QCoreApplication.translate("MainWindow", u"Lidar", None))
        self.mesafe_btn.setText(QCoreApplication.translate("MainWindow", u"Mesafe", None))
        self.kamera_btn.setText(QCoreApplication.translate("MainWindow", u"Kamera", None))
        self.veriler_pixmap.setText("")
        self.veriler_btn.setText(QCoreApplication.translate("MainWindow", u"Veriler", None))
        self.goruntu_btn.setText(QCoreApplication.translate("MainWindow", u"Goruntu", None))
        self.veriler_sensor_btn.setText(QCoreApplication.translate("MainWindow", u"Sensor", None))
        self.hareket_btn.setText(QCoreApplication.translate("MainWindow", u"Hareket", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SOLARI", None))
        self.home_icon.setText("")
        self.anasayfa_baslik_text.setText(QCoreApplication.translate("MainWindow", u"Anasayfa", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"G\u00f6revler", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"S\u0131ra aras\u0131na girme", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"S\u0131ra aras\u0131nda ilerleme", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Topra\u011f\u0131 i\u015fleme", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Engeli A\u015fma", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ik\u0131nc\u0131 s\u0131raya ge\u00e7me", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"S\u0131ra aras\u0131ndan \u00e7\u0131kma", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Motor Anl\u0131k De\u011fer:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Batarya Seviyes:", None))
        self.dht11_veriable.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.dht11_label.setText(QCoreApplication.translate("MainWindow", u"Ara\u00e7 i\u00e7i s\u0131cakl\u0131k: ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Aktif G\u00f6rev algoritmas\u0131:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Katedilen Konum:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ag Baglant\u0131\u0131s\u0131", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Motor Ortalama ak\u0131m:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Baslat", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Durdur", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"Kapat", None))
        self.viewData.setText("")
        self.sayi_label.setText(QCoreApplication.translate("MainWindow", u"Tespit Edilme Say\u0131s\u0131:", None))
        self.isim_Label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.konum_label.setText(QCoreApplication.translate("MainWindow", u"Son konumu:", None))
        self.isim_label.setText(QCoreApplication.translate("MainWindow", u"Tespit Edilecek Bitki :", None))
        self.sayi_Label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.konum_Label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tespit_goruntu_label.setText(QCoreApplication.translate("MainWindow", u"frame", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sensorler", None))
    # retranslateUi

