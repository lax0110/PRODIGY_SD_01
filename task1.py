def cel_to_fah(celsius):
    return (celsius * 9/5) + 32

def cel_to_kel(celsius):
    return celsius + 273.15

def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fah_to_kel(fahrenheit):
    return fah_to_cel(fahrenheit) + 273.15

def kel_to_cel(kelvin):
    return kelvin - 273.15

def kel_to_fah(kelvin):
    return cel_to_fah(kel_to_cel(kelvin))

def convert(value, unit):
    celsius = fahrenheit = kelvin = None  # Initialize variables to avoid UnboundLocalError

    if unit.lower() == 'c':
        celsius = value
        fahrenheit = cel_to_fah(celsius)
        kelvin = cel_to_kel(celsius)
    elif unit.lower() == 'f':
        fahrenheit = value
        celsius = fah_to_cel(fahrenheit)
        kelvin = fah_to_kel(fahrenheit)
    elif unit.lower() == 'k':
        kelvin = value
        celsius = kel_to_cel(kelvin)
        fahrenheit = kel_to_fah(kelvin)
    else:
        raise ValueError("Unknown temperature unit. Please use 'C', 'F', or 'K'.")

    return celsius, fahrenheit, kelvin

def main():
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of the temperature (C, F, K): ").strip()

        celsius, fahrenheit, kelvin = convert(value, unit)

        print(f"\nConverted temperatures:")
        print(f"Celsius: {celsius:.2f} °C")
        print(f"Fahrenheit: {fahrenheit:.2f} °F")
        print(f"Kelvin: {kelvin:.2f} K")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
