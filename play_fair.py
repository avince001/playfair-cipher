key = input("Enter the key : ")

msg = input("Enter your message : ")

list1=[[0 for j in range(5)] for i in range(5)]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'  # 'X' is excluded

list2 = []

for k in key:
	if k not in list2:
		list2.append(k)

for k in alphabet:
	if k not in list2:
		list2.append(k)

list2_index = 0

for i in range(0,5):
	for j in range(0,5):
		list1[i][j] = list2[list2_index]
		list2_index = list2_index+1

def in_list(char, classes):
    for i, sublist in enumerate(classes):
        if char in sublist:
            return [i, classes[i].index(char)]
    return -1

msg = msg.replace(" ","")
if len(msg)%2!=0:
    msg = msg + 'Z'

choice = int(input("Do you want to encode(0) or decode(1) ?"))

if choice == 0:

    for i in range(0,len(msg)-1,2):
        list3 = []
        list4 = []
        list3.append(in_list(msg[i],list1))
        list3.append(in_list(msg[i+1],list1))

        #print(list3)

        if list3[0][0] == list3[1][0] :
            #print('Case 1')
            if list3[0][1] == 4:
                list3[0][1] = 0
                print(list1[list3[0][0]][list3[0][1]],end="")
                print(list1[list3[1][0]][list3[1][1]+1],end="")
            elif list3[1][1] == 4:
                list3[1][1] = 0
                print(list1[list3[0][0]][list3[0][1]+1],end="")
                print(list1[list3[1][0]][list3[1][1]],end="")
            else:
                print(list1[list3[0][0]][list3[0][1]+1],end="")
                print(list1[list3[1][0]][list3[1][1]+1],end="")

        elif list3[0][1] == list3[1][1]:
            #print('Case 2')
            if list3[0][0] == 4:
                list3[0][0] = 0
                print(list1[list3[0][0]][list3[0][1]],end="")
                print(list1[list3[1][0]+1][list3[1][1]],end="")
            elif list3[1][0] == 4:
                list3[1][0] = 0
                print(list1[list3[0][0]+1][list3[0][1]],end="")
                print(list1[list3[1][0]][list3[1][1]],end="")
            else:
                print(list1[list3[0][0]+1][list3[0][1]],end="")
                print(list1[list3[1][0]+1][list3[1][1]],end="")

        else:
            #print('Case 3')
            print(list1[list3[0][0]][list3[1][1]],end="")
            print(list1[list3[1][0]][list3[0][1]],end="")

        #print(list3)
        #print("----------------")

if choice == 1:
    for i in range(0,len(msg)-1,2):
        list3 = []
        list4 = []
        list3.append(in_list(msg[i],list1))
        list3.append(in_list(msg[i+1],list1))

        #print(list3)

        if list3[0][0] == list3[1][0] :
            #print('Case 1')
            if list3[0][1] == 0:
                list3[0][1] = 4
                print(list1[list3[0][0]][list3[0][1]],end="")
                print(list1[list3[1][0]][list3[1][1]-1],end="")
            elif list3[1][1] == 0:
                list3[1][1] = 4
                print(list1[list3[0][0]][list3[0][1]-1],end="")
                print(list1[list3[1][0]][list3[1][1]],end="")
            else:
                print(list1[list3[0][0]][list3[0][1]-1],end="")
                print(list1[list3[1][0]][list3[1][1]-1],end="")

        elif list3[0][1] == list3[1][1]:
            #print('Case 2')
            if list3[0][0] == 0:
                list3[0][0] = 4
                print(list1[list3[0][0]][list3[0][1]],end="")
                print(list1[list3[1][0]-1][list3[1][1]],end="")
            elif list3[1][0] == 0:
                list3[1][0] = 4
                print(list1[list3[0][0]-1][list3[0][1]],end="")
                print(list1[list3[1][0]][list3[1][1]],end="")
            else:
                print(list1[list3[0][0]-1][list3[0][1]],end="")
                print(list1[list3[1][0]-1][list3[1][1]],end="")

        else:
            #print('Case 3')
            print(list1[list3[0][0]][list3[1][1]],end="")
            print(list1[list3[1][0]][list3[0][1]],end="")

        


    
