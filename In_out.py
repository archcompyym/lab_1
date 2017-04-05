import pickle

def Fillin():
    """Function that loads data from a file"""
    data = [{}]
    f = open("db.txt", "r")
    data = pickle.load(f)
    f.close()
    return data


def Out_day(cal,y,m,d):
    """Function that introduces information about a particular day"""
    print "Enter year, month, day (example 2017 march 23):"
    for i in cal :
       if (y == i['year']) and (m == i['month']) and (d == i['day']) :
            print 'At ', y, m, d
            print  i['weather'],i['temperature'],' wimd',i['wind']
       else:
            print "Day not found :( Didn\'t need people being told that the"

            
def Temp(cal,y,m):
    """Average temperature calculation function"""
    t=0
    d=0
    for i in cal:
        if (i['month']== m) and (y == i['year']):
            t+=int(i['temperature'])
            d+=1
    if d!=0:
        return (t/d)
    else:
        return None


def Midl_temp(cal):
    """Output function average temperature"""
    print "Enter year, month (example 2017 march ):"
    y = raw_input("Year = ")
    m = raw_input("Month = ")
    if Temp(cal,y,m) != None:
        print 'Average temperature in ',m,y,' = ',Temp(cal,y,m)
    else:
        print "Data not available"


def All_days(cal):
    """Display all days"""
    for i in cal:
        print i['year'],  i['month'], i['day']
        print i['weather'],i['temperature'],' wimd',i['wind'],'(m/s)'


#Fillin()
