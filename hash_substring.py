# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text = input()
    if "I" in text:
        pattern = input().rstrip()
        text = input().rstrip()
        return pattern, text
    if "F" in text:
        fl = "./tests/" + "06"
        with open(fl, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
            return pattern, text
    return (input().rstrip(), input().rstrip())
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
    pt_len = len(pattern)
    txt_len = len(text)
    pt_hash = hash(pattern)
    txt_hash = hash(text[:pt_len])

    occurances = []

    for i in range(txt_len - pt_len + 1):
        if pt_hash == txt_hash and text[i:i+pt_len] == pattern:
            occurances.append(i)
        if i < txt_len - pt_len:
            txt_hash = hash(textp[i+1:i+pt_len+1])
    return occurances

    
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

