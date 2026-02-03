'''
*
* *
* * *
* * * *
* * * * *
'''
row = 1
while row<6: #outer loop
    astrik = 0
    while astrik<row: #inner loop
        print('*',end=' ') #end= ' ' next print function will print on same line
        astrik=astrik + 1
    print("") #print empty blank link
    row = row + 1