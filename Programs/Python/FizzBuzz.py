def FizzBuzz(x):
    for i in range(0,x):
        if x % 3 == 0:
            print ("Fizz")
        elif x % 10 == 0 or x % 10 == 5:
            print ("Buzz")
        else:
            print (x)

def main():
    FizzBuzz(10)


if __name__ == "__main__":
    main()

