import pandas as pd

x = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,5,5,5]
})

x['C'] = x["A"] + x["B"]
print(x)