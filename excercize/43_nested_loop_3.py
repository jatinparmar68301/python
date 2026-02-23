'''
1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1
'''
count = 5
for row in range(5,0,-1):
    for number in range(1,count+1):
        print(f"{number} ",end='')
    count = count - 1
    print("") 