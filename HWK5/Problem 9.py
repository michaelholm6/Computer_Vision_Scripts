import nanohmm as hmm

import itertools

A_test_1 = [[0.33, 0, 0, 0.67, 0],
      [0.67, 0, 0.33, 0, 0],
      [0, 1.0, 0.0, 0, 0],
      [0, 0, 0, 0.25, 0.75],
      [0.0, 0.0, 0.6, 0, 0.4]]
B_test_1 = [[0.67, 0, 0, 0, 0, 0.33],
      [0.0, 1.0, 0, 0, 0, 0],
      [0.5, 0, 0, 0, 0, 0.5],
      [0, 0, 0, 0.25, 0.75, 0],
      [0, 0.0, 0.6, 0.4, 0, 0.0]]
pi_test_1 = [0.0, 0.0, 0.0, 1.0, 0.0]
observation_sequence_test_1 = [4,2,5,1,5,1,5,3,2,3,2,0,1,0,0,4,4,3,0,1]
A_test_2 = [[0.0, 0.0, 1.0, 0, 0.0],
      [0.0, 0, 0.0, 0.0, 1.0],
      [0.38, 0.0, 0.23, 0.38, 0.0],
      [0.0, 0.31, 0.0, 0.69, 0],
      [0.0, 0.75, 0.0, 0.25, 0.0]]
B_test_2 = [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
      [0.0, 0.6, 0.2, 0.2, 0.0, 0.0],
      [0.0, 0.0, 0, 1.0, 0.0, 0],
      [0, 0.0, 0, 0.22, 0.0, 0.78],
      [0.6, 0.0, 0.0, 0.0, 0.4, 0.0]]
pi_test_2 = [0.0, 0.0, 1.0, 0.0, 0.0]
observation_sequence_test_2 = [3,2,3,3,5,5,5,5,1,0,1,4,2,4,3,0,5,3,1,0]
A_test_3 = [[0, 0.0, 0.32, 0.18, 0.5],
      [0.0, 0.0, 0.0, 1.0, 0.0],
      [0, 0.0, 0, 0.0, 1.0],
      [0, 0.64, 0, 0.0, 0.36],
      [1.0, 0.0, 0, 0, 0]]
B_test_3 = [[0.0, 0.17, 0.33, 0.0, 0.0, 0.5],
      [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
      [0.47, 0.0, 0.0, 0.0, 0.0, 0.53],
      [0.27, 0.0, 0.0, 0.0, 0.73, 0.0],
      [0.66, 0.0, 0.0, 0.33, 0.0, 0.0]]
pi_test_3 = [0.0, 0.0, 0.0, 1.0, 0.0]
observation_sequence_test_3 = [4,3,0,3,4,0,1,0,2,0,5,3,2,0,0,5,5,3,5,4]
A_test_4 =  [[0.0, 0.0, 1.0, 0, 0.0],
      [0.0, 0, 0.62, 0, 0.38],
      [0.0, 0.5, 0.0, 0.5, 0.0],
      [0.0, 0.23, 0.0, 0.0, 0.77],
      [0.0, 0, 0, 1.0, 0]]
B_test_4 = [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
      [0.0, 0.0, 0.62, 0, 0.38, 0.0],
      [0, 0.0, 0.0, 0.0, 1, 0],
      [0, 0.0, 0, 0.41, 0.18, 0.41],
      [0.31, 0.16, 0.37, 0.16, 0, 0.0]]
pi_test_4 = [1.0, 0.0, 0.0, 0.0, 0]
observation_sequence_test_4 = [3,4,2,0,5,4,4,3,1,5,3,3,2,3,0,4,2,5,2,4]
A_test_5 = [[0.5, 0.33, 0, 0.17, 0.0],
      [0.0, 0.0, 0.0, 0.0, 1.0],
      [0.75, 0.0, 0.25, 0.0, 0.0],
      [0.0, 0.0, 0, 1.0, 0.0],
      [0.0, 0.0, 1.0, 0.0, 0.0]]
B_test_5 = [[0.0, 0.0, 0.0, 0.0, 1.0, 0],
      [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0, 1.0],
      [0.0, 0.0, 0.0, 0.0, 0, 1.0],
      [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
pi_test_5 = [0.0, 1.0, 0.0, 0.0, 0.0]
observation_sequence_test_5 = [2,0,5,4,4,2,0,5,5,4,4,2,0,5,4,4,5,5,5,5]

HMM_Parameter_Collection = [[A_test_1, B_test_1, pi_test_1], [A_test_2, B_test_2, pi_test_2], [A_test_3, B_test_3, pi_test_3], [A_test_4, B_test_4, pi_test_4], [A_test_5, B_test_5, pi_test_5]]
HMM_Observation_collection = [observation_sequence_test_1, observation_sequence_test_2, observation_sequence_test_3, observation_sequence_test_4, observation_sequence_test_5]


if __name__ == "__main__":
    hmm_collection = []
    forward_algo_collection = []
    for i in range(1, 6):
        hmm_collection.append(hmm.hmm_t(HMM_Parameter_Collection[i-1][0], HMM_Parameter_Collection[i-1][1], HMM_Parameter_Collection[i-1][2]))
    for hmm_index in hmm_collection:
        forward_algo_collection.append(hmm.forward_t(hmm_index, 20))
        print("Results for HMM " + str(len(forward_algo_collection)))
        for obsvertation in HMM_Observation_collection:
            print(forward_algo_collection[-1](obsvertation))
        pause = input("Press enter to continue")
            

