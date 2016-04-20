def subsets(s):
    items = [[(a + 1,b + 1) for a in range(max(s))] for b in range(max(s))]
    items = flatten(items)
    for a in range(max(s)):
        items.append((a + 1,0))
    return items

def flatten(items):
    flat = []
    for p in items:
        for i in p:
            flat.append(i)
    return flat

print(subsets((1,2,3)))
