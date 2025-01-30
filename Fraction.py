class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(a, b):
        if a == 0 and b ==0:
            return 0
        
        if a == 0 or b == 0:
            return 0

        while b != 0:
            a, b = b, a % b

        return abs(a)

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
