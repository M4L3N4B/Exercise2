class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        # Convert proper string argument to integers
        if isinstance(numerator, str):
            self.numerator, self.denominator = self.find_fraction_from_string(numerator)
    
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
