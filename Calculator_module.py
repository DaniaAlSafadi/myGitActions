"""
Calculator Module
A simple calculator with basic arithmetic operations
"""

import math
from typing import Union

class Calculator:
    """A simple calculator class with basic mathematical operations"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers"""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract second number from first number"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers"""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide first number by second number"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate base raised to the power of exponent"""
        result = base ** exponent
        self._add_to_history(f"{base}^{exponent} = {result}")
        return result
    
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate square root of a number"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self._add_to_history(f"√{number} = {result}")
        return result
    
    def percentage(self, number: Union[int, float], percent: Union[int, float]) -> Union[int, float]:
        """Calculate percentage of a number"""
        result = (number * percent) / 100
        self._add_to_history(f"{percent}% of {number} = {result}")
        return result
    
    def _add_to_history(self, operation: str) -> None:
        """Add operation to history"""
        self.history.append(operation)
        if len(self.history) > 10:  # Keep only last 10 operations
            self.history.pop(0)
    
    def get_history(self) -> list:
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history"""
        self.history.clear()


def main():
    """Main function to demonstrate calculator usage"""
    calc = Calculator()
    
    print("🧮 Calculator Demo")
    print("=" * 20)
    
    # Demonstrate basic operations
    print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtraction: 10 - 3 = {calc.subtract(10, 3)}")
    print(f"Multiplication: 4 × 6 = {calc.multiply(4, 6)}")
    print(f"Division: 15 ÷ 3 = {calc.divide(15, 3)}")
    print(f"Power: 2^3 = {calc.power(2, 3)}")
    print(f"Square Root: √16 = {calc.square_root(16)}")
    print(f"Percentage: 20% of 100 = {calc.percentage(100, 20)}")
    
    print("📊 Calculation History:")
    for i, operation in enumerate(calc.get_history(), 1):
        print(f"{i}. {operation}")


if __name__ == "__main__":
    main()
