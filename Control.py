import Editor
import In_out


def mode():
    """Mode"""
    print "\nSelect:"
    print " 1. Display all days"
    print " 2. Find day"
    print " 3. Add day"
    print " 4. Delete day"
    print " 5. Select day"
    print " 6. Average temperature per month"
    print "0. Exit"

    print "\nChoice: ",
    a = int(raw_input())

    if (a < 1) and (a > 6) and (a != 0):
        print "Input Error, try again!"
        a = mode()
    
    return a


def day():
    """Enter day"""
    y=raw_input("Year: ")
    m=raw_input("Month: ")
    d=raw_input("Day: ")
    return y,m,d


def selector(cal,a):
    "Select"
    y, m, d = day()
    if int(a)==2:
        In_out.Out_day(cal,y,m,d)
    if int(a)==3:
        Editor.add_el(cal,y,m,d)
    if int(a)==4:
        Editor.del_el(cal,y,m,d)
    if int(a)==5:
        Editor.del_el(cal,y,m,d)
        Editor.add_el(cal, y, m, d)


def menu(cal):
    """Main menu"""
    f = int(mode())
    while f >= 0 and f < 7:
        print "\n=========================="
        if f == 1:
            In_out.All_days(cal)
        if f == 6:
            print "=========================="
            In_out.Midl_temp(cal)
        else:
            selector(cal, f)
        f = int(mode())
    print "==========================\n"
    return 0
