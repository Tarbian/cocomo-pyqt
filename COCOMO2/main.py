from PyQt6 import QtWidgets, uic, QtGui

app = QtWidgets.QApplication([])
ui = uic.loadUi("main.ui")
ui.setWindowIcon(QtGui.QIcon('main.ico'))
ui.setWindowTitle("COCOMO2")

def gett(id):
	return float(id.currentText()[-4:len(id.currentText())])

def post(SIZE):
	PREC = gett(ui.comboBox)
	FLEX = gett(ui.comboBox_2)
	RESL = gett(ui.comboBox_3)
	TEAM = gett(ui.comboBox_4)
	PMAT = gett(ui.comboBox_5)

	ACAP = gett(ui.comboBox_56)
	AEXP = gett(ui.comboBox_68)
	PCAP = gett(ui.comboBox_66)
	PCON = gett(ui.comboBox_72)
	PEXP = gett(ui.comboBox_59)
	LTEX = gett(ui.comboBox_67)
	RELY = gett(ui.comboBox_58)
	DATA = gett(ui.comboBox_70)
	CPLX = gett(ui.comboBox_55)
	RUSE = gett(ui.comboBox_57)
	DOCU = gett(ui.comboBox_69)
	TIME = gett(ui.comboBox_61)
	STOR = gett(ui.comboBox_65)
	PVOL = gett(ui.comboBox_62)
	TOOL = gett(ui.comboBox_64)
	SITE = gett(ui.comboBox_71)
	SCED = gett(ui.comboBox_63)
	A = 2.45
	B = 0.91
	E = B + 0.01 * (PREC + FLEX + RESL + TEAM + PMAT)
	EAF = ACAP*AEXP*PCAP*PCON*PEXP*LTEX*RELY*DATA*CPLX*RUSE*DOCU*TIME*STOR*PVOL*TOOL*SITE*SCED
	PM = EAF*A*(SIZE**E)

	C = 3.67 
	D = 0.28
	TM = SCED * C * (PM**(D + 0.2*(E - B)))

	ui.label_10.setText(str(TM))
	ui.label_4.setText(str(PM))

def early(SIZE):
	PREC = gett(ui.comboBox)
	FLEX = gett(ui.comboBox_2)
	RESL = gett(ui.comboBox_3)
	TEAM = gett(ui.comboBox_4)
	PMAT = gett(ui.comboBox_5)

	PERS = gett(ui.comboBox_40)
	PREX = gett(ui.comboBox_51)
	RCPX = gett(ui.comboBox_37)
	RUSE = gett(ui.comboBox_39)
	PDIF = gett(ui.comboBox_38)
	FCIL = gett(ui.comboBox_50)
	SCED= gett(ui.comboBox_43)

	A = 2.94
	B = 0.91
	E = B + 0.01 * (PREC + FLEX + RESL + TEAM + PMAT)
	EAF = PERS*PREX*RCPX*PDIF*FCIL*SCED*RUSE
	PM = EAF*A*(SIZE**E)
	C = 3.67 
	D = 0.28
	TM = SCED * C * (PM**(D + 0.2*(E - B)))

	ui.label_10.setText(str(TM))
	ui.label_4.setText(str(PM))

ui.calc.clicked.connect(lambda: post(ui.size.value()))
ui.calc_2.clicked.connect(lambda: early(ui.size.value()))

ui.show()
app.exec()