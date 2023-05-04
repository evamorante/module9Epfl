number = input("Type a number : ")
result = int(number) + 1
print("The result is " + str(result))

number = input("Type a number : ")
try:
    result = int(number) + 1
except:
    print("it's not a number, sorry !")
    quit()
print("The result is " + str(result))