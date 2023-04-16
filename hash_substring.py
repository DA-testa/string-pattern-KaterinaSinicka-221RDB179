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

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    p_len = len(pattern)
    t_len = len(text)
    p_hash = sum(ord(pattern[i]) * pow(256, p_len - i - 1) for i in range(p_len))
    t_hash = sum(ord(text[i]) * pow(256, p_len - i - 1) for i in range(p_len))

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                occurances.append(i)
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(256, p_len - 1)) * 256 + ord(text[i+p_len])

    return occurances

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

