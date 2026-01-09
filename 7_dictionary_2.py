course = {'name':'spoken english','fees':9999.99,'days':120,'certified':True}
print(course)
print(course['name']) #spoken english
course['name'] = 'Communicative english' #update
course['trainer'] = 'Jiya Patel' #new key value pair add 
print(course)
print(course.get('location')) #error 
# course2 = course #bad way to copy dictionary
course2 = course.copy() 
course2.clear() #remove all key value pair 
print(course,course2)
print("Good bye")