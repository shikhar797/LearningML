import math
arr=[1,2,4,5]
#max ,min ,average,sum
sum=0,avergae=0,max=-1,min=100000

for i in arr:
    if i < min:
        min=i
    if i > max:
        max=i
    sum+=i
avergae=sum/len(arr)
print(math.sqrt(sum))             


import pandas as pd

data = {
    'Roll_No': [101, 102, 103],
    'Name': ['Rahul', 'Anita', 'Suresh'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


df.to_csv("students.csv", index=False)
df.to_excel("students.xlsx", index=False)
df.to_csv("students.txt", sep='\t', index=False)

df_csv = pd.read_csv("students.csv")
print("\nData from CSV File:")
print(df_csv)

# Read Excel
df_excel = pd.read_excel("students.xlsx")
print("\nData from Excel File:")
print(df_excel)

# Read Text File
df_txt = pd.read_csv("students.txt", sep='\t')
print("\nData from Text File:")
print(df_txt)
