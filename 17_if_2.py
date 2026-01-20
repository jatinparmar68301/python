'''
    write a program to figure out shape of object (portrait, landscape, square) using given length and width
'''
length = int(input("Enter shape's length :"))
width = int(input("Enter shape's width :"))

if length==width:
    print("given shape is square")
if width>length:
    print("given shape is landscape")
if width<length:
    print("given shape is portrait")

print('good bye.')