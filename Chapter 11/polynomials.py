import itertools
class Polynomial(object):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        return 'Polynomial({})'.format(self.coefficients)

    def __str__(self):
        terms = []
        for pow, coef in enumerate(self.coefficients):
            terms.append("{}*x^{}".format(coef, pow))
        return ' + '.join(terms)

    def __call__(self, x):
        res = 0
        for pow, coef in enumerate(self.coefficients):
            res += coef * x**pow
        return res

    def __add__(self, other):
        coefficients_pairs = \
            itertools.zip_longest(self.coefficients,
                                  other.coefficients,
                                  fillvalue = 0)
        new_coefficients = [a + b for a,b in coefficients_pairs]
        return Polynomial(new_coefficients)

p1 = Polynomial([0, 2, 1])
p2 = Polynomial([10, 1])

print(p1)
print(p2)
print(p1(1), p2(1))
print(p1(2), p2(2))
print(p1 + p2)
