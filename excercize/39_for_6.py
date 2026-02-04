# write a program to convert all negative values into positive values in the same list
numeric_list = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]
for i in range(len(numeric_list)):
    if numeric_list[i] < 0:
        numeric_list[i] = -numeric_list[i]
print("List with all positive values:", numeric_list)
