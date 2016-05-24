# a = current, b = total
def divide_by_seven(current, total):
    total = total + current
    if total > 7:
        total = total%7
    return current, total

def century_item(current, total):
    current = current % 4
    current = 3 - current
    current = 2 * current
    return divide_by_seven(current, total)

def year_item(current, total):
    dozens = current // 12
    overplus = current%12
    fours = overplus // 4
    current = dozens + overplus + fours
    return divide_by_seven(current, total)

def month_item(current, total):
    if current  == 1:
        current = 0
    elif current == 2:
        current =  3
    elif current == 3:
        current =  3
    elif current == 4:
        current =  6
    elif current == 5:
        current =  1
    elif current == 6:
        current = 4
    elif current == 7:
        current = 6
    elif current == 8:
        current = 2
    elif current == 9:
        current = 5
    elif current == 10:
        current = 0
    elif current == 11:
        current = 3
    elif current == 12:
        current = 5
    return divide_by_seven(current, total)

def day_item(year, month, current, total):
    if month == 1 or month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if (current - 1) == 0:
                current = 7
    return divide_by_seven(current, total)

def day_of_the_week(y, m, d):
    current = 0
    total = 0
    current, total = century_item(int(str(y)[:2]), total)
    current, total = year_item(y % 100, total)
    current, total = month_item(m, total)
    current, total = day_item(y, m, d, total)
    data = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return(data[total])

#print(day_of_the_week(1845, 5, 23))
#print(day_of_the_week(1974, 9, 7))
#print(day_of_the_week(1977,10, 16))
#print(day_of_the_week(2016, 5, 23))
#print(day_of_the_week(2016, 5, 24))
