import math


class Fraction:
    def __init__(self, numerator, denominator):
        # Check for zero denominator
        if denominator == 0:
            raise ValueError("Denominator cannot be zero!")
        self.numerator = numerator
        self.denominator = denominator

    # Function in the Class---->Methods
    def add(self, other_fraction):
        "Adds two fractions and returns the result as a new Fraction object"
        numerator_after_sum = (
            self.numerator * other_fraction.denominator
            + other_fraction.numerator * self.denominator
        )
        denominator_after_sum = self.denominator * other_fraction.denominator
        return Fraction(numerator_after_sum, denominator_after_sum).simplify()

    def subtract(self, other_fraction):
        "Subtracts two fractions and returns the result as a new Fraction object"
        numerator_after_difference = (
            self.numerator * other_fraction.denominator
            - other_fraction.numerator * self.denominator
        )
        denominator_after_difference = self.denominator * other_fraction.denominator
        return Fraction(numerator_after_difference, denominator_after_difference).simplify()

    def multiply(self, other_fraction):
        "Multiplies two fractions and returns the result as a new Fraction object"
        numerator_after_product = self.numerator * other_fraction.numerator
        denominator_after_product = self.denominator * other_fraction.denominator
        return Fraction(numerator_after_product, denominator_after_product).simplify()

    def divide(self, other_fraction):
        "Divides two fractions and returns the result as a new Fraction object"
        # Check for zero division
        if other_fraction.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        numerator_after_quotient = self.numerator * other_fraction.denominator
        denominator_after_quotient = self.denominator * other_fraction.numerator
        return Fraction(numerator_after_quotient, denominator_after_quotient).simplify()

    def simplify(self):
        "Simplifies the fraction by finding the greatest common divisor and dividing both numerator and denominator"
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        return self

    def to_decimal(self):
        "Returns the decimal representation of the fraction"
        return self.numerator / self.denominator

    def __str__(self):
        "Returns a string representation of the fraction in numerator/denominator format"
        return f"{self.numerator}/{self.denominator}"


# Get user input and handle errors gracefully
while True:
    try:
        numerator1 = int(input("Enter the numerator of the first fraction: "))
        denominator1 = int(input("Enter the denominator of the first fraction (cannot be zero): "))

        if denominator1 == 0:
            raise ValueError("Denominator cannot be zero.")

        numerator2 = int(input("Enter the numerator of the second fraction: "))
        denominator2 = int(input("Enter the denominator of the second fraction (cannot be zero): "))

        if denominator2 == 0:
            raise ValueError("Denominator cannot be zero.")

        break  # Exit the loop if input is valid

    except ValueError:
        print(
            "Invalid input. Please enter integers for numerators and non-zero integers for denominators."
        )

# Create fraction objects and perform operations
fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

result_sum = fraction1.add(fraction2)
result_subtract = fraction1.subtract(fraction2)
result_multiply = fraction1.multiply(fraction2)
result_divide = fraction1.divide(fraction2)
result_decimal1 = fraction1.to_decimal()
result_decimal2 = fraction2.to_decimal()

# Print results in a user-friendly format
print("\n--- Results ---")
print(f"SUM: {result_sum}")
print(f"SUB: {result_subtract}")
print(f"MULT: {result_multiply}")
print(f"DIV: {result_divide}")
print(f"Decimal (fraction1): {result_decimal1:.2f}")
print(f"Decimal (fraction2): {result_decimal2:.2f}")
