from math import cos, sin


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


def FFT(input_values: list):
    n = Imaginary(len(input_values), 0)  # n must be a power of 2
    if n.real == 1:
        return input_values
    omega_first = (Imaginary(-2, 0) * Imaginary(3.14, 0) * Imaginary(0, 1) / n).exp()
    omega = Imaginary(1, 0)
    a0 = []
    a1 = []
    for i in range(len(input_values)):
        if i % 2 == 0:
            a0.append(input_values[i])
        elif i % 2 == 1:
            a1.append(input_values[i])
    y0 = FFT(a0)
    y1 = FFT(a1)
    output = [None] * n.real
    for i in range(int((n / Imaginary(2, 0)).real)):
        output[i] = y0[i] + omega * y1[i]
        output[i + int((n / Imaginary(2, 0)).real)] = y0[i] - omega * y1[i]
        omega = omega * omega_first
    return output


if __name__ == "__main__":
    output_FFT = FFT([Imaginary(0, 0), Imaginary(.7071, 0), Imaginary(1, 0), Imaginary(.7071, 0), Imaginary(0, 0), Imaginary(-.7071, 0), Imaginary(-1, 0), Imaginary(-.7071, 0)])
    for number in output_FFT:
        print(number)
