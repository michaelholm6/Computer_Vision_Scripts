import math


def reorg_list(ind, log2n):
    n = 0
    for i in range(log2n):
        """This whole loop is reorganizing the order of the original list in order to build the recursion
        tree that would be created in the recursive algorithm from the bottom up"""
        n <<= 1
        n |= (ind & 1)
        ind >>= 1
    return n


def fft_iterative(input_list):
    n = len(input_list)
    input_reorg = [None] * n
    log2n = int(math.log(n, 2))
    for i in range(n):
        rev_ind = reorg_list(i, log2n)
        input_reorg[i] = input_list[rev_ind]
    for i in range(1, log2n+1):
        element_one = 1 << i
        element_two = element_one >> 1
        omega = 1
        omega_unity = 2.718281**(-1j * 3.1415926/element_two)
        for j in range(element_two):
            for k in range(j, n, element_one):
                t = omega * input_reorg[k + element_two]
                u = input_reorg[k]
                input_reorg[k] = u + t
                input_reorg[k+element_two] = u-t
            omega *= omega_unity
    return input_reorg


a = [0, .7071, 1, .7071, 0, -.7071, -1, -.7071]
answer = fft_iterative(a)

print(answer)






