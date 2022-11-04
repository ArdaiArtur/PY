from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)


#python -m venv env
#env/Scripts/activate
#pip freeze
#pip install python-dateutil
#pip freeze
#deactivate
#pip install <name of package> --upgrade
#
#