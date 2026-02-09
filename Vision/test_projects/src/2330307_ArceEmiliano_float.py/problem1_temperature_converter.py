# Problem 1: Temperature converter and range flag

try:
    temp_c = float(input("Enter temperature in Celsius: "))

    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: invalid input")
