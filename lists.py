#1
#listy = []
#amountinput = 1
#while True:
#    value = input("Please input 5 values: ")
#    if amountinput == 5:
#        listy.append(value)
#        break
#    else:
#        amountinput += 1
#        listy.append(value)
        
#print("Here's your values: ")

#for value in listy:
#    print(value)
    
#2
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
listofalllists = [list1, list2, list3, list4, list5]
aovil = 1
while True:
    value1 = input("Input 2 values for 5 lists, first list: ")
    if aovil == 2:
        list1.append(value1)
        break
    else:
        aovil += 1
        list1.append(value1)

while True:
    value2 = input("Second list: ")
    if aovil == 3:
        list2.append(value2)
        break
    else:
        aovil += 1
        list2.append(value2)

while True:
    value3 = input("Third list: ")
    if aovil == 4:
        list3.append(value3)
        break
    else:
        aovil += 1
        list3.append(value3)

while True:
    value4 = input("Fourth: ")
    if aovil == 5:
        list4.append(value4)
        break
    else:
        aovil += 1
        list4.append(value4)

while True:
    value5 = input("Finally, the Fifth list: ")
    if aovil == 6:
        list5.append(value5)
        break
    else:
        aovil += 1
        list5.append(value5)

print("Here are your lists: ")
print(listofalllists)




