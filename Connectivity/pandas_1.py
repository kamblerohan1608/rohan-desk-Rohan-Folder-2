import pandas as pd

# Pandas 

# data manipulation

# data frames (column name + data)

# data = [[1,2,3,4,5,6,7]]
# df = pd.DataFrame(data,columns=["Mon","Tue","Wed","Thurs","Fri","Sat","Sun"])
# print(df)
# df.to_csv("test2.csv")
ss = pd.read_csv("test1.csv")
print(ss)