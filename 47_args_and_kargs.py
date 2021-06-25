list = []
def function_add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print("Enter numbers you want to add Enter c for REsult")
while(1):
    number = input()
    if(number == 'c'):
        break
    list.append(int(number))
summation = function_add(*list)
print(summation)
