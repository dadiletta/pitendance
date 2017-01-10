

class Btcheck(object):

    def __init__(self):
        try:
            from bluetooth import *
        except ImportError:
            raise ImportError('No Bluetooth Found. Install PyBluez')
            return


    def check_bluetooth(address):

        try:
            result = bluetooth.lookup_name(address, timeout=5)
            if result is not None:
                return True
            else:
                return False
        except Exception:
            print("\nERROR: " + str(Exception))
            return