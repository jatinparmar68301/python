set1 = {50,100,200,500}
set2 = {150,100,200,1500}

print(set1,set2) 
union = set1.union(set2) 
print(union)

intersection = set1.intersection(set2)
print(intersection)

#difference 
difference = set1.difference(set2)
print(difference)