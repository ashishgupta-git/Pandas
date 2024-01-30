import pandas as pd

x = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
})

#Inserting data
x.insert(2, 'C', ['Apple','Ball','Cat'])

#For Deleting table
x.pop('C')
print(x)