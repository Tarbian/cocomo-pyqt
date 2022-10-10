from PyQt6 import QtWidgets, uic, QtGui

app = QtWidgets.QApplication([])
ui = uic.loadUi("main.ui")
icon = QtGui.QIcon()
ui.setWindowIcon(QtGui.QIcon('main.ico'))
ui.setWindowTitle("COCOMO")

def calculate(model, size):
	table =[[2.4, 1.05, 2.5, 0.38], [3.0, 1.12, 2.5, 0.35], [3.6, 1.20, 2.5, 0.32]]

	effort = round(table[model][0]*pow(size, table[model][1]), 3)
	time = round(table[model][2]*pow(effort, table[model][3]), 3)
	staff = round(effort/time, 3)
	productivity = round(size/effort, 3)
    
	ui.label_8.setText(str(effort))
	ui.label_6.setText(str(time))
	ui.label_4.setText(str(staff))
	ui.label_10.setText(str(productivity))

ui.calc.clicked.connect(lambda: calculate(ui.model1.currentIndex(), ui.size.value()))
ui.model1.currentIndexChanged.connect(lambda: calculate(ui.model1.currentIndex(), ui.size.value()))
ui.size.valueChanged.connect(lambda: calculate(ui.model1.currentIndex(), ui.size.value()))

ui.show()
app.exec()