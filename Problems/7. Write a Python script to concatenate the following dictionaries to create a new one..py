#7. Write a Python script to concatenate the following dictionaries to create a new one. Sample
#Dictionary : dic1 = 1 : 10, 2 : 20dic2 = 3 : 30, 4 : 40dic3 = 5 : 50, 6 : 60 Expected Result : 1 : 10, 2 : 20, 3
#: 30, 4 : 40, 5 : 50, 6 : 60
dict1={1:20,2:20}
dict2={3:30,4:40}
dict3={4:40,5:50}
dict4={5:50,6:60}
dict5={}

for d in (dict1,dict2,dict3,dict4):
    dict5.update(d)
print(dict5)