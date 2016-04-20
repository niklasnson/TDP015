operations = []
operations.append(lambda x, y: not not x and y  and x and not y)
operations.append(lambda x, y: not(x and y) and not x and not y)
operations.append(lambda x, y: not x and y)
operations.append(lambda x, y: not x)
operations.append(lambda x, y: x and not y)
operations.append(lambda x, y: not y)
operations.append(lambda x, y: not(not(x and not(x and y)) and not(y and not(x and y))))
operations.append(lambda x, y: not(x and y))
operations.append(lambda x, y: x and y)
operations.append(lambda x, y: (not(x and not(x and y)) and not(y and not(x and y))))
operations.append(lambda x, y: y)
operations.append(lambda x, y: not(x and not y))
operations.append(lambda x, y: x)
operations.append(lambda x, y: not(not x and y))
operations.append(lambda x, y: not(not(x and y) and (not x and not y)))
operations.append(lambda x, y: not(not not x and y and x and not y))

#i = 0
#for item in operations:
#    print('%d:\t' %(i), end =" ")
#    print(item(True, True), end="\t")
#    print(item(True, False), end="\t")
#    print(item(False, True), end="\t")
#    print(item(False, False))
#    i += 1
