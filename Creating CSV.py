import pandas as pd 

x = pd.DataFrame({
    'Name':['Ashish', 'Rohan', 'Satyam'],
    'Age' : [25, 30, 40],
    'City': ['GKP','GKP', 'GolaBazar']  
    })

x.to_csv('Friends.csv')


