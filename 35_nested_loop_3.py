'''
        1
      1 2  
    1 2 3  
  1 2 3 4  
1 2 3 4 5  
'''
count = 1
for row in range(5,0,-1): #4 3 2 1
  for space in range(1,row): #1 2 3 4 5
    print(' ',end=' ')
  for number in range(1,count+1): #2nd inner for loop
    print(f"{number} ",end='')
  count = count + 1
  print("") #new line 