import In_out
import Control

calendar = In_out.Fillin()
Control.menu(calendar)
fl = open("Db.txt", "w")
In_out.pickle.dump(calendar, fl)
fl.close()
