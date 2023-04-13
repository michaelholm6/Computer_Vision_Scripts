import itertools
import math as m

A_test = [[.66, .34], [1, 0]]
B_test = [[.5, .25, .25], [.1, .1, .8]]
pi_test = [.8, .2]
observation_sequence_test = [2,2,0,1,1,0,1]

def safelog2(x):
    """
    Computes the logarithm base 2 of the number x.

    Returns negative infinity when x is zero.
    
    NOTE: I took this from nanohmm. I completely understand how it works, it's just stupid
    to rewrite code this simplistic. 
    """
    if x == 0:
        return -float('inf')
    else:
        return m.log(x, 2)


def Fast_HMM_Forward_Algo_normalization(A: list, B: list, pi: list, observation_sequence: list):
    LogL = 0
    alpha_array = [[0 for i in range(len(observation_sequence))] for j in range(len(A_test[0]))]

    for time in range(len(alpha_array[0])):
        for state_list in range(len(alpha_array)):
            if time == 0:
                alpha_array[state_list][0] = pi_test[state_list] * B_test[state_list][observation_sequence[time]]
            else:
                previous_alpha_sum = 0
                for j in range(len(alpha_array)):
                    previous_alpha_sum += alpha_array[j][time-1] * A[j][state_list]
                alpha_array[state_list][time] = previous_alpha_sum * B[state_list][observation_sequence[time]]
        sum = 0
        for state in range(len(alpha_array)):
            sum += alpha_array[state][time]
        for state in range(len(alpha_array)):
            if sum != 0:
                alpha_array[state][time] /= sum
        LogL += safelog2(sum)
    return LogL


if __name__ == "__main__":
    output = Fast_HMM_Forward_Algo_normalization(A_test, B_test, pi_test, observation_sequence_test)
    print(output)
