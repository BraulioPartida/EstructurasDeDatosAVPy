# recursividad lista invertida
def invList(l):
    if len(l) == 0:
        return []
    else:
        return [l[-1]] + invList(l[:-1])
