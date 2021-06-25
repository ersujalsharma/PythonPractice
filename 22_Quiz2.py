# Create a list and print only number greater than 10
list = ["Sujal","Sharma",10,50,40,50,60,354,0,321,81,41,51]

for item in list:
    if str(item).isnumeric() and item>10:
        print(item)
