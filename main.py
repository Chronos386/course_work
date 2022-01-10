from interface_classes import *
import sys

app = QApplication(sys.argv)
window = log_panel()
window.show()
sys.exit(app.exec_())
