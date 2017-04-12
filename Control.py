import Editor
import In_out


def mode():
    """Mode"""
    print "\nSelect:"
    print " 1. Display all days"
    print " 2. Find day"
    print " 3. Add day"
    print " 4. Delete day"
    print " 5. Rewrite day"
    print " 6. Average temperature per month"
    print "0. Exit"

    print "\nChoice: ",
    a = raw_input()

    if (not a.isdigit()) or int(a) < 0 and int (a) > 6 :
        print "Input Error, try again!"
        a = mode()
    
    return a

def day ():
    """Enter day"""
    y=raw_input("Year: ")
    m=raw_input("Month: ")
    d=raw_input("Day: ")
    return y,m,d


def selector(cal,a):
    "Select"
    print "\nEnter year, month, day (example 2017 march 23):"
    y, m, d = day()
    if check_date(y, m, d):
        if int(a)==2:
            In_out.Out_day(cal,y,m,d)
        if int(a)==3:
            Editor.add_el(cal,y,m,d)
        if int(a)==4:
            Editor.del_el(cal,y,m,d)
        if int(a)==5:
            Editor.del_el(cal,y,m,d)
            Editor.add_el(cal, y, m, d)
    else:
         print "Incorrect input date!"   


def menu(cal):
    """Main menu"""
    f = int(mode())
    while f > 0 and f < 7:
        if f == 1:
            In_out.All_days(cal)
        elif f == 6:
            In_out.Midl_temp(cal)
        else:
            selector(cal, f)
        f = int(mode())
    return 0
