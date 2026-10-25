class FractionSimulator:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def divide(self, second_fraction):
        result_numerator = self.num * second_fraction.den
        result_denominator = self.den * second_fraction.num
        return FractionSimulator(result_numerator, result_denominator)


Fraction_1 = FractionSimulator(2, 4)
Fraction_2 = FractionSimulator(4, 8)

Result_Div = Fraction_1.divide(Fraction_2)
print("devide", Result_Div.num / Result_Div.den)
