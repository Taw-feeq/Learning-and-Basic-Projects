'''# Input Reading
K = int(input())  # Number of words
words = [input().strip() for _ in range(K)]  # List of words
N, M = map(int, input().split())  # Number of lines and max length per line

# Function to calculate the maximum number of words that can be arranged
def max_words_in_lines(words, N, M):
    current_line_length = 0
    lines_used = 1
    words_used = 0

    for word in words:
        word_length = len(word)
        # Check if the current word fits in the current line
        if current_line_length + word_length <= M:
            current_line_length += word_length + 1  # Add word and space
            words_used += 1
        else:
            # Move to the next line
            lines_used += 1
            if lines_used > N:  # If no more lines are available, stop
                break
            current_line_length = word_length + 1
            words_used += 1

    return words_used

# Sorting words by length ensures shorter words can fit better
words.sort(key=len)
max_words = max_words_in_lines(words, N, M)

# Output the result
print(max_words)




K = int(input())  # Number of words
words = [input().strip() for _ in range(K)]  # List of words
N, M = map(int, input().split(" "))  # Number of lines and max length per line

def max_words_in_lines(words, N, M):
    current_line_length = 0
    lines_used = 1
    words_used = 0

    for word in words:
        word_length = len(word)
        # Check if the current word fits in the current line
        if current_line_length + word_length <= M:
            current_line_length += word_length + 1  # Add word and space
            words_used += 1
        else:
            # Move to the next line
            lines_used += 1
            if lines_used > N:  # If no more lines are available, stop
                break
            current_line_length = word_length + 1
            words_used += 1

    return words_used

# Sorting words optimally by lexicographical order
words.sort()
max_words = max_words_in_lines(words,N,M);


k = int(input())
words = [input().strip() for _ in range(k)]
n, m = map(int, input().split())

def word_fit(k, valid_words, n, m):
    valid_words = [word for word in words if len(word) <= m]

    def backtracking(index, lines):
        if index == len(words):
            return sum(len(line.split()) for line in lines)

        max_words = 0
        word = valid_words[index]

        for i in range(len(lines)):
            if len(lines[i]) + len(word) + (1 if lines[i] else 0) <= m:
                original_line = lines[i]
                lines[i] += (" " if lines[i] else "") + word
                max_words = max(max_words, backtracking(index + 1, lines))
                lines[i] = original_line  

        if len(lines) < n:
            lines.append(word)
            max_words = max(max_words, backtracking(index + 1, lines))
            lines.pop()  

        return max_words

    return backtracking(0, [])

print(word_fit(k, words, n, m))
'''

k = int(input())  
words = [input().strip() for _ in range(k)]  
n, m = map(int, input().split())  

def word_fit(k, word_list, n, m):
    valid_words = [word for word in word_list if len(word) <= m]

    def backtracking(index, lines):
        if index == len(valid_words):
            return sum(len(line.split()) for line in lines)

        max_words = 0
        current_word = valid_words[index]

        for i in range(len(lines)):
            if len(lines[i]) + len(current_word) + (1 if lines[i] else 0) <= m:
                original_line = lines[i]
                lines[i] += (" " if lines[i] else "") + current_word

                max_words = max(max_words, backtracking(index + 1, lines))
                lines[i] = original_line

        if len(lines) < n:
            lines.append(current_word)
            max_words = max(max_words, backtracking(index + 1, lines))
            lines.pop()  

        return max_words

    return backtracking(0, []) 

print(word_fit(k, words, n, m))
