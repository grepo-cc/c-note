from  conf import *


try:
    PP = conf.ConfProcessor()
except AttributeError:
    print("The object has no  attribute.")
PP = order(conf.ConfAuto(""))