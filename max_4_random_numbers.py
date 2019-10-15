import random
print("This program generates 4 random numbers than prints the biggest one")
a = random.random()*100
b = random.random()*100
c = random.random()*100
d = random.random()*100

print("I have generated these numbers: %.2f %.2f %.2f %.2f" % (a, b, c, d))
if a >= b and a >= c and a >= d:
    print("The biggest number is %.2f" % a)
    if b>=c and b>=d:
        print("the second biggest number is: ", b)
    elif c>=b and c>=d:
        print("the second biggest number is: ", c)
    elif d>=b and d>=c:
        print("the second biggest number is: ", d)
elif b >= a and b >= c and b >= d:
    print("The biggest number is %.2f" % b)
    if a>=c and a>=d:
        print("the second biggest number is: ", a)
    elif c>=a and c>=d:
        print("the second biggest number is: ", c)
    elif d>=a and d>=c:
        print("the second biggest number is: ", d)
elif c >= a and c >= b and c >= d:
    print("The biggest number is %.2f" % c)
    if b>=a and b>=d:
        print("the second biggest number is: ", b)
    elif a>=b and a>=d:
        print("the second biggest number is: ", a)
    elif d>=b and d>=a:
        print("the second biggest number is: ", d)
else:
    print("The biggest number is %.2f" % d)
    if b>=c and b>=a:
        print("the second biggest number is: ", b)
    elif c>=b and c>=a:
        print("the second biggest number is: ", c)
    elif a>=b and a>=c:
        print("the second biggest number is: ", a)

# determine the second largest number
