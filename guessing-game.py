secretWord = 'python'
typedExistsInTheSecretWord = []

while True:

    typedWord = input('Digite uma letra: ')

    if len(typedWord) > 1:
        print('Não vale, você precisa digitar apenas uma paravra!!\n')
        continue

    typedExistsInTheSecretWord.append(typedWord)
    if typedWord in secretWord:
        print('Essa letra está na paravra secreta!!')

    else:
        print('Essa letra não está na palavra secreta!!')
        typedExistsInTheSecretWord.pop()

    temporary_letter = ''
    for secret_word in secretWord:
        if secret_word in typedExistsInTheSecretWord:
            temporary_letter += secret_word
        else:
            temporary_letter += "*"

    if temporary_letter == secretWord:
        print(f'Parabens, você acertou a palavra secreta: {temporary_letter}\n')
        break
    else:
        print(f'A palavra secreta ainda não está batendo, porem olha como ela está: {temporary_letter} tente mais um pouco\n')
