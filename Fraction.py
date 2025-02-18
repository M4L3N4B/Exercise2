class Fraction(object):
    def __init__(self, numerator=0, denominator=1):
        # Defaults to 0, 1 for invalid inputs
        if isinstance(numerator, str):
            self._numerator, self._denominator = self._find_fraction_from_string(numerator)
        elif isinstance(numerator, float) or isinstance(denominator, float): # Floats are not supported
            self._numerator, self._denominator = 0, 1   
        else:
            self._numerator, self._denominator = numerator, denominator
        
        if self._denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        else:
            self._lowest_term() # In preparation for accessor methods, which should return values in lowest terms
    
    def _find_fraction_from_string(self, fraction_string):
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

    def _lowest_term(self):
        # Set numerator and denominator to their lowest terms
        gcd_value = self.gcd(abs(self._numerator), abs(self._denominator))
        
        if gcd_value != 0:
            self._numerator //= gcd_value
            self._denominator //= gcd_value
            
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1

    @staticmethod
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0

        while b != 0:
            a, b = b, a % b

        return abs(a)

    def get_numerator(self):
        return str(self._numerator)

    def get_denominator(self):
        return str(self._denominator)

    def get_fraction(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"
