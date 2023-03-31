import math


def dft(input_values: list):
    n = len(input_values)
    output_real = [None] * n
    output_imag = [None] * n
    for i in range(n):
        sumreal = sumimag = 0
        for j in range(n):
            angle = 2 * 3.14159 * j * i/n
            sumreal += input_values[j] * math.cos(angle)
            sumimag += -input_values[j] * math.sin(angle)
        output_real[i] = sumreal
        output_imag[i] = sumimag
    result = [output_real[k] + output_imag[k] for k in range(len(output_real))]
    return result


if __name__ == "__main__":
    answer = dft([0, .7071, 1, .7071, 0, -.7071, -1, -.7071])
    print(answer)