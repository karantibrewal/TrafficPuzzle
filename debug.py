from Vehicles import Car
a = set()
c = Car((1,2),(1,1), "A")
a.add(c)
print c in a
m = {}
m[c] = 1
print m[c]
l = [] 
l.append(c)
print c in l
b = list(l)
l.remove(c)

print c in l
print c in b