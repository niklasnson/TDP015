def divide_by_seven(a, b):
    if a > 7:
        a = a%7
    if b > 7:
        b = a%7
    return a,b

def do_calc(a, b):
    a, b = divide_by_seven(a,b)
    c = a + b
    if c > 7:
        c = c%7
    return c

def calculate_the_year_item(a):
    dozens = a//12
    overplus = a%12
    fours = overplus//4
    a = dozens + overplus + fours
    return a

def calculate_the_month_item(a):
    if a == 1:
        return 0
    elif a == 2:
        return 3
    elif a == 3:
        return 3
    elif a == 4:
        return 6
    elif a == 5:
        return 1
    elif a == 6:
        return 4
    elif a == 7:
        return 6
    elif a == 8:
        return 2
    elif a == 9:
        return 5
    elif a == 10:
        return 0
    elif a == 11:
        return 3
    elif a == 12:
        return 5

def calculate_day_item(a, b):
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
        b = b - 1
    return b

def day_of_week(y, m, d):
    number_of_centuries = int(str(y)[:2])
    number_of_years_over = y % 100
    calc = 0
    calc = do_calc((3-(number_of_centuries%4))*2, calc)
    calc = do_calc(calculate_the_year_item(number_of_years_over), calc)
    calc = do_calc(calculate_the_month_item(m), calc)
    calc = do_calc(calculate_day_item(y,d), calc)
    data = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return data[calc]

print(day_of_week(1845, 5, 23))
