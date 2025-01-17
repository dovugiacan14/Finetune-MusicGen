"""Assignment 22: Generate Parentheses 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1: 
- Input: n = 3 
- Ouput: ["((()))","(()())","(())()","()(())","()()()"]
"""
def generate_parenthesis(n):
    result = []
    def back_track(s, open, close): 
        if len(s) == 2*n:
            result.append(s)
            return 

        if open < n: 
            back_track(s + "(", open + 1, close)
        if close < open: 
            back_track(s + ")", open, close + 1)
    back_track("", 0, 0)
    return result 


"""Assignment 30: Substring with Concatenation of All Words 

You are given a string s and an array of strings words. 
All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

Example 1: 
- Input:  s = "barfoothefoobarman", words = ["foo","bar"]
- Ouput: [0, 9]
- Explaination: 
    + The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
    + The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

"""
from itertools import permutations
from collections import Counter
def find_substring(s, words):
    permutate_lst = ["".join(word) for word in permutations(words)]
    len_words = len(permutate_lst[0])
    result = []
    idx = 0 
    while True: 
        if idx >= len(s):
            break 
        if s[idx:idx+len_words] in permutate_lst: 
            result.append(idx)
        idx += 1
    return result 

def find_substring(s, words): 
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words) # count the frequency of each word in list 

    result = []
    for i in range(word_len):
        left = i 
        right = i 
        current_freq = Counter()
        while right + word_len <= len(s):
            word = s[right : right + word_len]
            right += word_len   # update right index 
            if word in word_freq:
                current_freq[word] += 1 

                while current_freq[word] > word_freq[word]:
                    current_freq[s[left:left + word_len]] -= 1
                    left += word_len
                
                if right - left == total_len:
                    result.append(left)
            else: 
                current_freq.clear()
                left = right 
    return result