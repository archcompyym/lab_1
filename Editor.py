
def find_el (cal,y,m,d):
    """Find day.
    tests:
    cal = {}
    find_el(cal, "2015", "march", "8") => None
    cal = [{year':'2017', 'day':'8', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}]
    find_el(cal, "2017", "march", "8")
    => {year':'2017', 'day':'8', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}
    """
    for i in cal :
       if (y == i['year']) and (m == i['month']) and (d == i['day']):
            return i
    return None


def add_el (cal,y,m,d):
    """Add element function.
    tests:
    cal = {}
    cal = add_el(cal, "2016", "march", "2")
       => [{year':'2017', 'day':'2', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}]
    add_el(cal, "2016", "march", "2")
       => [{year':'2017', 'day':'2', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}]
    """
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
    """Delete element function
    tests:
    cal =  [{year':'2017', 'day':'2', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}]
    cal = del_el(cal, "2017", "march", "2") => {}
    """
    i=find_el (cal,y,m,d)
    if i == None:
        print "This day is empty"
    else:
        cal.remove(i)
    return cal
