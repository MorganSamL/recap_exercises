num_read = 0
print("This program reads 4 numbers and will print the biggest one")
request = "Give me a number that you want to compare"
error = "That was not a valid number"
max = 0
cheese = int(input("Please enter the amount of numbers you would like to compare: "))
while num_read < cheese:
    try:
        read_line = input(request)
        num = float(read_line)
    except ValueError:
        print(error)
        continue
    if num_read == 0:
        max = num
    elif num > max:
        max = num
    num_read += 1

print("The biggest number read was ", max)

#change for max N numbers, where N is a number typed by the user
