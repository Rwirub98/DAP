import pandas as pd
data={"Name":["Ram","Subash","Raghul","Arun","Deepak"],"Age":[24,25,24,
26,25],"CGPA":[9.5,9.3,9.0,8.5,8.8]}
t=pd.DataFrame(data) ;
t.index+=1
print(t) 