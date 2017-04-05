import Editor
import In_out

''''mode'''
def mode():
    print "Select:"
    print "1.Display all days"
    print "2.Find day"
    print "3.Add day"
    print "4.Delete day"
    print "5.Select day"
    print "6.Average temperature per month"
    print "7.exit"
    a = raw_input()
    return a

'''enter day'''
def day():
    y=raw_input("Year: ")
    m=raw_input("Month: ")
    d=raw_input("Day: ")
    return y,m,d

'''selector'''
def selector(cal,a):
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

'''main menu'''
def menu(cal):
    f = int(mode())
    while int(f) >= 0 and int(f) < 7:
        print "11111111111111111"
        if f == 1:
            In_out.All_days(cal)
        if f > 1 and  f <=5:
            selector(cal, f)
        if f == 6:
            print "1111111111111111111"
            In_out.Midl_temp(cal)
        f = int(mode())
    return 0