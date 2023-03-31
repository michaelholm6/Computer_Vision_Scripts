import math


def inverse_dft(input_values_real: list, input_values_imag: list):
    n = len(input_values_real)
    output = [None] * n
    for i in range(n):
        output[i] = 0
        for j in range(n):
            angle = (2 * 3.1415926 * j * i)/n
            output[i] += (input_values_real[j] * math.cos(angle)) + complex(0, (input_values_imag[j] * math.sin(angle)))
        output[i] /= n
    return output


if __name__ == "__main__":
    output_inverse_dft = inverse_dft([0, 0, 0, 0, 0, 0, 0, 0], [0, -4j, 0, 0, 0, 0, 0, 4j])
    print(output_inverse_dft)