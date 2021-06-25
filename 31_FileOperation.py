f = open("sujal.txt",'r')
content = f.read()
print(content)
f.close()
f = open("sujal.txt",'r')
for lin in f:
    print(lin)
