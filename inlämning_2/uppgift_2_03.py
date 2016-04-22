def subsets(s):
    t = []
    spinner = []
    for el in s:
        tmp = set([el])
        if not tmp in t:
            t.append(tmp)
            spinner.append(el)
        for le in spinner:
            print(le)
            pmt = set([el,le])
            if (le, el) not in t:
                print((le,el))
                if (el,le) not in t:
                    print((el,le))
                    t.append(pmt)
    return sorted(t)
# (1,2) => [(0), (1), (2), (1,2)]
# (a,b) => [(0), (a), (b), (a,b)]
# (1,2,3) => [(0), (1), (2), (3), (1,2), (1,3), (2,3), (1,2,3) ]

print(subsets((1,2,5)))
