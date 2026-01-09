course = {'name':'spoken english','fees':9999.99,'days':120,'certified':True}
print(course)
#display key value pair as object
print(course.items())
#disply keys 
print(course.keys())
print(course.values())

students = ['name','age','gender','weight']
#create dictionary using elements of list 
bhavdeep = dict.fromkeys(students) 
print(bhavdeep)
bhavdeep['name'] = 'bhavdeep'
bhavdeep['gender'] = True 
bhavdeep['age'] = 21
bhavdeep['weight'] = 75.11
print(bhavdeep)

#remove key value pair
bhavdeep.pop('weight')
print(bhavdeep)
#remove last key value pair 
bhavdeep.popitem()
print(bhavdeep)
bhavdeep['city'] = 'Bhavnagar' #it will add new key value pair 
bhavdeep.update({'pincode':364001})
print(bhavdeep)