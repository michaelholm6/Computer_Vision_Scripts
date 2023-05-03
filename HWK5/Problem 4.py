import itertools

A_test = [[0.8, 0.1, 0.1],
     [0.4, 0.2, 0.4],
     [0, 0.3, 0.7]]
B_test = [[0.66, 0.34, 0],
     [0, 0, 1],
     [0.5, 0.4, 0.1]]
pi_test = [0.6, 0, 0.4]
observation_sequence_test = [0,1,0,2,0,1,0]

def backward_algorithm(A: list, B: list, pi: list, observation_sequence: list):
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
    beta_array = backward_algorithm(A_test, B_test, pi_test, observation_sequence_test)
    print(beta_array)
