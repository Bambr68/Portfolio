
list=[]
for i in range(1,150):
    if i%15==0: 
        list.append('FizzBazz')
    elif i%3==0:
        list.append('Fizz')
    elif i%5==0:
        list.append('Bazz')
    else:
        list.append(i) 
print (list)