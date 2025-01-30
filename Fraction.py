class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
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
