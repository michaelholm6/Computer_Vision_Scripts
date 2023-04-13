from math import cos, sin, log


class Imaginary:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Imaginary(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Imaginary(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Imaginary(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        return Imaginary((self.real*other.real+self.imag*other.imag)/(other.real*other.real+other.imag*other.imag), (self.imag*other.real-self.real*other.imag)/(other.real*other.real+other.imag*other.imag))

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def exp(self):
        return Imaginary((2.71828183 ** self.real) * cos(self.imag), (2.71828183 ** self.real) * sin(self.imag))


def reorg_list(ind, log2n):
    n = 0
    for i in range(log2n):
        """This whole loop is reorganizing the order of the original list in order to build the recursion
        tree that would be created in the recursive algorithm from the bottom up"""
        n <<= 1
        n |= (ind & 1)
        ind >>= 1
    return Imaginary(n, 0)


def fft_iterative(input_list):
    n = len(input_list)
    input_reorg = [None] * n
    log2n = int(log(n, 2))
    for i in range(n):
        rev_ind = reorg_list(i, log2n)
        input_reorg[i] = (Imaginary(input_list[rev_ind.real], 0))
    for i in range(1, log2n+1):
        element_one = 1 << i
        element_two = element_one >> 1
        element_two = Imaginary(element_two, 0)
        omega = Imaginary(1, 0)
        omega_unity = (Imaginary(0, -1) * Imaginary(3.1515926, 0)/element_two).exp()
        for j in range(element_two.real):
            for k in range(j, n, element_one):
                t = omega * input_reorg[k + element_two.real]
                u = input_reorg[k]
                input_reorg[k] = u + t
                input_reorg[k+element_two.real] = u-t
            omega *= omega_unity
    return input_reorg


a = [0, .7071, 1, .7071, 0, -.7071, -1, -.7071]
answer = fft_iterative(a)

for i in answer:
    print(i)






