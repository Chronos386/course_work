'''
from interface_classes import *
import sys
from backup_db import *
'''
'''
app = QApplication(sys.argv)
window = log_panel()
window.show()
sys.exit(app.exec_())
'''
'''
# dump PostgreSQL
postgresqlResults = DumpPostgreSql("postgres")
print(postgresqlResults)
'''

from backup_db import *

DumpPostgreSql()
