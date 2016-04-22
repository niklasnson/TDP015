def subsets(s):
    tmp = []
    b = []
    for pos in range(0, 2**len(s)):
        tmp.append(bin(pos)[2:].zfill(len(s)))

    for p in tmp:
        builder = set()
        for index, item in enumerate(p, start=0):
            if item == '1':
                builder.add(s[index])
        b.append(builder)
    return b

print(len(subsets([1,2,3,4,5,6,7,8,9,10])) == 2**10)
print(len(subsets([1,'apa',3])) == 2**3)
print(len(subsets([1,2,3])) == 2**3)
