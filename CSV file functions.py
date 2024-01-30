import pandas as pd 


x = pd.DataFrame({
    'Name':['Ashish', 'Rohan', 'Satyam'],
    'Age' : [25, 30, 40],
    'City': ['GKP','GKP', 'GolaBazar']  
    })

x = pd.read_csv('Friends.csv')

x.loc[1, 'Age'] = 70
x.loc[1, 'Name'] = 'Vishal'

print(x)

# an h1 with inline style

