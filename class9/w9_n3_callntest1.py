listex = [ 27, 60, 50, 70, 55]
for k in range(len(listex)):
    m = k + 5
    r = listex[k] % m
    if ((m-r) < r):
        listex[k] = listex[k] + (m-r)
    else:
        listex[k] = listex[k] - r

print(listex)
