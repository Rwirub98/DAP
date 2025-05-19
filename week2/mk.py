#create pandas dataframe with column data prodict sales and region . filter the sales data where region "north"


import pandas as pd

data={
  'product':['A','B','C'],
  'sales':[100,39,200],
  'region':['north', 'south', 'west']
  
}

df=pd.DataFrame(data)

north_df=df[df['region']=='north']

print(north_df)