#   {"":"","":""} ------ Dictionary
#   [] ------ List
#   {"",""} ---- Array
t1 = ["Sujal","Sharma","Deepak","Sharma"]
print(t1[1])
#Pair of Key and Values
df = {}
print(df)
df = {"Sujal":"1","Deepak":"2","Ranjeet":"3"}
print(type(df))
print(df.keys())
print(df.values())
print(df.items())
print(df["Sujal"])
df["raja"] = "Babu"
print(df)
df1 = df
print(df1)
df1.pop("raja")
print(df1)
df1.update({"Raja":"Babu"})
print(df1)
print(df1.get("Sujal"))
print(df1.get("Raja"))
print(df)
df1 = df.copy()
print(df1)
print(df)
df1.pop("Raja")
print(df1)
print(df)



