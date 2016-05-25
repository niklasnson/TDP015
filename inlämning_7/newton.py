def newton(f, f_prime, x):
    i = 0
    while True:
        z = round(x - (f(x) / f_prime(x)), 10)
        x = round(x, 10)
        if x == z:
            #print(i)
            return x
        i += 1
        x = z

# 7.01
#print(newton(lambda x : x**2 - 2, lambda x : x*2, 1))
# testfil som bara används för att testa funktionen. eftersom jag använder mig
# av round och inte trunkar värdet int(str -> chop) så blir värdena här lite
# avrundade och inte helt som de är i exemplena.

# 7.02
newton(lambda x : x**3 - x + 1, lambda x : 3*x**2 - 1, -1)
# 5 itterationer är vad jag behöver för att komma fram till rätt svar.
# då jag använder -1 som ett lämpligt startvärde på funktionen.
# svar: -1.3247179572

# 7.03
newton(lambda x : x**5 - 5, lambda x : 5*x**4, 1)

# 7.04
newton(lambda x : x**2 - 3, lambda x: x*2, -1.5)
newton(lambda x : x**2 - 3, lambda x: x*2, 1.5)

# (3 - x^2) - (2x) derivata
# för att få en ledsen mun som inte får n dubbelrot på x axeln väljer jag en
# funktion som ger en graf som.
