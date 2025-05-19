import pandas as pd

data={
  'name':['rw','re','rr'],
  'gender':['female','male','female'],
  'age':[12,13,14]
}
df=pd.DataFrame(data)

print("student data", data)

average_age = df.groupby('gender')['age'].mean()

print('average age of each student', average_age)