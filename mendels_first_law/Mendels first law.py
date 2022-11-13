import numpy as np
GG = np.array([[0, 0]])
Gg = np.array([[0, 1]])
gg = np.array([[1, 1]])
each_prob = []
each_domintant_fraction = []
sum_probs = []

# this program is tailored for this specific problem. There is no function that
# helps correlate the probabilities. Only the order of the inputs.


def probability_dom(k, m, n):
    input = [k, m, n]
    for ii in range(len([k, m, n])):
        for iii in range(len([k, m, n])):
            t = k + m + n
            if ii != iii:
                probability = (input[ii] / t) * (input[iii] / (t - 1))
            else:
                probability = (input[ii] / t) * ((input[iii] - 1) / (t - 1))
            each_prob.append(probability)
    print(each_prob)
    print(sum(each_prob))

    for iT in [GG, Gg, gg]:
        for i in [GG, Gg, gg]:
            matrix = iT.T * i
            # print(matrix) ## the order is important
            Dominant_fraction = np.sum(matrix == 0) / 4
            each_domintant_fraction.append(Dominant_fraction)
    print(each_domintant_fraction)

    for n in range(0, 9):
        sum_probs.append(each_domintant_fraction[n] * each_prob[n])
    print(sum(sum_probs))


probability_dom(25, 23, 20)
