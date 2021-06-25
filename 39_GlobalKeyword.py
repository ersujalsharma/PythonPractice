a = 10;
print(a)
def func():
    global a
    a = 45
    print(a)
func()
print(a)