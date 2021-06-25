file = open("FIleHandling.txt")
readed = file.read()
print(readed)
# tell Function
address = file.tell()
print(address)
characters = file.seek(9)
print(characters)



