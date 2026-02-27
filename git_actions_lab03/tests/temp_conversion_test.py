
from src.temp_coversion import celsius_to_fahrenheit,fahrenheit_to_celsius,kelvin_to_celsius,celsius_to_kelvin
import pytest 




def test_celsius_to_fahrenheit_conversion():
    assert celsius_to_fahrenheit(15) == 59.00
    assert celsius_to_fahrenheit(0) == 32.00
    assert celsius_to_fahrenheit(-16.50) == 2.30

def test_celsius_to_fahrenheit_type_error():
    with pytest.raises(TypeError, match="Input must be a number"):
        celsius_to_fahrenheit("temprature")

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(60) == 15.56
    assert fahrenheit_to_celsius(50) == 10.00
    assert fahrenheit_to_celsius(6) == -14.44
    assert fahrenheit_to_celsius(70) == 21.11
    assert fahrenheit_to_celsius(123) == 50.56

def test_fahrenheit_to_celsius_type_error():
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius("temprature")

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(60) == -213.15
    assert kelvin_to_celsius(50) == -223.15
    assert kelvin_to_celsius(6) == -267.15
    assert kelvin_to_celsius(70) == -203.15
    assert kelvin_to_celsius(123) == -150.15

def test_kelvin_to_celsius_type_error():
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius("temprature")

def test_kelvin_to_celsius_negative_number_error():
    with pytest.raises(ValueError,match="Kelvin cannot be negative"):
        kelvin_to_celsius(-111)

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(60) == 333.15
    assert celsius_to_kelvin(50) == 323.15
    assert celsius_to_kelvin(6) == 279.15
    assert celsius_to_kelvin(70) == 343.15
    assert celsius_to_kelvin(123) == 396.15
    assert celsius_to_kelvin(-111) == 162.15

def test_celsius_to_kelvin_type_error():
    with pytest.raises(TypeError, match="Input must be a number"):
        celsius_to_kelvin("temprature")

def test_kelvin_to_celsius_negative_number_error():
    with pytest.raises(ValueError,match="Temperature below absolute zero"):
        celsius_to_kelvin(-300)
