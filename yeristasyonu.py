# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonhaliexccMs.ui'
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
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)
import istasyon_icon_rc
import istasyon_icon_rc
import istasyon_icon_rc
import istasyon_icon_rc
import istasyon_icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1091, 741)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 694))
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

        self.waypoint_btn = QPushButton(self.veriler_alt_widget)
        self.waypoint_btn.setObjectName(u"waypoint_btn")

        self.verticalLayout_2.addWidget(self.waypoint_btn)


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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 882, 624))
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
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 6, 1, 1, 1)

        self.label_38 = QLabel(self.frame_6)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 8, 0, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.kalkcak_wp = QLabel(self.frame_6)
        self.kalkcak_wp.setObjectName(u"kalkcak_wp")

        self.gridLayout_6.addWidget(self.kalkcak_wp, 7, 1, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(False)

        self.gridLayout_6.addWidget(self.label_10, 6, 0, 1, 1)

        self.incek_wp = QLabel(self.frame_6)
        self.incek_wp.setObjectName(u"incek_wp")

        self.gridLayout_6.addWidget(self.incek_wp, 8, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 4, 1, 1, 1)

        self.label_34 = QLabel(self.frame_6)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 5, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 2, 1, 1, 1)

        self.current_waypoint_seq = QLabel(self.frame_6)
        self.current_waypoint_seq.setObjectName(u"current_waypoint_seq")

        self.gridLayout_6.addWidget(self.current_waypoint_seq, 1, 1, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_36 = QLabel(self.frame_6)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 7, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 7, 1, 1, 1, Qt.AlignTop)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_11)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 268, 26))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_13.addWidget(self.label_25)

        self.mavlink_lineedit = QLineEdit(self.layoutWidget)
        self.mavlink_lineedit.setObjectName(u"mavlink_lineedit")

        self.horizontalLayout_13.addWidget(self.mavlink_lineedit)

        self.mavlink_button = QPushButton(self.layoutWidget)
        self.mavlink_button.setObjectName(u"mavlink_button")

        self.horizontalLayout_13.addWidget(self.mavlink_button)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 50, 75, 24))
        self.capa_test_up = QPushButton(self.frame_11)
        self.capa_test_up.setObjectName(u"capa_test_up")
        self.capa_test_up.setGeometry(QRect(20, 60, 75, 24))
        self.capa_test_down = QPushButton(self.frame_11)
        self.capa_test_down.setObjectName(u"capa_test_down")
        self.capa_test_down.setGeometry(QRect(110, 60, 75, 24))
        self.reconnect_btn = QPushButton(self.frame_11)
        self.reconnect_btn.setObjectName(u"reconnect_btn")
        self.reconnect_btn.setGeometry(QRect(20, 40, 75, 24))
        self.disconnect_btn = QPushButton(self.frame_11)
        self.disconnect_btn.setObjectName(u"disconnect_btn")
        self.disconnect_btn.setGeometry(QRect(110, 40, 75, 24))

        self.gridLayout_5.addWidget(self.frame_11, 8, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_20)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 190, 75, 24))
        self.lineEdit = QLineEdit(self.frame_20)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 190, 113, 22))
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 160, 91, 16))

        self.verticalLayout_13.addWidget(self.frame_20)


        self.horizontalLayout_10.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 300))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.loadlcell_label = QLabel(self.frame_10)
        self.loadlcell_label.setObjectName(u"loadlcell_label")

        self.gridLayout_7.addWidget(self.loadlcell_label, 5, 0, 1, 1)

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

        self.loadcell_veriable = QLabel(self.frame_10)
        self.loadcell_veriable.setObjectName(u"loadcell_veriable")

        self.gridLayout_7.addWidget(self.loadcell_veriable, 5, 1, 1, 1)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_10)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 3, 0, 1, 1)

        self.rover_mod = QLabel(self.frame_10)
        self.rover_mod.setObjectName(u"rover_mod")

        self.gridLayout_7.addWidget(self.rover_mod, 6, 0, 1, 1)

        self.label_30 = QLabel(self.frame_10)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 6, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_17)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.force_arm_btn = QPushButton(self.frame_17)
        self.force_arm_btn.setObjectName(u"force_arm_btn")

        self.gridLayout_9.addWidget(self.force_arm_btn, 1, 1, 1, 1)

        self.label_31 = QLabel(self.frame_17)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_9.addWidget(self.label_31, 0, 0, 1, 1)

        self.hold_btn = QPushButton(self.frame_17)
        self.hold_btn.setObjectName(u"hold_btn")

        self.gridLayout_9.addWidget(self.hold_btn, 1, 0, 1, 1)

        self.auto_mode_start_btn = QPushButton(self.frame_17)
        self.auto_mode_start_btn.setObjectName(u"auto_mode_start_btn")

        self.gridLayout_9.addWidget(self.auto_mode_start_btn, 0, 1, 1, 1)

        self.disarm_btn = QPushButton(self.frame_17)
        self.disarm_btn.setObjectName(u"disarm_btn")

        self.gridLayout_9.addWidget(self.disarm_btn, 2, 1, 1, 1)

        self.manual_btn = QPushButton(self.frame_17)
        self.manual_btn.setObjectName(u"manual_btn")

        self.gridLayout_9.addWidget(self.manual_btn, 2, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_17)


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
        self.textEdit.setReadOnly(True)

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
        self.waypoint = QWidget()
        self.waypoint.setObjectName(u"waypoint")
        self.verticalLayout_9 = QVBoxLayout(self.waypoint)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_12 = QFrame(self.waypoint)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setMaximumSize(QSize(16777215, 250))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_28 = QLabel(self.frame_16)
        self.label_28.setObjectName(u"label_28")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_28.setFont(font4)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_28)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_15)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.capa_kalk_wp = QLineEdit(self.frame_15)
        self.capa_kalk_wp.setObjectName(u"capa_kalk_wp")
        self.capa_kalk_wp.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_8.addWidget(self.capa_kalk_wp, 4, 1, 1, 1)

        self.label_35 = QLabel(self.frame_15)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_8.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_8.addWidget(self.label_32, 7, 0, 1, 1)

        self.clear_elemets = QPushButton(self.frame_15)
        self.clear_elemets.setObjectName(u"clear_elemets")

        self.gridLayout_8.addWidget(self.clear_elemets, 1, 1, 1, 1)

        self.label_27 = QLabel(self.frame_15)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_8.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_26 = QLabel(self.frame_15)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_8.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_33 = QLabel(self.frame_15)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_8.addWidget(self.label_33, 4, 0, 1, 1)

        self.get_gps_button = QPushButton(self.frame_15)
        self.get_gps_button.setObjectName(u"get_gps_button")

        self.gridLayout_8.addWidget(self.get_gps_button, 2, 1, 1, 1)

        self.send_waypoints_button = QPushButton(self.frame_15)
        self.send_waypoints_button.setObjectName(u"send_waypoints_button")
        self.send_waypoints_button.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.send_waypoints_button, 3, 1, 1, 1)

        self.mission_wp_send_btn = QPushButton(self.frame_15)
        self.mission_wp_send_btn.setObjectName(u"mission_wp_send_btn")

        self.gridLayout_8.addWidget(self.mission_wp_send_btn, 6, 0, 1, 1)

        self.capa_in_wp = QLineEdit(self.frame_15)
        self.capa_in_wp.setObjectName(u"capa_in_wp")
        self.capa_in_wp.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_8.addWidget(self.capa_in_wp, 5, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 300))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.waypoint_edit_line = QTextEdit(self.frame_19)
        self.waypoint_edit_line.setObjectName(u"waypoint_edit_line")

        self.horizontalLayout_15.addWidget(self.waypoint_edit_line)

        self.waypoint_list = QTextEdit(self.frame_19)
        self.waypoint_list.setObjectName(u"waypoint_list")
        self.waypoint_list.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.waypoint_list)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.label_29 = QLabel(self.frame_14)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_11.addWidget(self.label_29)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.send_cord_btn = QPushButton(self.frame_18)
        self.send_cord_btn.setObjectName(u"send_cord_btn")

        self.horizontalLayout_14.addWidget(self.send_cord_btn)

        self.gps_manual_add = QLineEdit(self.frame_18)
        self.gps_manual_add.setObjectName(u"gps_manual_add")

        self.horizontalLayout_14.addWidget(self.gps_manual_add)


        self.verticalLayout_11.addWidget(self.frame_18)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.sayfalar.addWidget(self.waypoint)

        self.gridLayout.addWidget(self.sayfalar, 0, 0, 1, 1)

        self.sayfalar_scrollarea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.sayfalar_scrollarea)

        self.splitter.addWidget(self.anasema_widget)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1091, 22))
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
        self.waypoint_btn.setText(QCoreApplication.translate("MainWindow", u"Waypoint Kaydetme", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SOLARI", None))
        self.home_icon.setText("")
        self.anasayfa_baslik_text.setText(QCoreApplication.translate("MainWindow", u"Anasayfa", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u00c7apa indirilcek", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"S\u0131ra aras\u0131na girme", None))
        self.kalkcak_wp.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Topra\u011f\u0131 i\u015fleme", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Aktif waypoint", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Engeli A\u015fma", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ik\u0131nc\u0131 s\u0131raya ge\u00e7me", None))
        self.incek_wp.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"S\u0131ra aras\u0131nda ilerleme", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.current_waypoint_seq.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"G\u00f6revler", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u00c7apa kald\u0131r\u0131lcak", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Mavlink", None))
        self.mavlink_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"com6", None))
        self.mavlink_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.capa_test_up.setText(QCoreApplication.translate("MainWindow", u"kalk", None))
        self.capa_test_down.setText(QCoreApplication.translate("MainWindow", u"in", None))
        self.reconnect_btn.setText(QCoreApplication.translate("MainWindow", u"reconnect", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"diconnect", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"resume", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"resume at wp", None))
        self.loadlcell_label.setText(QCoreApplication.translate("MainWindow", u"Loadcell_raw:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Batarya Seviyes:", None))
        self.dht11_veriable.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.dht11_label.setText(QCoreApplication.translate("MainWindow", u"Ara\u00e7 i\u00e7i s\u0131cakl\u0131k: ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u00c7apa g\u00f6revi", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.loadcell_veriable.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Mavlink Baglant\u0131s\u0131", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ag Baglant\u0131\u0131s\u0131", None))
        self.rover_mod.setText(QCoreApplication.translate("MainWindow", u"Arac\u0131n modu", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.force_arm_btn.setText(QCoreApplication.translate("MainWindow", u"Force-arm", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Auto Mode start", None))
        self.hold_btn.setText(QCoreApplication.translate("MainWindow", u"HOLD", None))
        self.auto_mode_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.disarm_btn.setText(QCoreApplication.translate("MainWindow", u"Disarm", None))
        self.manual_btn.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
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
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Record Waypoints", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u00c7apa indirilcek waypointler:", None))
        self.label_32.setText("")
        self.clear_elemets.setText(QCoreApplication.translate("MainWindow", u"remove list elements", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Waypointler yolla:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"GPS konumunu alma:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u00c7apa kalk\u0131cak waypointler:", None))
        self.get_gps_button.setText(QCoreApplication.translate("MainWindow", u"Get Gps ", None))
        self.send_waypoints_button.setText(QCoreApplication.translate("MainWindow", u"Send waypoints", None))
        self.mission_wp_send_btn.setText(QCoreApplication.translate("MainWindow", u"G\u00f6rev plan\u0131n\u0131 g\u00f6nder", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Manual kordinat girme:", None))
        self.send_cord_btn.setText(QCoreApplication.translate("MainWindow", u" Add", None))
    # retranslateUi

