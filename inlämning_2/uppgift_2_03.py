def subsets(s):
    t = []
    for el in s:
        tmp = set()
        tmp.add(el)
        t.append(tmp)
        for le in t:
            print(len(t))
    return t
# (1,2) => [(0), (1), (2), (1,2)]
# (a,b) => [(0), (a), (b), (a,b)]
# (1,2,3) => [(0), (1), (2), (3), (1,2), (1,3), (2,3), (1,2,3) ]

print(subsets((1,2,3)))
