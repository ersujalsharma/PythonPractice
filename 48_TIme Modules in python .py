import time
initial = time.time()
k=0
while k<4000:
    print("Hello")
    k+=1
print( time.time() - initial)
initial2=time.time()
for i in range(1500):
    print("THis is sujal")
print(time.time()-initial2)