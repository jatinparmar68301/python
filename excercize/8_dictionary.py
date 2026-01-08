#create dictionary to store 20 different details about your ownself
student={"name":'Jatin Parmar',"age":20,"weight":45,"gender":True,"degree":'bca',"dob":"19-05-2006"}

#print dictionary

print(student)

#print name,age,gender,dob

print(student["name"])
print(student["age"])
print(student["gender"])
print(student["dob"])

#add key value pair pincode into dictionary 

student.update({'pincode':364001})
print(student)

#add key value pair to store your 5 favourite touriest destination

student.update({'favourite_touriest_destination':["paris","france","italy","london","dubai"]}) 

print(student)

#print all the favourite touriest destination

print(student['favourite_touriest_destination'])

#use update method to add new key value pair in dictionary

student.update({'hobby':'cricket'})

print(student)

#use update method to change exiting key value pair in dictionary

student.update({"weight":40})

print(student)

#use pop method to remove dob

student.pop('dob')

print(student)

#use popitem method to remove last item

student.popitem()

print(student)

#display all keys

print(student.keys())

#display all values

print(student.values())

#copy dictionary to another dictionary using copy function

student2=student.copy()

print(student2)

#clear newly create dictionary

student2.clear()

print(student,student2)

print("GOOD BYY :):)")