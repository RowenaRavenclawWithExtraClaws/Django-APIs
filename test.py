#O(k * n)
def even_sub_array(numbers, k): 
    count = 0
 
    for m in range(k + 1):
        prefix = [0] * (len(numbers))
        odd = 0
 
        for i in range(len(numbers)):
            prefix[odd] += 1
 
            if (numbers[i] & 1):
                odd += 1
    
            if (odd >= m):
                count += prefix[odd - m]
 
    return count

#------------------------------------------------------

#O(m * n + m^2*s)
def areAnagram(word1, word2):
    if len(word1) != len(word2):
        return False

    char_count_list = [0] * 26
    chars = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(word1)):
        char_count_list[chars.find(word1[i])] += 1
        char_count_list[chars.find(word2[i])] += 1

    for count in char_count_list:
        if (count % 2 != 0):
            return False

    return True

def get_anagram_dict(word_set):
    anagram_dict = {}

    for i in range(len(word_set) - 1):
        for j in range(i + 1, len(word_set)):
            if areAnagram(word_set[i], word_set[j]) and word_set[i] not in anagram_dict:
                anagram_dict[word_set[i]] = word_set[j]
                anagram_dict[word_set[j]] = word_set[i]
    
    return anagram_dict

def count_sentences(word_set, sentences):
    sol = [0] * len(sentences)
    anagram_dict = get_anagram_dict(word_set)

    for i in range(len(sentences)):
        for word in sentences[i].split(" "):
            if word in anagram_dict:
                sol[i] += 2

    return sol

#------------------------------------------------------

# O(nlogn)
def closetNumbers(numbers):
    numbers = sorted(numbers)
    min_diff = float('inf')

    for i in range(len(numbers) - 1):
        min_diff = min(min_diff, abs(numbers[i] - numbers[i + 1]))

    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) == min_diff:
            print(numbers[i], numbers[i + 1])

#------------------------------------------------------

# O(n)
def countMoves(numbers):
    sum = 0
    smallest = numbers[0]

    for num in numbers:
        smallest = min(smallest, num)
        sum += num

    return sum - len(numbers) * smallest
