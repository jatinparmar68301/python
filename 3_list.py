lit=['The Easy Learn',32,12.4,False,"The Easy Learn"]
lit1=[1,2,3,4,5]

# Print complete list
print(lit)

# Print first element of the list
print(lit[0])

# Print elements starting from 1st till 3rd 
print(lit[0:3])

# Print elements starting from 2nd element
print(lit[1:])

# Print list two times
print(lit*2)

# Print concatenated lists
print(lit+lit1)

lit.append(0)
print(lit)

lit1.extend([1,2,3])
print(lit1)

lit.insert(2,"hi")
print(lit)

lit.remove("hi")
lit.remove(12.4)
print(lit)

print(lit1.pop(2))

lit1.clear()
print(lit1)

print(lit.index("The Easy Learn"))

print(lit.count("The Easy Learn"))

lit2=[3,5,8,1,0,3]
lit2.sort()
print(lit2)

lit2.reverse()
print(lit2)

lit3=lit2.copy()
print(lit3)