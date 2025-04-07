import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shivam/code-masala/SeDriCa-BatMobile-v2/install/batmobile_perception'
