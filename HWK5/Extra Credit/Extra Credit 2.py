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
    alpha_array = [[0 for i in range(len(observation_sequence))] for j in range(len(A_test[0]))]
    alpha_log_array = [None for i in range(len(observation_sequence))]

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
        alpha_log_array[time] = safelog2(sum) + alpha_log_array[time-1] if time > 0 else safelog2(sum)
    return alpha_array, alpha_log_array


def backward_algorithm_renormaliziation(A: list, B: list, pi: list, observation_sequence: list):
    beta_array = [[0 for i in range(len(observation_sequence))] for j in range(len(A[0]))]
    beta_log_array = [None for i in range(len(observation_sequence))]
    for time in reversed(range(len(observation_sequence))):
        column_sum = 0
        for state_list in range(len(A)):
            if time == len(observation_sequence)-1:
                beta_array[state_list][time] = 1
            else:
                sum = 0
                for j in range(len(A[0])):
                    sum += A[state_list][j] * B[j][observation_sequence[time+1]] * beta_array[j][time+1]
                beta_array[state_list][time] = sum
        for row in range(len(A)):
            column_sum += beta_array[row][time]
        beta_log_array[time] = safelog2(column_sum) + beta_log_array[time+1] if time < len(observation_sequence)-1 else safelog2(column_sum)
        for row in beta_array:
            row[time] = row[time]/column_sum
    return beta_array, beta_log_array


if __name__ == "__main__":
    alpha_array, alpha_log_array = Fast_HMM_Forward_Algo_normalization(A_test, B_test, pi_test, observation_sequence_test)
    beta_array, beta_log_array = backward_algorithm_renormaliziation(A_test, B_test, pi_test, observation_sequence_test)
    print(alpha_array)
    print(alpha_log_array)
    print(beta_array)
    print(beta_log_array)