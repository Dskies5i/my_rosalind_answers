#import this

#Variables and Some Arithmetic

# a = 866
# b = 880
#
# print(f'{a}^2 + {b}^2 = {a**2 + b**2}')


#3 Strings and lists

# wordonestart = 22
# wordonefinish = 32
# wordstwostart =  85
# wordtwofinish = 92
#
# given_list = "sxg6YBh2yMpklfYvzIXSgbEublepharis9sWQUNspRC4yWbWJXh4ESov2GkcGgjUjjZONsMQIG3yAllbtesngtarandus8cXkRZvyk7Cy05YHaNuzhuzo1ht6rs8RxoKkfMNko6eCLEFKwG9VycErMuGBtKYCbRpTsDpgBMwmPGBbbb9MNiVsQVKxG."
#
# print(f'{given_list[wordonestart:wordonefinish + 1]} {given_list[wordstwostart:wordtwofinish + 1]}')


#4 ==================== Conditions and Loops  ===================
# startpos= 4163
# endpos = 8991
# result = 0
#
# for x in range (startpos, endpos + 1):
#     if x %2 != 0:
#         result += x
#
# # result = [x for x in range (startpos, endpos + 1) if x %2 ! = 0]
# print (result)


#5 ==================== Reading and Writing  ===================
# outputfile = []
#
# with open('C:/Users/Jose Isidoro/Desktop/bioinformatics python/village/input.txt', 'r') as f:
#     outputfile = [line for pos, line in enumerate (
#         f.readlines()) if pos  %2 != 0]
#
# with open('C:/Users/Jose Isidoro/Desktop/bioinformatics python/village/out.txt', 'w') as f:
#     f.write(' '.join([line for line in outputfile]))
#
#
# print(outputfile)


#6 ==================== Dictionaries ===================
from collections import Counter
txtstring = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
#method 1
# wordcountdict = {}
# for word in txtstring.split(' '):
#     if word in wordcountdict:
#         wordcountdict[word] += 1
#     else:
#         wordcountdict[word] =  1
# for key, value in wordcountdict.items():
#     print(key, value)


# #method 2 Counter
wordcountdict = Counter(txtstring.split(' '))
for key, value in wordcountdict.items():
    print(key, value)
