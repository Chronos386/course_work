from adm_db_panel import *


Ui_MainWindow.app = QtWidgets.QApplication(sys.argv)
Ui_MainWindow.MainWindow = QtWidgets.QMainWindow()
Ui_MainWindow.ui = Ui_MainWindow()
Ui_MainWindow.ui.setupUi(Ui_MainWindow.MainWindow)
Ui_MainWindow.MainWindow.show()
sys.exit(Ui_MainWindow.app.exec_())

