student = {'name':'jatin parmar','age':21,'weight':51.25,'gender':True,'degree':None}
print(student)
print(student['name']) #jatin parmat
student['age'] = 20 #key value pair update
print(student['age']) # 20
del student['degree'] #remove key value pair
student['city'] = 'bhavnagar' #it will add new key value pair 
print(student)