

def FFT(input_values: list):
    n = len(input_values)  # n must be a power of 2
    if n == 1:
        return input_values
    omega_first = 2.718281**(-2 * 3.14 * 1j / n)
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


if __name__ == "__main__":
    output_FFT = FFT([0, .7071, 1, .7071, 0, -.7071, -1, -.7071])
    print(output_FFT)
