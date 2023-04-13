import itertools

A_test = [[.66, .34], [1, 0]]
B_test = [[.5, .25, .25], [.1, .1, .8]]
pi_test = [.8, .2]
observation_sequence_test = [0, 1, 0, 2, 0, 1, 0]


def Slow_HMM_Forward_Algo(A: list, B: list, pi: list, observation_sequence: list):
    possible_states = []

    for i in range(len(pi_test)):
        possible_states.append(i)

    testing_states = [state for state in itertools.product(possible_states, repeat=len(observation_sequence_test))]

    list_of_likelihoods = []

    for state_list in testing_states:
        likelihood = 1
        for state in range(len(state_list)):
            if state == 0:
                likelihood *= pi[state_list[0]] * B[state_list[state]][observation_sequence[state]]
            else:
                likelihood *= A[state_list[state-1]][state_list[state]] * B[state_list[state]][observation_sequence[state]]
        list_of_likelihoods.append(likelihood)

    return list_of_likelihoods


if __name__ == "__main__":
    output = Slow_HMM_Forward_Algo(A_test, B_test, pi_test, observation_sequence_test)
    print(sum(output))