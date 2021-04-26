# Stack , LIFO
# Last In First Out

word = input("Input a word : ")

word_list = list(word)

# for i in range(len(word_list)):
#     print(word_list.pop())

# Input a word : stack
# k
# c
# a
# t
# s

# Queue, FIFO
# First In First Out
# LIFO <-> FIFO
# pop(0)

for i in range(len(word_list)):
    print(word_list.pop(0))