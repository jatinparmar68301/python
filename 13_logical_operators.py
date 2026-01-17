#example of logical operators 
j = int(input("Enter number for j :")) 
r = int(input("Enter number for r :")) 
p = int(input("Enter number for p :")) 

#     10 < 20    20 < 30
#True        True       True
result = j < r and r < p
print(f"{result} = {j} < {r} and {r} < {p}")

# check j is below r or r is above p 
result = j < r or r > p
print(f"{result} = {j} < {r} or {r} > {p}")


result = not (j < r) 
print(f"{result} = not ({j} < {r})") 