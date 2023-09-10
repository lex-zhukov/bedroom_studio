from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from __grafic__ import grafic
from __engine__ import engine
from __instext__ import text_of_instructions

grand_variants = []
grand_points = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1296, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.p2X = QtWidgets.QTextEdit(self.centralwidget)
        self.p2X.setGeometry(QtCore.QRect(110, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p2X.setFont(font)
        self.p2X.setObjectName("p2X")
        self.p2Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p2Y.setGeometry(QtCore.QRect(190, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p2Y.setFont(font)
        self.p2Y.setObjectName("p2Y")
        self.p4X = QtWidgets.QTextEdit(self.centralwidget)
        self.p4X.setGeometry(QtCore.QRect(110, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p4X.setFont(font)
        self.p4X.setObjectName("p4X")
        self.p4Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p4Y.setGeometry(QtCore.QRect(190, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p4Y.setFont(font)
        self.p4Y.setObjectName("p4Y")
        self.p3X = QtWidgets.QTextEdit(self.centralwidget)
        self.p3X.setGeometry(QtCore.QRect(110, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p3X.setFont(font)
        self.p3X.setObjectName("p3X")
        self.p3Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p3Y.setGeometry(QtCore.QRect(190, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p3Y.setFont(font)
        self.p3Y.setObjectName("p3Y")
        self.p8Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p8Y.setGeometry(QtCore.QRect(190, 410, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p8Y.setFont(font)
        self.p8Y.setObjectName("p8Y")
        self.p7X = QtWidgets.QTextEdit(self.centralwidget)
        self.p7X.setGeometry(QtCore.QRect(110, 360, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p7X.setFont(font)
        self.p7X.setObjectName("p7X")
        self.p7Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p7Y.setGeometry(QtCore.QRect(190, 360, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p7Y.setFont(font)
        self.p7Y.setObjectName("p7Y")
        self.p6X = QtWidgets.QTextEdit(self.centralwidget)
        self.p6X.setGeometry(QtCore.QRect(110, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p6X.setFont(font)
        self.p6X.setObjectName("p6X")
        self.p6Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p6Y.setGeometry(QtCore.QRect(190, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p6Y.setFont(font)
        self.p6Y.setObjectName("p6Y")
        self.p5X = QtWidgets.QTextEdit(self.centralwidget)
        self.p5X.setGeometry(QtCore.QRect(110, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p5X.setFont(font)
        self.p5X.setObjectName("p5X")
        self.p8X = QtWidgets.QTextEdit(self.centralwidget)
        self.p8X.setGeometry(QtCore.QRect(110, 410, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p8X.setFont(font)
        self.p8X.setObjectName("p8X")
        self.p5Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p5Y.setGeometry(QtCore.QRect(190, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p5Y.setFont(font)
        self.p5Y.setObjectName("p5Y")
        self.p9X = QtWidgets.QTextEdit(self.centralwidget)
        self.p9X.setGeometry(QtCore.QRect(110, 460, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p9X.setFont(font)
        self.p9X.setObjectName("p9X")
        self.p10Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p10Y.setGeometry(QtCore.QRect(190, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p10Y.setFont(font)
        self.p10Y.setObjectName("p10Y")
        self.p10X = QtWidgets.QTextEdit(self.centralwidget)
        self.p10X.setGeometry(QtCore.QRect(110, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p10X.setFont(font)
        self.p10X.setObjectName("p10X")
        self.p9Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p9Y.setGeometry(QtCore.QRect(190, 460, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p9Y.setFont(font)
        self.p9Y.setObjectName("p9Y")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 71, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 71, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 71, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 71, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 460, 71, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 310, 71, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 360, 71, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 410, 71, 41))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 510, 81, 41))
        self.label_12.setObjectName("label_12")
        self.p13Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p13Y.setGeometry(QtCore.QRect(190, 660, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p13Y.setFont(font)
        self.p13Y.setObjectName("p13Y")
        self.p14X = QtWidgets.QTextEdit(self.centralwidget)
        self.p14X.setGeometry(QtCore.QRect(110, 710, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p14X.setFont(font)
        self.p14X.setObjectName("p14X")
        self.p15X = QtWidgets.QTextEdit(self.centralwidget)
        self.p15X.setGeometry(QtCore.QRect(110, 760, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p15X.setFont(font)
        self.p15X.setObjectName("p15X")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(290, 160, 81, 41))
        self.label_13.setObjectName("label_13")
        self.p12X = QtWidgets.QTextEdit(self.centralwidget)
        self.p12X.setGeometry(QtCore.QRect(110, 610, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p12X.setFont(font)
        self.p12X.setObjectName("p12X")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 660, 81, 41))
        self.label_14.setObjectName("label_14")
        self.p17Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p17Y.setGeometry(QtCore.QRect(460, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p17Y.setFont(font)
        self.p17Y.setObjectName("p17Y")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 710, 81, 41))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 560, 81, 41))
        self.label_16.setObjectName("label_16")
        self.p16Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p16Y.setGeometry(QtCore.QRect(460, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p16Y.setFont(font)
        self.p16Y.setObjectName("p16Y")
        self.p18X = QtWidgets.QTextEdit(self.centralwidget)
        self.p18X.setGeometry(QtCore.QRect(380, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p18X.setFont(font)
        self.p18X.setObjectName("p18X")
        self.p19X = QtWidgets.QTextEdit(self.centralwidget)
        self.p19X.setGeometry(QtCore.QRect(380, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p19X.setFont(font)
        self.p19X.setObjectName("p19X")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 610, 81, 41))
        self.label_17.setObjectName("label_17")
        self.p16X = QtWidgets.QTextEdit(self.centralwidget)
        self.p16X.setGeometry(QtCore.QRect(380, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p16X.setFont(font)
        self.p16X.setObjectName("p16X")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(480, 10, 21, 41))
        self.label_18.setObjectName("label_18")
        self.p18Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p18Y.setGeometry(QtCore.QRect(460, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p18Y.setFont(font)
        self.p18Y.setObjectName("p18Y")
        self.p15Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p15Y.setGeometry(QtCore.QRect(190, 760, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p15Y.setFont(font)
        self.p15Y.setObjectName("p15Y")
        self.p11Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p11Y.setGeometry(QtCore.QRect(190, 560, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p11Y.setFont(font)
        self.p11Y.setObjectName("p11Y")
        self.p20X = QtWidgets.QTextEdit(self.centralwidget)
        self.p20X.setGeometry(QtCore.QRect(380, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p20X.setFont(font)
        self.p20X.setObjectName("p20X")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(290, 260, 81, 41))
        self.label_20.setObjectName("label_20")
        self.p13X = QtWidgets.QTextEdit(self.centralwidget)
        self.p13X.setGeometry(QtCore.QRect(110, 660, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p13X.setFont(font)
        self.p13X.setObjectName("p13X")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(400, 10, 21, 41))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(290, 110, 81, 41))
        self.label_22.setObjectName("label_22")
        self.p12Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p12Y.setGeometry(QtCore.QRect(190, 610, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p12Y.setFont(font)
        self.p12Y.setObjectName("p12Y")
        self.p17X = QtWidgets.QTextEdit(self.centralwidget)
        self.p17X.setGeometry(QtCore.QRect(380, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p17X.setFont(font)
        self.p17X.setObjectName("p17X")
        self.p19Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p19Y.setGeometry(QtCore.QRect(460, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p19Y.setFont(font)
        self.p19Y.setObjectName("p19Y")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(290, 210, 81, 41))
        self.label_23.setObjectName("label_23")
        self.p14Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p14Y.setGeometry(QtCore.QRect(190, 710, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p14Y.setFont(font)
        self.p14Y.setObjectName("p14Y")
        self.p20Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p20Y.setGeometry(QtCore.QRect(460, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p20Y.setFont(font)
        self.p20Y.setObjectName("p20Y")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(20, 760, 81, 41))
        self.label_24.setObjectName("label_24")
        self.p11X = QtWidgets.QTextEdit(self.centralwidget)
        self.p11X.setGeometry(QtCore.QRect(110, 560, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p11X.setFont(font)
        self.p11X.setObjectName("p11X")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(290, 310, 81, 41))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(290, 460, 81, 41))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(290, 760, 81, 41))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(290, 560, 81, 41))
        self.label_28.setObjectName("label_28")
        self.p28X = QtWidgets.QTextEdit(self.centralwidget)
        self.p28X.setGeometry(QtCore.QRect(380, 660, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p28X.setFont(font)
        self.p28X.setObjectName("p28X")
        self.p23X = QtWidgets.QTextEdit(self.centralwidget)
        self.p23X.setGeometry(QtCore.QRect(380, 410, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p23X.setFont(font)
        self.p23X.setObjectName("p23X")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(290, 660, 81, 41))
        self.label_30.setObjectName("label_30")
        self.p21Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p21Y.setGeometry(QtCore.QRect(460, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p21Y.setFont(font)
        self.p21Y.setObjectName("p21Y")
        self.p29X = QtWidgets.QTextEdit(self.centralwidget)
        self.p29X.setGeometry(QtCore.QRect(380, 710, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p29X.setFont(font)
        self.p29X.setObjectName("p29X")
        self.p25X = QtWidgets.QTextEdit(self.centralwidget)
        self.p25X.setGeometry(QtCore.QRect(380, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p25X.setFont(font)
        self.p25X.setObjectName("p25X")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(290, 710, 81, 41))
        self.label_31.setObjectName("label_31")
        self.p27Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p27Y.setGeometry(QtCore.QRect(460, 610, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p27Y.setFont(font)
        self.p27Y.setObjectName("p27Y")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(290, 610, 81, 41))
        self.label_32.setObjectName("label_32")
        self.p24Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p24Y.setGeometry(QtCore.QRect(460, 460, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p24Y.setFont(font)
        self.p24Y.setObjectName("p24Y")
        self.p23Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p23Y.setGeometry(QtCore.QRect(460, 410, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p23Y.setFont(font)
        self.p23Y.setObjectName("p23Y")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(290, 510, 81, 41))
        self.label_33.setObjectName("label_33")
        self.p22X = QtWidgets.QTextEdit(self.centralwidget)
        self.p22X.setGeometry(QtCore.QRect(380, 360, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p22X.setFont(font)
        self.p22X.setObjectName("p22X")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(290, 410, 81, 41))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(290, 360, 81, 41))
        self.label_35.setObjectName("label_35")
        self.p24X = QtWidgets.QTextEdit(self.centralwidget)
        self.p24X.setGeometry(QtCore.QRect(380, 460, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p24X.setFont(font)
        self.p24X.setObjectName("p24X")
        self.p21X = QtWidgets.QTextEdit(self.centralwidget)
        self.p21X.setGeometry(QtCore.QRect(380, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p21X.setFont(font)
        self.p21X.setObjectName("p21X")
        self.p26X = QtWidgets.QTextEdit(self.centralwidget)
        self.p26X.setGeometry(QtCore.QRect(380, 560, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p26X.setFont(font)
        self.p26X.setObjectName("p26X")
        self.p22Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p22Y.setGeometry(QtCore.QRect(460, 360, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p22Y.setFont(font)
        self.p22Y.setObjectName("p22Y")
        self.p25Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p25Y.setGeometry(QtCore.QRect(460, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p25Y.setFont(font)
        self.p25Y.setObjectName("p25Y")
        self.p29Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p29Y.setGeometry(QtCore.QRect(460, 710, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p29Y.setFont(font)
        self.p29Y.setObjectName("p29Y")
        self.p28Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p28Y.setGeometry(QtCore.QRect(460, 660, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p28Y.setFont(font)
        self.p28Y.setObjectName("p28Y")
        self.p27X = QtWidgets.QTextEdit(self.centralwidget)
        self.p27X.setGeometry(QtCore.QRect(380, 610, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p27X.setFont(font)
        self.p27X.setObjectName("p27X")
        self.l_input = QtWidgets.QTextEdit(self.centralwidget)
        self.l_input.setGeometry(QtCore.QRect(380, 760, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_input.setFont(font)
        self.l_input.setObjectName("l_input")
        self.p26Y = QtWidgets.QTextEdit(self.centralwidget)
        self.p26Y.setGeometry(QtCore.QRect(460, 560, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p26Y.setFont(font)
        self.p26Y.setObjectName("p26Y")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(110, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(190, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.ssout = QtWidgets.QLabel(self.centralwidget)
        self.ssout.setGeometry(QtCore.QRect(560, 280, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ssout.setFont(font)
        self.ssout.setObjectName("ssout")
        self.as1out = QtWidgets.QLabel(self.centralwidget)
        self.as1out.setGeometry(QtCore.QRect(560, 320, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.as1out.setFont(font)
        self.as1out.setObjectName("as1out")
        self.as2out = QtWidgets.QLabel(self.centralwidget)
        self.as2out.setGeometry(QtCore.QRect(560, 360, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.as2out.setFont(font)
        self.as2out.setObjectName("as2out")
        self.p1out = QtWidgets.QLabel(self.centralwidget)
        self.p1out.setGeometry(QtCore.QRect(560, 400, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p1out.setFont(font)
        self.p1out.setObjectName("p1out")
        self.p2out = QtWidgets.QLabel(self.centralwidget)
        self.p2out.setGeometry(QtCore.QRect(560, 440, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p2out.setFont(font)
        self.p2out.setObjectName("p2out")
        self.p3out = QtWidgets.QLabel(self.centralwidget)
        self.p3out.setGeometry(QtCore.QRect(560, 480, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p3out.setFont(font)
        self.p3out.setObjectName("p3out")
        self.p4out = QtWidgets.QLabel(self.centralwidget)
        self.p4out.setGeometry(QtCore.QRect(560, 520, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p4out.setFont(font)
        self.p4out.setObjectName("p4out")
        self.p5out = QtWidgets.QLabel(self.centralwidget)
        self.p5out.setGeometry(QtCore.QRect(560, 560, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p5out.setFont(font)
        self.p5out.setObjectName("p5out")
        self.p9out = QtWidgets.QLabel(self.centralwidget)
        self.p9out.setGeometry(QtCore.QRect(560, 720, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p9out.setFont(font)
        self.p9out.setObjectName("p9out")
        self.p10out = QtWidgets.QLabel(self.centralwidget)
        self.p10out.setGeometry(QtCore.QRect(560, 760, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p10out.setFont(font)
        self.p10out.setObjectName("p10out")
        
        self.instructions = QtWidgets.QLabel(self.centralwidget)
        self.instructions.setGeometry(QtCore.QRect(560, 260, 721, 561))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instructions.setFont(font)
        self.instructions.setObjectName("instructions")
        
        self.p8out = QtWidgets.QLabel(self.centralwidget)
        self.p8out.setGeometry(QtCore.QRect(560, 680, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p8out.setFont(font)
        self.p8out.setObjectName("p8out")
        self.p7out = QtWidgets.QLabel(self.centralwidget)
        self.p7out.setGeometry(QtCore.QRect(560, 640, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p7out.setFont(font)
        self.p7out.setObjectName("p7out")
        self.p6out = QtWidgets.QLabel(self.centralwidget)
        self.p6out.setGeometry(QtCore.QRect(560, 600, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p6out.setFont(font)
        self.p6out.setObjectName("p6out")
        self.v_number = QtWidgets.QLabel(self.centralwidget)
        self.v_number.setGeometry(QtCore.QRect(560, 240, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.v_number.setFont(font)
        self.v_number.setObjectName("v_number")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 20, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 200, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(290, 60, 81, 41))
        self.label_29.setObjectName("label_29")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(850, 50, 431, 191))
        self.listWidget.setObjectName("listWidget")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(850, 10, 431, 41))
        self.label_36.setObjectName("label_36")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1296, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("BEDROOM STUDIO", "BEDROOM STUDIO"))
        self.p2X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p2Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p4X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p4Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p3X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p3Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p8Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p7X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p7Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p6X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p6Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p5X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p8X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p5Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p9X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p10Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p10X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p9Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">X</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Y</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 1</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 2</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 3</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 4</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 5</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 9</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 6</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 7</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 8</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 10</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 16</span></p></body></html>"))
        self.p13Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p14X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p15X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 18</span></p></body></html>"))
        self.p12X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 13</span></p></body></html>"))
        self.p17Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 14</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 11</span></p></body></html>"))
        self.p16Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p18X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p19X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 12</span></p></body></html>"))
        self.p16X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Y</span></p></body></html>"))
        self.p18Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p15Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p11Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p20X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 20</span></p></body></html>"))
        self.p13X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">X</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 17</span></p></body></html>"))
        self.p12Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p17X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p19Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 19</span></p></body></html>"))
        self.p14Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p20Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 15</span></p></body></html>"))
        self.p11X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 21</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 24</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">l (база)</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 26</span></p></body></html>"))
        self.p28X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p23X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 28</span></p></body></html>"))
        self.p21Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p29X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p25X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 29</span></p></body></html>"))
        self.p27Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 27</span></p></body></html>"))
        self.p24Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p23Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 25</span></p></body></html>"))
        self.p22X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 23</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">точка 22</span></p></body></html>"))
        self.p24X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p21X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p26X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p22Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p25Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p29Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p28Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p27X.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.l_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.p26Y.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">0.0</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">0.0</span></p></body></html>"))
        self.ssout.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.as1out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.as2out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p1out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p2out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p3out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p4out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p5out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p9out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p10out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p8out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p7out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.p6out.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.v_number.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\"></span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Инструкция"))
        self.pushButton_2.setText(_translate("MainWindow", "Альтернативный вариант"))
        self.pushButton_3.setText(_translate("MainWindow", "Расчет"))
        self.pushButton_4.setText(_translate("MainWindow", "Сброс"))       
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Предыдущие варианты</span></p></body></html>"))

        self.instruction()

        self.pushButton.clicked.connect(self.instruction)        
        self.pushButton_2.clicked.connect(self.alternative)        
        self.pushButton_3.clicked.connect(self.count)
        self.pushButton_4.clicked.connect(self.reset)
        
        self.listWidget.insertItem(1, 'testing')
        self.listWidget.itemDoubleClicked.connect(self.setuptest)
    
    def instruction(self):
        self.reset()
        self.instructions.setText(text_of_instructions)
    
    def setuptest(self, item):
        self.reset()
        points = [{'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 1.5, 'y': 4.5}, {'x': 1.5, 'y': 1.0}, {'x': 2.0, 'y': 1.0}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]
        x_dots = (self.poles())[0]
        y_dots = (self.poles())[1]
        for i in range(len(points)):
            x_dots[i].insertPlainText(str(points[i]['x']))
            y_dots[i].insertPlainText(str(points[i]['y']))
        print(item.text())

    def poles(self):
        x_dots = (self.p2X, self.p3X, self.p4X, self.p5X, self.p6X, self.p7X, self.p8X, self.p9X, self.p10X, 
                  self.p11X, self.p12X, self.p13X, self.p14X, self.p15X, self.p16X, self.p17X, self.p18X,
                  self.p19X, self.p20X, self.p21X, self.p22X, self.p23X, self.p24X, self.p25X, self.p26X,
                  self.p27X, self.p28X, self.p29X)
        y_dots = (self.p2Y, self.p3Y, self.p4Y, self.p5Y, self.p6Y, self.p7Y, self.p8Y, self.p9Y, self.p10Y, 
                  self.p11Y, self.p12Y, self.p13Y, self.p14Y, self.p15Y, self.p16Y, self.p17Y, self.p18Y,
                  self.p19Y, self.p20Y, self.p21Y, self.p22Y, self.p23Y, self.p24Y, self.p25Y, self.p26Y,
                  self.p27Y, self.p28Y, self.p29Y)
        cort = (x_dots, y_dots)
        return cort
        
    def reset(self):
        global grand_variants
        global grand_points
        grand_variants.clear()
        grand_points.clear()
        poles = self.poles()
        for pole in poles[0]:
            pole.clear()
        for pole in poles[1]:
            pole.clear()
        self.l_input.clear()
        self.v_number.clear()
        self.ssout.clear()
        self.as1out.clear()
        self.as2out.clear()
        self.instructions.clear()
        for pos in self.allpans():
            pos.clear() 
        try:
            self.svgWidget.close()
        except AttributeError:
            None
    
    def alternative(self):

        global grand_variants
        global grand_points
        grand_variants.append(grand_variants[0])
        grand_variants.pop(0)
        grafic(grand_points, grand_variants)
        self.instructions.clear()
        self.v_number.setText(f'Вариантов: {len(grand_variants)}')
        self.ssout.setText(f"Координаты точки прослушивания, м: x = {round(grand_variants[0][3]['x'], 2)}, y = {round(grand_variants[0][3]['y'], 2)}")
        self.as1out.setText(f"Координаты первой АС, м: x = {round(grand_variants[0][0]['x'], 2)}, y = {round(grand_variants[0][0]['y'], 2)}")
        self.as2out.setText(f"Координаты второй АС, м: x = {round(grand_variants[0][1]['x'], 2)}, y = {round(grand_variants[0][1]['y'], 2)}")
        try:
            for pos in self.allpans():
                number = self.allpans().index(pos) + 5
                pos.setText(self.formpanel(number))
        except IndexError:
            None
        self.svgWidget = QtSvg.QSvgWidget('pic_location.svg')
        self.svgWidget.setWindowTitle(QtCore.QCoreApplication.translate("schematic", "schematic"))
        self.svgWidget.setGeometry(1400,50,500,500)
        self.svgWidget.show()

    def formpanel(self, number):
        #global grand_variants
        dict_number = number
        if grand_variants[0][dict_number]['depth'] == 0:
            membrane = 'мембраны нет'
        else:
            membrane = 'мембрана есть'
        depth = grand_variants[0][dict_number]['depth']
        if depth == 0:
            depth = 10
        form = f"Панель {number - 4}: координаты, м: x = {round(grand_variants[0][dict_number]['x'], 2)}, y = {round(grand_variants[0][dict_number]['y'], 2)}; d = {depth} см; {membrane}"
        return form
    
    def allpans(self):
        panslist = [self.p1out, self.p2out, self.p3out, self.p4out, self.p5out,
                    self.p6out, self.p7out, self.p8out, self.p9out, self.p10out]
        return panslist
    
    def count(self):
        global grand_variants
        global grand_points
        points = [{'x':0.0, 'y':0.0}]
        x_dots = (self.poles())[0]
        y_dots = (self.poles())[1]
        for i in range(28):
            try:
                a = float(x_dots[i].toPlainText())
            except ValueError:
                a = 0
            try:
                b = float(y_dots[i].toPlainText())
            except ValueError:
                b = 0
            if a == b == 0:
                None
            else:
                points.append({'x':a, 'y':b})
        try:
            grand_l = float(self.l_input.toPlainText())
        except ValueError:
            grand_l = 0
        grand_variants = engine(points, grand_l)
        grand_points = points
        self.alternative()            

class Demo(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet('.QWidget {background-image: url(wallpaper.jpg);}')
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Demo()
    w.show()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())

