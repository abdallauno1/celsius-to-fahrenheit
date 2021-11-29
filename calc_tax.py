insert = input('insert your status situation\n [0] single\n [1] married jointhly\n [2] married filling separatly\n [3] head for household\n [q] to quit\n').lower()
valTax = 0

while True:
    if insert == 'q':
        print('closing program....')
        exit()
    # single
    if insert == "0":
        income = float(input("insert your income: \n"))
        if (income in range(0 ,8350)):
            valTax = income * 10 / 100
            print("for your status and your income that your inserted {} , the tax calcualtion will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(8351,33950)):
            valTax = ( income * 15 ) / 100
            print("for your status and your income that your inserted {} , the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(33951,82250)):
            valTax = ( income * 25 )/ 100
            print("for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(82251,171550)):
            valTax = ( income * 28 )/ 100
            print("for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(171551,372950 )):
            valTax = ( income * 33 ) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif ( income > 372950):
            valTax = (income * 35 ) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()


    # marreid
    if insert == "1":
        income = float(input("insert your income: \n"))
        if (income in range(0 ,16700)):
            valTax = income * 10 / 100
            print("for your status and your income that your inserted {} , the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(16701,67900)):
            valTax = ( income * 15 ) / 100
            print("for your status and your income that your inserted {} , the tax calculation will be :\n".format(
                income))
            print(valTax)
            exit()
        elif (income in range(67901,137050)):
            valTax = ( income * 25 )/ 100
            print("for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(137051,208850)):
            valTax = ( income * 28 )/ 100
            print("for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(208851,372950 )):
            valTax = ( income * 33 ) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif ( income > 372950):
            valTax = (income * 35 ) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()

    # separated
    if insert == "2":
        income = float(input("insert your income: \n"))
        if (income in range(0 ,8350)):
            valTax = income * 10 / 100
            print("for your status and your income that your inserted {} , the tax calcualtion will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(8351, 33950)):
            valTax = (income * 15) / 100
            print("for your status and your income that your inserted {} , the tax calculation will be :\n".format(
                income))
            print(valTax)
            exit()
        elif (income in range(33951, 68525)):
            valTax = (income * 25) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(68526, 104425)):
            valTax = (income * 28) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(104426, 186475)):
            valTax = (income * 33) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income > 186475):
            valTax = (income * 35) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()

    # household
    if insert == "3":
        income = float(input("insert your income: \n"))
        if (income in range(0 ,11950)):
            valTax = income * 10 / 100
            print("for your status and your income that your inserted {} , the tax calcualtion will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(11951, 45500)):
            valTax = (income * 15) / 100
            print("for your status and your income that your inserted {} , the tax calculation will be :\n".format(
                income))
            print(valTax)
            exit()
        elif (income in range(45501, 117450)):
            valTax = (income * 25) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(117451, 190200)):
            valTax = (income * 28) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income in range(190201, 372950)):
            valTax = (income * 33) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()
        elif (income > 372950):
            valTax = (income * 35) / 100
            print(
                "for your status and your income that your inserted {}, the tax calculation will be :\n".format(income))
            print(valTax)
            exit()


