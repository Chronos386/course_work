from interface_classes import *

app = QApplication(sys.argv)
window = log_panel()
window.show()
sys.exit(app.exec_())
