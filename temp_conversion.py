def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value

    if from_scale == 'C':
        if to_scale == 'F':
            return celsius_to_fahrenheit(value)
        elif to_scale == 'K':
            return celsius_to_kelvin(value)
    elif from_scale == 'F':
        if to_scale == 'C':
            return fahrenheit_to_celsius(value)
        elif to_scale == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_scale == 'K':
        if to_scale == 'C':
            return kelvin_to_celsius(value)
        elif to_scale == 'F':
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid temperature scales.")

def main():
    print("Temperature Conversion Program")
    print("Supported scales: C (Celsius), F (Fahrenheit), K (Kelvin)")

    try:
        value = float(input("Enter the temperature value to convert: "))
        from_scale = input("Enter the current scale (C/F/K): ").strip().upper()
        to_scale = input("Enter the target scale (C/F/K): ").strip().upper()

        if from_scale not in ['C', 'F', 'K'] or to_scale not in ['C', 'F', 'K']:
            raise ValueError("Invalid scale input. Use C, F, or K.")

        converted_value = convert_temperature(value, from_scale, to_scale)
        print(f"{value} {from_scale} is equal to {converted_value:.2f} {to_scale}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
