from math import sin, cos, tan, exp, log, e, pi
import aufgabe4_2


# TODO: Potenzieren von Funktionen, Rechnen mit Konstanten k ohne ConstFunction(k)

# Kommentiere das alles demnächst mal ordentlich


class DualNumber:
    def __init__(self, value, derivative):
        self.val = value
        self.der = derivative

    def __call__(self, x):
        return self.val(x), self.der(x)

    def __add__(self, n):
        return DualNumber(self.val + n.val, self.der + n.der)

    def __sub__(self, n):
        return DualNumber(self.val - n.val, self.der - n.der)

    def __mul__(self, n):
        return DualNumber(self.val * n.val, self.der * n.val + self.val * n.der)

    def __truediv__(self, n):
        return DualNumber(self.val / n.val, (self.der * n.val - n.der * self.val) / n.val ** 2)

    def __pow__(self, n):
        return DualNumber(self.val ** n, n * (self.val ** (n - 1)) * self.der)

    def __str__(self):
        return "(" + str(self.val) + ", " + str(self.der) + ")"





class DualFunction(aufgabe4_2.Function):
    def __add__(self, g):
        return AddFunction(self, g)

    def __sub__(self, g):
        return SubFunction(self, g)

    def __mul__(self, g):
        return MultFunction(self, g)

    def __truediv__(self, g):
        return DivFunction(self, g)

    def __pow__(self, g):
        return PowFunction(self, g)

    def __matmul__(self, g):
        return CompFunction(self, g)




class AddFunction(DualFunction):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) + self.g(x)


class SubFunction(DualFunction):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) - self.g(x)


class MultFunction(DualFunction):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) * self.g(x)


class DivFunction(DualFunction):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) / self.g(x)


class PowFunction(DualFunction):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x)**self.g(x)


class CompFunction(DualFunction):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(self.g(x))


class Identity(DualFunction):
    def __call__(self, x):
        if isinstance(x, DualNumber):
            return x
        else:
            return DualNumber(x, 1)


class ConstFunction(DualFunction):
    def __init__(self, c):
        self.c = c

    def __call__(self, x):
        return DualNumber(self.c, 0)


class Sin(DualFunction):
    def __call__(self, x):
        if isinstance(x, DualNumber):
            return DualNumber(sin(x.val), cos(x.val) * x.der)
        else:
            return DualNumber(sin(x), cos(x))


class Cos(DualFunction):
    def __call__(self, x):
        if isinstance(x, DualNumber):
            return DualNumber(cos(x.val), -sin(x.val) * x.der)
        else:
            return DualNumber(cos(x), -sin(x))


class Tan(DualFunction):
    def __call__(self, x):
        if isinstance(x, DualNumber):
            return DualNumber(tan(x.val), tan(x.val) ** 2 + 1)
        else:
            return DualNumber(tan(x), tan(x) ** 2 + 1)


class Exp(DualFunction):
    def __call__(self, x):
        if isinstance(x, DualNumber):
            return DualNumber(exp(x.val), exp(x.val) * x.der)
        else:
            return DualNumber(exp(x), exp(x))


class Log(DualFunction):
    def __init__(self,  base = e):
        self.base = base

    def __call__(self, x):
        if isinstance(x, DualNumber):
            return DualNumber(log(x.val, self.base), 1 / (x.val * log(self.base)) * x.der)
        else:
            return DualNumber(log(x, self.base), 1 / (x * log(self.base, e)))


if __name__ == '__main__':
    tangens = Sin() / Cos()
    print(tangens(3))
    print(tan(3), 1/cos(3)**2)

    smth = Sin() * Sin() + Cos()
    print(smth(2))
    print(sin(2)**2 + cos(2), 2*sin(2)*cos(2) - sin(2))

    smthElse = ConstFunction(3) * Log(10)
    print(smthElse(10))
    print(3 * log(10, 10), 3 / (10 * log(10, e)))

    smthDifferent = ConstFunction(pi) * Identity() * Identity() + Exp() @ Tan()
    print(smthDifferent(e))
    print(pi * e**2 + exp(tan(e)), pi * 2 * e + (exp(tan(e))) / cos(e)**2)

    impossible = Sin() @ (ConstFunction(1) / Identity())
    print(impossible(5))
    print(sin(1/5), cos(1/5) * -1/25)
    #print(impossible(0)) hehe