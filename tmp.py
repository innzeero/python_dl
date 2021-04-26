# 1 stack , LIFO

word = input("Input a word : ")

word_list = list(word)

for i in range(len(word_list)):
    print(word_list.pop())

# Input a word : stack
# k
# c
# a
# t
# s