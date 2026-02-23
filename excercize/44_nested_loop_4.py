'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

count = 5
for row in range(5,0,-1):
    for number in range(5,5-row,-1):
        print(f"{number} ",end='')
    count = count - 1
    print("")
