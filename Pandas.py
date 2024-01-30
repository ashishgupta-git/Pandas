import pandas as pd

#TOPICS:
#Series(1 Dimensional data)
#Panel
#Dataframes


# y1 = {'name':['Ashish', 'Mukesh', 'shrey']}

# a = pd.Series(y1, index=False)
# print(a)
# print(type(a))


#Converting Series to dataframe:
# a = {'name':['Ashish', 'Mukesh', 'shrey'], 'age':[21,22,23]}
# b = pd.Series(a)
# print(b)
# print(type(b))


# #
# a = {'name':['Ashish', 'Mukesh', 'shrey'], 'age':[21,22,23]}
# b = pd.Series(a)
# print(b)
# print(type(b))


# DataFremes:
# a = [4,2,7,8,9,12]
# b = pd.DataFrame(a)
# print(b)
# print(type(b))


# a = {'name':['Ashish', 'Mukesh', 'shrey'], 'age':[21,22,23], 'mail':['a@gmail.com','m@gmail.com','s@gmail.com']}
# b = pd.DataFrame(a, index= ['a','b','c'])
# print(b)

#Printing Particular Column:
# a = {'name':['Ashish', 'Mukesh', 'shrey'], 'age':[21,22,23], 'mail':['a@gmail.com','m@gmail.com','s@gmail.com']}
# b = pd.DataFrame(a, columns= ['name'])
# print(b.name)


# a = {'Name':['Ashish', 'Mukesh', 'Shrey','Rohan','Satyam',], 'English':[70,60,80,65,70], 'Math':[80,70,70,55,80], 'Hindi':[65,70,70,90,75]}
# b = pd.DataFrame(a)
# # a['Percentage'] = (a['Total']/300)*100
# # a.loc[(a['English'])]
# print(b)



# x = {'Name':['Ashish','Rohan','Satyam'],
#      'Ranks': [1,3,2],
#      'City': ['Gorakhpur','Banglore','Delhi']
#      }


# y = pd.DataFrame(x, columns=["a"])

# print(type(y))
# print(y)



# x = pd.DataFrame({
#     'a': [1,2,3,4],
#     'b': [5,6,7,8],
# })
# print(x)

# x['c'] = x['a']+x['b']
# print(x)

x = pd.DataFrame({'A':[1,2,3,4],
                  'B':[5,6,7,8]
                  })
x.insert(2,'C',[9,10,11,12])

y = x.pop('B')

print(x)











