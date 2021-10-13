# find fibonacchi series 

while True:
    num = int(input("Enter last number : "))
    def checkNumber(n):
        if num > 0:
            def fiboNumber(x):

                a = 0
                b = 1

                if n == 1:
                    print(a)
                else:
                    print(a)
                    print(b)
                    for i in range(2, n):
                        c = a + b
                        a = b
                        b = c 
                        print(c)
            fiboNumber(num)
        else:
            print("Negative Number!")

    checkNumber(num)
        
    findAgain = input("Find again (y / n): ")
    if findAgain != "y":
        print("End")
        break
