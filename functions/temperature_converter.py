"""
This code uses custom functions to convert a user-provided temperature between Celsius and Fahrenheit,
based on their chosen unit.
"""
def celsius_to_fahrenheit(temperature):
  return (9 / 5 * temperature + 32)

def fahrenheit_to_celsius(temperature):
  return ((temperature - 32) * 5 / 9)

print("Enter the temperature and units of the temperature: ")
temperature = float(input("temperature : "))
units = input("units(C/F): ").lower()

if units == "c":
  converted_result = round(celsius_to_fahrenheit(temperature), 2)
  print(f"The temperature in fahrenheit is {converted_result} F")
elif units == "f":
  converted_result = round(fahrenheit_to_celsius(temperature), 2)
  print(f"The temperature in celsius is {converted_result} C")