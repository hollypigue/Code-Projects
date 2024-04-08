#temperature converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

print("Temperature Converter:")
print("1.) Celsius to Fahrenheit")
print("2.) Fahrenheit to Celsius")
print("3.) Celsius to Kelvin")
print("4.) Kelvin to Celsius")
print("5.) Fahrenheit to Kelvin")
print("6.) Kelvin to Fahrenheit")

choice = input("Enter a choice between 1-6: ")

if choice in ['1', '2', '3', '4', '5', '6']:
    temperature = float(input("Enter temperature to convert to selected choice: "))

    if choice == '1':
        converted_temp = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp}°F")
    elif choice == '2':
        converted_temp = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp}°C")
    elif choice == '3':
        converted_temp = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {converted_temp}K")
    elif choice == '4':
        converted_temp = kelvin_to_celsius(temperature)
        print(f"{temperature}K is equal to {converted_temp}°C")
    elif choice == '5':
        converted_temp = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is equal to {converted_temp}K")
    elif choice == '6':
        converted_temp = kelvin_to_fahrenheit(temperature)
        print(f"{temperature}K is equal to {converted_temp}°F")
else:
    print("Invalid choice, please enter a number from 1 to 6: ") 