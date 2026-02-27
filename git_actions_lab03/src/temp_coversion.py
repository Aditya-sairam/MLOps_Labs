def celsius_to_fahrenheit(celsius) -> float:
    if not isinstance(celsius,(int,float)):
        raise TypeError("Input must be a number")
    return round((celsius* 9/5)+32,2)

def fahrenheit_to_celsius(fahrenheit) -> float:
    if not isinstance(fahrenheit,(int,float)):
        raise TypeError("Input must be a number")
    return round((fahrenheit-32) * 5/9,2)
     
def kelvin_to_celsius(kelvin) -> float:
    if not isinstance(kelvin, (int, float)):
        raise TypeError("Input must be a number")
    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative")
    return round(kelvin - 273.15,2)

def celsius_to_kelvin(celsius) -> float:
    """Convert Celsius to Kelvin"""
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero")
    return round(celsius + 273.15,2)