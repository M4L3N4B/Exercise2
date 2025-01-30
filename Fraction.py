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
    
    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
