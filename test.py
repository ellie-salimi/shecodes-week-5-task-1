isbn_10 ='8889997776'
sum=0
for multiply_counter, num in enumerate(isbn_10,-10):
    num = int(num)
    sum += (num*(-multiply_counter))
    print (sum)