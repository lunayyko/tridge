#Implement the `_convert` method of the following class:

# Convert numbers from base 10 integers to base N strings and back again.
# Sample usage:
# >>> base20 = Transformer('0123456789abcdefghij')
# >>> base20.from_decimal(1234)
# '31e'
# >>> base20.to_decimal('31e')
# 1234

class Transformer(object):
    decimal_digits = '0123456789'
    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)
    
    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))
    
    def _convert(self, number, fromdigits, todigits):
        fromdigits_len, todigits_len = len(fromdigits), len(todigits)
        number = str(number)
        number_len = len(number)

        tmp_dec=0
        for idx, n in enumerate(number):
            tmp = fromdigits_len ** (number_len-idx-1) * fromdigits.index(n)
            tmp_dec += tmp
        
        result=''
        while tmp_dec > 0:
            tmp_dec, mod = divmod(tmp_dec, todigits_len)
            result += str(todigits[mod])
        return result[::-1]

#Test
base20 = Transformer('0123456789abcdefghij')
print(base20.from_decimal(1234))
print(base20.to_decimal('31e'))