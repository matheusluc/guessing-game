secretWord = 'python'
typedExistsInTheSecretWord = []

while True:

    typedWord = input('Digite uma letra: ')

    if len(typedWord) > 1:
        print('Não vale, você precisa digitar apenas uma paravra!!')
        continue

    letra = typedWord
    for letra in secretWord:
        if letra == secretWord:
            print('essa letra está na paravra secreta!!')

        else:
            print('Essa letra não está na palavra secreta!!')