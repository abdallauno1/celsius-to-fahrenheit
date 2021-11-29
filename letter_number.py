lett = input ("Provide letters for conversion without using space: ")
NumList = []
letters = []
for let in lett:

         letters.append(let)
         numbers = ord (let) - 96
         NumList.append (numbers)


print ("Corresponding numbers for the letters {} given are:\n".format(letters), NumList)