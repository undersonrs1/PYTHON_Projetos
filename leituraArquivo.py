def readFile(filename): # cria função readfile apos busca de filename

    infile = open(filename, 'r') # associa o comando de leitura de arquivo ao filename indicado

    content = infile.read() # associa cada palavra lida no arquivo aberto a content

    infile.close() # encerra a leitura do arquivo

    wordList = content.split() # cria uma lista de palavras wordlist 

    print() # pula uma linha

    print(wordList, end='\n\n') # exibe as palavras encontradas e pula linha

    return len(wordList), len(content) # mostra quantidade de palavras na wordlist e também quantidade de letras

n_words, n_chars = readFile('teste.txt',)

# não roda sem a indentação indicada neste código
# funciona em conjunto com teste.txt, é lá que fica o texto