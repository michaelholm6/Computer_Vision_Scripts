import nanohmm as nhmm
from random import random

O1 = (4,2,5,1,5,1,5,3,2,3,2,0,1,0,0,4,4,3,0,1)
O2 = (3,2,3,3,5,5,5,5,1,0,1,4,2,4,3,0,5,3,1,0)
O3 = (4,3,0,3,4,0,1,0,2,0,5,3,2,0,0,5,5,3,5,4)
O4 = (3,4,2,0,5,4,4,3,1,5,3,3,2,3,0,4,2,5,2,4)
O5 = (2,0,5,4,4,2,0,5,5,4,4,2,0,5,4,4,5,5,5,5)

states = 4

A_initial_state = [[random() for i in range(states)] for j in range(states)]
B_initial_state = [[random() for i in range(6)] for j in range(states)]
pi_initial_state = [random() for i in range(states)]

initial_HMM = nhmm.hmm_t(A_initial_state, B_initial_state, pi_initial_state)
Baum_Welch = nhmm.baumwelch_t(initial_HMM, 20)
forward_backward, parameters = Baum_Welch(O5, 100000)
print('A=' + str(parameters.A) + '\n' + 'B=' + str(parameters.B) + '\n' + 'pi=' + str(parameters.pi))