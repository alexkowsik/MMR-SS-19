from math import sin, cos, tan, exp, log, e, pi

class Function:
    def __call__(self, x):
        pass

    def __add__(self, g):
        if isinstance(g, Function):
            return AddFunction(self, g)
        else:
            return AddFunction(self, ConstFunction(g))

    def __sub__(self, g):
        if isinstance(g, Function):
            return SubFunction(self, g)
        else:
            return SubFunction(self, ConstFunction(g))

    def __mul__(self, g):
        if isinstance(g, Function):
            return MultFunction(self, g)
        else:
            return MultFunction(self, ConstFunction(g))

    def __truediv__(self, g):
        if isinstance(g, Function):
            return DivFunction(self, g)
        else:
            return DivFunction(self, ConstFunction(g))

    def __pow__(self, g):
        if isinstance(g, Function):
            return PowFunction(self, g)
        else:
            return PowFunction(self, ConstFunction(g))

    def __matmul__(self, g):
        if isinstance(g, Function):
            return CompFunction(self, g)
        else:
            return CompFunction(self, ConstFunction(g))


class AddFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) + self.g(x)


class SubFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) - self.g(x)


class MultFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) * self.g(x)


class DivFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x) / self.g(x)


class PowFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(x)**self.g(x)

class CompFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, x):
        return self.f(self.g(x))


class Identity(Function):
    def __call__(self, x):
        return x


class ConstFunction(Function):
    def __init__(self, c):
        self.c = c

    def __call__(self, x):
        return self.c


class Sin(Function):
    def __call__(self, x):
        return sin(x)


class Cos(Function):
    def __call__(self, x):
        return cos(x)


class Tan(Function):
    def __call__(self, x):
        return tan(x)


class Exp(Function):
    def __call__(self, x):
        return exp(x)


class Log(Function):
    def __init__(self,  base = e):
        self.base = base

    def __call__(self, x):
        return log(x, self.base)



krasserTangens = Sin() / Cos()
weirdF = krasserTangens + Exp()
threeF = ConstFunction(3.14) ** Identity()
lastF = threeF * 7

print(krasserTangens(42), tan(42))
print(weirdF(13.37), tan(13.37) + exp(13.37))
print(threeF(pi), 3.14**pi)
print(lastF(23), 3.14**23 * 7)

print("jup, scheint zu klappen")
