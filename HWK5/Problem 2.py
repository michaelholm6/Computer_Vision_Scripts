import itertools

A_test = [[0.6, 0.4],
     [1, 0]]
B_test = [[0.7, 0.3, 0],
     [0.1, 0.1, 0.8]]
pi_test = [0.7, 0.3]
observation_sequence_test = [2,2,0,1,1,0,1]


def Fast_HMM_Forward_Algo(A: list, B: list, pi: list, observation_sequence: list):
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

    return alpha_array


if __name__ == "__main__":
    output = Fast_HMM_Forward_Algo(A_test, B_test, pi_test, observation_sequence_test)
    print(output)
    answer_sum = 0
    for i in output:
        answer_sum += i[-1]
    print(answer_sum)
