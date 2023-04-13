import itertools

A_test_1 = [[1.0, 0.0], [0.5, 0.5]]
B_test_1 = [[0.4, 0.6, 0.0], [0.0, 0.0, 1.0]]
pi_test_1 = [0.0, 1.0]
observation_sequence_test_1 = [1,0,0,0,1,0,1]
A_test_2 = [[0.25, 0.75], [1.0, 0.0]]
B_test_2 = [[0, 1.0, 0], [0.66, 0.0, 0.34]]
pi_test_2 = [1.0, 0.0]
observation_sequence_test_2 = [0,0,0,1,1,2,0]
A_test_3 = [[0.0, 1.0], [1.0, 0.0]]
B_test_3 = [[1.0, 0.0, 0.0], [0.0, 0.66, 0.34]]
pi_test_3 = [1.0, 0.0]
observation_sequence_test_3 = [1,1,0,1,0,1,2]
A_test_4 =  [[1, 0], [0.44, 0.56]]
B_test_4 = [[0.36, 0.42, 0.22], [1.0, 0, 0]]
pi_test_4 = [0, 1.0]
observation_sequence_test_4 = [0,1,0,2,0,1,0]
A_test_5 = [[0.0, 1.0], [1.0, 0.0]]
B_test_5 = [[0.25, 0.75, 0.0], [1.0, 0.0, 0.0]]
pi_test_5 = [1.0, 0.0]
observation_sequence_test_5 = [2,2,0,1,1,0,1]

HMM_Parameter_Collection = [[A_test_1, B_test_1, pi_test_1], [A_test_2, B_test_2, pi_test_2], [A_test_3, B_test_3, pi_test_3], [A_test_4, B_test_4, pi_test_4], [A_test_5, B_test_5, pi_test_5]]
HMM_Observation_collection = [observation_sequence_test_1, observation_sequence_test_2, observation_sequence_test_3, observation_sequence_test_4, observation_sequence_test_5]


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


if __name__ == "__main__":
    for i in range(1, 6):
        for j in range(1, 6):
            output = Fast_HMM_Forward_Algo(HMM_Parameter_Collection[i-1][0], HMM_Parameter_Collection[i-1][1], HMM_Parameter_Collection[i-1][2], HMM_Observation_collection[j-1])
            answer_sum = 0
            for k in output:
                answer_sum += k[-1]
            print(answer_sum)
        pause = input("Press enter to continue")
