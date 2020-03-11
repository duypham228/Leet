myList = input("Enter array of streaks:").split()

maxHead = 0
maxTail = 0
tempHead = 0
tempTail = 0

for i in myList:
    # head
    if  i == 'h':
        tempHead += 1
        if tempHead > maxHead:
            maxHead = tempHead
    else:
        tempHead = 0

    # tail
    if  i == 't':
        tempTail += 1
        if tempTail > maxTail:
            maxTail = tempTail
    else:
        tempTail = 0

print("Head:", maxHead, "Tail:", maxTail)