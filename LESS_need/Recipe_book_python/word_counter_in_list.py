from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']
words_counter = Counter(words)
top_three = words_counter.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'look']

# for word in morewords:
#     words_counter[word] += 1

words_counter.update(morewords)

top_three = words_counter.most_common(3)
print(top_three)
print(words_counter['eyes'])