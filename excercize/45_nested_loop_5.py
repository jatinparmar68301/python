'''
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
'''
for row in range(1,6):
    for space in range(1,row):
        print(' ',end=' ')
    for astrik in range(1,6-row+1):
        print(' * ',end=' ')
    print('') #new line
for row in range(5,0,-1):
    for space in range(1,row):
        print(' ',end=' ')
    for astrik in range(1,6-row+1):
        print(' * ',end=' ')
    print('') #new line