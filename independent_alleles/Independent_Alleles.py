"""
Given: Two positive integers k (k≤7) and N (N≤2^k). In this problem,
we begin with Tom, who in the 0th generation has genotype Aa Bb.
Tom has two children in the 1st generation, each of whom has two children, and so on.
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N (Aa Bb) organisms will belong
to the k-th generation of Tom's family tree (don't count the Aa Bb
mates at each level). Assume that Mendel's second law holds for the factors.

Tom(AaBb) x (AaBb)
1()x(AaBb) + 2()x(AaBb)

1x1
1x1 + 1x1
(1x1 + 1x1) + (1x1 + 1x1)
(1x1 + 1x1)+(1x1 + 1x1)+(1x1 + 1x1)+(1x1 + 1x1)

"""
# https://georginalesliedotcom.wordpress.com/2020/09/28/independent-alleles-part-one/
# http://saradoesbioinformatics.blogspot.com/2016/07/independent-alleles.html
# calculate the probability that at least N (Aa Bb) organisms will belong
# to the k-th generation of Tom's tree (dont count the mates at each level)
import math
# calculates the probability that from the total 2^k, at least N individuals will be AaBb. It means, the sum of probability
# from 34 to 2^k
k = 7
N = 34
P = 2**k
probability = 0
for i in range(N, P + 1):
    print(i)
    prob = (math.factorial(P) /
            (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))
    probability += prob
print(probability)
