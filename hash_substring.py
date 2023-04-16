# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().strip()
    if input_type = 'I':
        pattern = input().strip()
        text = input().strip()
    else:
        with open(input_type) as F:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    # return both lines in one return
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    p = len(pattern)
    t = len(text)
    occurances = []
    # Calculate
    hash_pattern = sum(ord(pattern[i]) * (31**i) for i in range(p)) 
    hash_text = sum(ord(text[i]) * (31**i) for i in range(p))

    for i in range(t - p + 1):
        if hash_pattern == hash_text:
            if text[i:i+p] == pattern:
                occurances.append(i)
        if i < t - p:
            hash_text = 31 * (hash_text - ord(text[i]) * (31 ** (p-1))) + ord(text[i+p])
    # and return an iterable variable
    return occurances
    
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

