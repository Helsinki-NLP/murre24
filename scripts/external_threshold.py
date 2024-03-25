
# set threshold number of tokens
threshold = 20

files = [<files>]

for filename in files:
    sentences = []
    f = open(filename, 'r')
    origtext = [line.strip() for line in f]
    for sent in origtext:
        if len(sent.split()) > threshold:
            sentences.append(sent)
        else:
            continue
    f.close()
    
    f_new = open(f"threshold_{filename}", "w")
    for item in sentences:
        f_new.write(item + "\n")
