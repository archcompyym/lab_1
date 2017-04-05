
def find_el (cal,y,m,d):
    """Find day"""
    for i in cal :
       if (y == i['year']) and (m == i['month']) and (d == i['day']):
            return i
    return None


def add_el (cal,y,m,d):
    """Add element function"""
    i=find_el (cal,y,m,d)
    if i == None:
        w = raw_input('weather: ')
        t = raw_input('temperature: ')
        wind = raw_input('wimd(m/s): ')
        day={'year':y, 'day':d, 'month':m, 'weather':w, 'temperature':t, 'wind':wind}
        cal.append(day)
    else:
        print "This day already have an input if you want to change select the editing mode"
    return cal


def del_el (cal,y,m,d):
    """Delete element function"""
    i=find_el (cal,y,m,d)
    if i == 0:
        print "This day is empty"
    else:
        cal.remove(i)
    return cal
