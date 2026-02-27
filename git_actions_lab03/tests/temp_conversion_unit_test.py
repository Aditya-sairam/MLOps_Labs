import unittest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.temp_coversion import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
    celsius_to_kelvin
)


class TestTemperatureConversion(unittest.TestCase):
    
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
    
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=1)
    
    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(273.15), 0.0)
        self.assertEqual(kelvin_to_celsius(373.15), 100.0)
        self.assertEqual(kelvin_to_celsius(0), -273.15)
    
    def test_celsius_to_kelvin(self):
        self.assertEqual(celsius_to_kelvin(0), 273.15)
        self.assertEqual(celsius_to_kelvin(100), 373.15)
        self.assertEqual(celsius_to_kelvin(-273.15), 0.0)
    
    def test_celsius_to_fahrenheit_type_error(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("not a number")
    
    def test_kelvin_negative_error(self):
        with self.assertRaises(ValueError):
            kelvin_to_celsius(-10)
    
    def test_celsius_below_absolute_zero(self):
        with self.assertRaises(ValueError):
            celsius_to_kelvin(-300)


if __name__ == '__main__':
    unittest.main()