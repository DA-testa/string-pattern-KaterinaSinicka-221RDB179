# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()
    if "I" in choice:
        pattern = input()
        text = input()
    else:
        folder = "tests/06"
        with open(folder, "r") as files:
            pattern = files.readline()
            text = files.readline()
    
    return (pattern.rstrip(), text.rstrip())
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    # return both lines in one return
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def hash_func(s):
    h = 0
    for c in s:
        h = (h*256 + ord(c)) % 101
    return h

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash_func(pattern)
    t_hashes = [hash_func(text[i:i+p_len]) for i in range(t_len-p_len+1)]
    occurances = [i for i in range(t_len-p_len+1) if t_hashes[i] == p_hash]
    return occurances

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

