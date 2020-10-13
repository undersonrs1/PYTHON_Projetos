def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print()
    print(wordList, end='\n\n')
    return len(wordList), len(content)
n_words, n_chars = readFile('teste.txt',)

#não roda sem a indentação indicada neste código