def FFT(input_values: list):
    n = len(input_values)  # n must be a power of 2
    if n == 1:
        return input_values
    omega_first = 2.718281**(-2 * 3.1415926 * 1j / n)
    omega = 1
    a0 = []
    a1 = []
    for i in range(len(input_values)):
        if i % 2 == 0:
            a0.append(input_values[i])
        elif i % 2 == 1:
            a1.append(input_values[i])
    y0 = FFT(a0)
    y1 = FFT(a1)
    output = [None] * n
    for i in range(int((n / 2))):
        output[i] = y0[i] + omega * y1[i]
        output[i + int(n / 2)] = y0[i] - omega * y1[i]
        omega = omega * omega_first
    return output


def IFFT(input_values_real: list, input_values_imag: list):
    """For this IFFT implementation, im taking advantage of the fact that the IFFT of a vector is equal
    to the FFT of the same vector reversed, but keeping it's first value in the same location. The algorithm for
    the IFFT doesn't actually need to be implemented."""
    n = len(input_values_real)
    input_values_real_prefix = input_values_real[0]
    input_values_real = input_values_real[1:n]
    input_values_real.reverse()
    input_values_real = [[input_values_real_prefix] + input_values_real]
    input_values_imag_prefix = input_values_imag[0]
    input_values_imag = input_values_imag[1:n]
    input_values_imag.reverse()
    input_values_imag = [[input_values_imag_prefix] + input_values_imag]
    input_values_imag = input_values_imag[0]
    input_values_real = input_values_real[0]
    real_output = FFT(input_values_real)
    imag_output = FFT(input_values_imag)
    real_output = [x/n for x in real_output]
    imag_output = [x/n for x in imag_output]
    output = [real_output[i] + imag_output[i] for i in range(len(real_output))]

    return output


if __name__ == "__main__":
    IFFT_output = IFFT([0, 0, 0, 0, 0, 0, 0, 0], [0, -4j, 0, 0, 0, 0, 0, 4j])
    print(IFFT_output)
