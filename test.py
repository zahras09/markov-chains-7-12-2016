def open_and_read_file(file_path):
    corpus = open(file_path).read()
    return corpus

def make_chains(text_string):
    chains = {}
    words = text_string.split()


    for i in range(len(words)-2):
        chains[(words[i], words[i+1])] = [words[i+2]]
        duplicates = chains.get(key, [])
        duplicates.append(words[i+2])
        chains[key] = duplicates
        return chains

