
def fizzbuzz(num):
    for i in range(1, num+1):
        imprime = ""
        if i%3==0:
            imprime += "Fizz"
        if i%5==0:
            imprime += "Buzz"
        if imprime:
            print(imprime)
        else:
            print(i)
