import conf


try:
    conf.ConfProcessor().order(conf.ConfAuto(""))
except AttributeError:
    print("The object has no  attribute.")
 