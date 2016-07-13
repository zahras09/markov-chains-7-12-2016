def open_and_read_file(file_path):
    corpus = open(file_path).read()
    return corpus

def make_chains(text_string):
    chains = {}
    words = text_string.split()


    for i in range(len(words)-2):
        key = (words[i], words[i+1]) 
        chains[key] = [words[i+2]]
        duplicates = chains.get(key, [])
        duplicates.append([words[i+2]])
        # chains[key] = duplicates
    print chains

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)