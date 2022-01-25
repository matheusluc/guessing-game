
insertCpf = input("Digite o seu CPF, sem os caracteres especiais: ")
multiplicatioFirst = 10
multiplicatioLast = 11
firstVerification = 0
lastVerification = 0
firstResult = 0
lastResult = 0
verificationDigit1 = 0
verificationDigit2 = 0
digit1 = 0




for i in insertCpf:

    i = int(i)

    fistVerification = i * multiplicatioFirst
    multiplicatioFirst -= 1
    firstResult += firstVerification


    if multiplicatioFirst == 2:
        verificationDigit1 = 11 - (firstResult % 11)

        if verificationDigit1 > 9:


            for a in insertCpf:

                a = int(a)
                lastVerification = a * multiplicatioLast
                multiplicatioLast -= 1
                lastResult += lastVerification



                if multiplicatioFirst == 3:
                    #lastResult += (digit1 * 2)

                    print(lastResult)



        else:
            print("xablau")





