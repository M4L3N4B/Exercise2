class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        # Defaults to 0, 1 for invalid inputs
        if isinstance(numerator, str):
            self.numerator, self.denominator = self.find_fraction_from_string(numerator)
        elif isinstance(numerator, float) or isinstance(denominator, float):   # Floats are not supported
            self.numerator, self.denominator = 0, 1   
        else:
            self.numerator, self.denominator = numerator, denominator
        
        if self.denominator == 0:
            self.numerator, self.denominator = 0, 1
    
    def find_fraction_from_string(self, fraction_string):
        # Returns 0, 1 for invalid strings
        fraction_string = fraction_string.strip()
        
        if fraction_string.count('/') != 1:
            return 0, 1   
        
        try:
            numerator, denominator = fraction_string.split('/')
            numerator, denominator = int(numerator), int(denominator)
            return numerator, denominator
        except ValueError:
            return 0, 1
    
    @classmethod
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        
        while b != 0:
            a, b = b, a%b

        return abs(a)

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
