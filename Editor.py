'''Find day'''
def find_el (cal,y,m,d):
    f=0
    for i in cal :
       if (y == i['year']) and (m == i['month']) and (d == i['day']):
            f = 1
            break
    if f == 1:
        return i
    else:
        return 0


''' Add element function'''
def add_el (cal,y,m,d):
    i=find_el (cal,y,m,d)
    if i == 0:
        w = raw_input('weather: ')
        t = raw_input('temperature: ')
        wind = raw_input('wimd(m/s): ')
        day={'year':y,'day':d,'month':m,'weather':w,'temperature':t,'wind':wind}
        cal.append(day)
    else:
        print "This day already have an input if you want to change select the editing mode"
    return cal

''' Delete element function'''
def del_el (cal,y,m,d):
    i=find_el (cal,y,m,d)
    if i == 0:
        print "This day is empty"
    else:
        cal.remove(i)
    return cal