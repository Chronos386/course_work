from all_models import *

for i in session.query(Character).all():
    print(i)
