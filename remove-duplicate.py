numbers=[5,1,2,5,6,8,2,1,4,10]
getList=[]

for number in numbers:
      if (number not in  getList):
            getList.append(number)

print(getList)
