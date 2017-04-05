import pickle

'''Function that loads data from a file'''
def Fillin():
    data = [{}]
    f = open("Db.txt", "r");
    data = pickle.load(f)
    f.close()
    return data

'''Function that introduces information about a particular day'''
def Out_day(cal,y,m,d):
    print "Enter year, month, day (example 2017 march 23):"
    for i in cal :
       if (y == i['year']) and (m == i['month']) and (d == i['day']) :
            print 'At ', y, m, d
            print  i['weather'],i['temperature'],' wimd',i['wind']
       else:
            print "Day not found :("

'''Average temperature calculation function'''
def Temp(cal,y,m):
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

'''Output function average temperature'''
def Midl_temp(cal):
    print "Enter year, month (example 2017 march ):"
    y = raw_input("Year = ")
    m = raw_input("Month = ")
    if Temp(cal,y,m) != None:
        print 'Average temperature in ',m,y,' = ',Temp(cal,y,m)
    else:
        print "Data not available"


'''Display all days'''
def All_days(cal):
    for i in cal:
        print i['year'],  i['month'], i['day'],'\0'
        print i['weather'],i['temperature'],' wimd',i['wind'],'(m/s)','\0','\0'