import pickle

def Fillin():
    """Function that loads data from a file"""
    data = [{}]
    f = open("db.txt", "r")
    data = pickle.load(f)
    f.close()
    return data

def check_date (y, m, d = None):
    """Check correct input data.
    tests:
    check_date("2017", "April", "21") -> True
    check_date("1016", "April", "21") -> False
    check_date("2015", "Apr", "21") -> False
    check_date("2014", "April", "32") -> False
    check_date("2134", "April") -> True
    check_date("1996", "Oct") -> False
    """
    months = ["january", "february", "march", "april", "may", "june", "july", "august",
              "september", "october", "november", "december"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y.isdigit() and int(y) > 1899 and int(y) < 3000:
        if m in months:
            if d == None or d.isdigit() and int(d) > 0 and int(d) <= days[months.index(m)]:
                return True
    return False


def Out_day(cal,y,m,d):
    """Function that introduces information about a particular day"""
    for i in cal :
       if (y == i['year']) and (m == i['month']) and (d == i['day']) :
           print "\n-------------------------------"
           print 'At ', y, m, d
           print  i['weather'],i['temperature'],' wimd',i['wind']
           print "--------------------------------"
       else:
            print "Day not found :( Didn\'t need people being told that the"

            
def Temp(cal,y,m):
    """Average temperature calculation function.
    tests:
    Temp("2017", "march") -> 18
    Temp("2016", "april") -> 0
    """
    t = d = 0
    for i in cal:
        if (i['month']== m) and (y == i['year']):
            t+=int(i['temperature'])
            d+=1
    if d!=0:
        return (t/d)
    else:
        return None


def Midl_temp(cal):
    """Output function average temperature.
    tests:
    Midl_temp("2017", "march") -> 18
    Midl_temp("2016", "april") -> 0
    """
    print "Enter year, month (example 2017 march ):"
    y = raw_input("Year = ")
    m = raw_input("Month = ")
    if check_date(y, m):
        if Temp(cal,y,m) != None:
            print 'Average temperature in ',m,y,' = ',Temp(cal,y,m)
        else:
            print "Data not available"
    else:
        print "Incorrect input date!"


def All_days(cal):
    """Display all days"""
    print "\n----------------------------------"
    for i in cal:
        print i['year'],  i['month'], i['day']
        print i['weather'],i['temperature'],' wimd',i['wind'],'(m/s)'
        print "----------------------------------"

