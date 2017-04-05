import In_out
import Control

def start ():
        calendar = In_out.Fillin()
	Control.menu(calendar)
	fl = open("db.txt", "w")
        In_out.pickle.dump(calendar, fl)
        fl.close()

start()
