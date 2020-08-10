import decimal
from decimal import Decimal
from random import uniform
import cmath


class Qualean:
    def __init__(self, val=None, qual=None):
        if val in [-1, 0, 1]:
            self.val = Decimal(val)
            self.uni_val = Decimal(uniform(-1, 1))
            with decimal.localcontext() as cxt:
                cxt.prec = 10
                self.qual = self.val * self.uni_val
        elif isinstance(qual, Decimal):
            self.uni_val = None
            self.val = 'Derieved'
            self.qual = qual
        else:
            raise ValueError('Input value must be -1, 0 or 1')

    def __repr__(self):

        return f'Qualean(({self.val}, \
{self.uni_val}) -> {format(self.qual,".10f")})'

    def __str__(self):

        return f'This is an object of type Qualean \
with internal val {format(self.qual,".10f")}'

    def __eq__(self, other):

        if isinstance(other, Qualean):
            return self.qual == other.qual
        else:
            raise TypeError("Quantum entanglement Failed...")

    def __add__(self, other):

        if isinstance(other, Qualean):
            return self.__class__(val=None, qual=self.qual+other.qual)

        # elif isinstance(other, (int, float, Decimal, complex)):
        #     return self.__class__(qual = self.qual+Decimal(other))

        else:
            raise TypeError("You can only add Qbits...")

    def __mul__(self, other):

        if isinstance(other, Qualean):
            return self.__class__(qual=self.qual*other.qual)

        elif isinstance(other, (int, float, Decimal, complex)):
            return self.__class__(qual=self.qual*Decimal(other))
        else:
            raise TypeError("You can only multiply Qbits...")

    def __sqrt__(self):
        return self.qual.sqrt() if self.qual > 0 else cmath.sqrt(self.qual)

    def __gt__(self, other):

        if isinstance(other, Qualean):
            return self.qual > other.qual
        # elif isinstance(other, (int, float, Decimal, complex)):
        #     return self.qual > other
        else:
            raise TypeError("Can't compare Qbits")

    def __ge__(self, other):

        if isinstance(other, Qualean):
            return self.qual >= other.qual
        # elif isinstance(other, (int, float, Decimal, complex)):
        #     return self.qual >= other
        else:
            raise TypeError("Can't compare Qbits")

    def __lt__(self, other):

        if isinstance(other, Qualean):
            return self.qual < other.qual
        # elif isinstance(other, (int, float, Decimal, complex)):
        #     return self.qual < other
        else:
            raise TypeError("Can't compare Qbits")

    def __le__(self, other):

        if isinstance(other, Qualean):
            return self.qual <= other.qual
        # elif isinstance(other, (int, float, Decimal, complex)):
        #     return self.qual <= other
        else:
            raise TypeError("Can't compare Qbits")

    def __bool__(self):
        return True if self.qual != 0 and self.qual != None else False

    def __invertsign__(self):
        return self.__class__(qual=self.qual * -1)

    def __float__(self):
        return float(self.qual)

    def __and__(self, other):
        if isinstance(other, Qualean):
            return True if self.qual and other.qual else False

    def __or__(self, other):
        if isinstance(other, Qualean):
            return True if self.qual or other.qual else False
