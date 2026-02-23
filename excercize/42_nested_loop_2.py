'''
1
0 1
0 1 0
1 0 1 0
1 0 1 0 1
'''


row = 5

for i in range(1, row + 1):
    # decide starting value for each row
    if i % 4 == 1 or i % 4 == 0:
        count = 1
    else:
        count = 0

    for j in range(i):
        print(count, end=" ")
        count = 1 - count   # switch between 0 and 1
    print()

