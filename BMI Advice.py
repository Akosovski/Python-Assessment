name = input("Please enter your name: ")
weight = int(input("Please enter your weight (in kg): "))
height = float(input("Please enter your height (in meters): "))
res1 = height * height
res2 = weight / res1
rounded = "%0.2f" %(res2)

print("Dear", name + ", your BMI is", str(rounded))

if res2 >= 22:
    print("Please exercise more!")

if res2 >= 18 and res2 < 22:
    print("Keep it up!")

if res2 < 18:
    print("Please eat more!")

