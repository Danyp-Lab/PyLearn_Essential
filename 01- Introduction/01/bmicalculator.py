Weight = float(input("please enter your weight(KG)"))
Height = float(input("please enter your height(Meters)"))

BMI = Weight / Height**2

if BMI < 18.5:
    print("under weight")
elif BMI <= 24.9:
    print("Normal Weight")
elif BMI <= 29.9:
    print("Over Weight")
elif BMI <= 34.9:
    print("Obesity")
elif BMI <= 39.9:
    print("Extreme Obesity")
elif BMI > 40:
    print("Input Wrong Or Its not In calculation Table Range")
