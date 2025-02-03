class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            self.numerator, self.denominator = self.find_fraction_from_string(numerator)
        elif isinstance(numerator, float) or isinstance(denominator, float):
            self.numerator, self.denominator = 0, 1   
        else:
            self.numerator, self.denominator = numerator, denominator
        
        if self.denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        else:
            self.lowest_term()
    
    def find_fraction_from_string(self, fraction_string):
        fraction_string = fraction_string.strip()
        
        if fraction_string.count('/') != 1:
            return 0, 1   
        
        try:
            numerator, denominator = fraction_string.split('/')
            numerator, denominator = int(numerator), int(denominator)
            return numerator, denominator
        except ValueError:
            return 0, 1

    def lowest_term(self):
        gcd_value = self.gcd(abs(self.numerator), abs(self.denominator))
        
        if gcd_value != 0:
            self.numerator //= gcd_value
            self.denominator //= gcd_value
            
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    @staticmethod
    def gcd(a, b):
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
