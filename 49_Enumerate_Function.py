l1=["Mango","PineApple","Pomegranate","banana"]
# leave 2 nd item of list
# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Your items are {item}")
#     i +=1
# By ENumerated function
for index,item in enumerate(l1):
    if index%2 == 0:
        print(f"Your items are {item}")