import itertools

A_test = [[0.6, 0.4],
     [1, 0]]
B_test = [[0.7, 0.3, 0],
     [0.1, 0.1, 0.8]]
pi_test = [0.7, 0.3]
O1 = (1,0,0,0,1,0,1)
O2 = (0,0,0,1,1,2,0)
O3 = (1,1,0,1,0,1,2)
O4 = (0,1,0,2,0,1,0)
O5 = (2,2,0,1,1,0,1)
observation_sequence_list = [O1, O2, O3, O4, O5]

def Fast_HMM_Forward_Algo(A: list, B: list, pi: list, observation_sequence: list):
    alpha_array = [[0 for i in range(len(observation_sequence))] for j in range(len(A[0]))]

    for time in range(len(alpha_array[0])):
        for state_list in range(len(alpha_array)):
            if time == 0:
                alpha_array[state_list][0] = pi[state_list] * B[state_list][observation_sequence[time]]
            else:
                previous_alpha_sum = 0
                for j in range(len(alpha_array)):
                    previous_alpha_sum += alpha_array[j][time-1] * A[j][state_list]
                alpha_array[state_list][time] = previous_alpha_sum * B[state_list][observation_sequence[time]]

    return alpha_array

def backward_algorithm(A: list, B: list, pi: list, observation_sequence: list, alpha_array: list):
    beta_array = [[0 for i in range(len(observation_sequence))] for j in range(len(A[0]))]
    for time in reversed(range(len(observation_sequence))):
        for state_list in range(len(A)):
            if time == len(observation_sequence)-1:
                beta_array[state_list][time] = 1
            else:
                sum = 0
                for j in range(len(A[0])):
                    sum += A[state_list][j] * B[j][observation_sequence[time+1]] * beta_array[j][time+1]
                beta_array[state_list][time] = sum
    return beta_array


if __name__ == "__main__":
    for observation_sequence in observation_sequence_list:
        alpha_array = Fast_HMM_Forward_Algo(A_test, B_test, pi_test, observation_sequence)
        beta_array = backward_algorithm(A_test, B_test, pi_test, observation_sequence, alpha_array)
    
        likeliehood_list = [None] * len(observation_sequence)
        for column in range(len(alpha_array[0])):
            dot_product = 0
            for row in range(len(alpha_array)):
                dot_product += alpha_array[row][column] * beta_array[row][column]
            likeliehood_list[column] = dot_product
       
        likeliehood = 0 
        likeliehood += sum([alpha[-1] for alpha in alpha_array])
        print(likeliehood)
        print(', '.join(['{:.3e}'.format(x) for x in likeliehood_list]))
    
            