number = int(input("Please enter a number..:"))
increase = 2
if (number>2):
    def primeNumberFinder (number):
        increase = 2
        isPrime = True
        while (increase < number ):

            if (number%increase == 0):
                print("The number is not prime.")
                isPrime = False
                break
            elif(number == increase * increase):
                print("The number is not prime")
                isPrime = False
                break
            increase = increase + 1
        if isPrime:
            print("The number is prime.")
    print(primeNumberFinder(number))
elif (number==2):
    print("The number is prime.")
else:
    print("The number is not prime.")
