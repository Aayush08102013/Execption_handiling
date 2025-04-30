
try:
    num = int(input("Enter your number: "))
    print(num)
    # using ValueError
except ValueError as ex:
    print("Execption: ", ex)

# Multiple execptions:

try:
    num1 = int(input("Enter a numerical value: "))
    num2 = int(input("Enter a numerical value: "))
    result = num1/num2
    print(f"result is: {result:.3f}")
    print(f"result is: {result:.3f}")
    
except ZeroDivisionError:
    print("Division by 0 is not allowed!!")
except ValueError:
    print("Please enter a numerical value")
except NameError as ex:
    print("The execption is: ", ex)

except:
    print("Some error has occured!")

finally:
    print("I will execute no matter what")

# Create a execption while using the while loop:
valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        # entered a even number:
        while n % 2 == 0:
            print("Bye!")
            valid = True
    except ValueError:
        print("Invalid Input!!")
