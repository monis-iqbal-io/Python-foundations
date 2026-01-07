x = float(input("Enter any number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x > y and x > z:
    print(f"{x} is greater than {y} and {z}")

elif y > x and y > z:
    print(f"{y} is greater than {x} and {z}")

elif z > x and z > y:
    print(f"{z} is greater than {x} and {y}")

else:
    if x == y and x > z:
        print(f"{x} = {y} is greater than {z}")

    elif x == z and x > y:
        print(f"{x} = {z} is greater than {y}")

    elif y == z and y > x:
        print(f"{y} = {z} is greater than {x}")

    else:
        print("All are equal")
