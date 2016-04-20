def subsets(s):
    items = [[(a + 1,b + 1) for a in range(max(s))] for b in range(max(s))]
    items = flatten_array(items)
    items = remove_dublicates(items)
    for a in range(max(s)):
        items.append((a + 1,0))
    return items

def flatten_array(items):
    flat = []
    for p in items:
        for i in p:
            flat.append(i)
    return flat

def remove_dublicates(items):
    clean = []
    for i in items:
        if (i[1], i[0]) not in clean:
            clean.append(i)
    return clean

print(subsets((1,2)))
