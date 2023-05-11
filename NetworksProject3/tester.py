with open('sampletcpdump.txt') as f:
        lines = f.readlines();
ttlString = "ttl "
ttlNumber = 1
found = True
currentInd = 0
while found and ttlNumber < 255 and currentInd < len(lines):
        currentTTL = ttlString + str(ttlNumber) + ","
        currentLine = ""

        for i in range(3):
                sendInd = 0
                recInd = 0
                sendTime = 0
                recTime = 0
                for j in range (currentInd, len(lines)):
                        if currentTTL in lines[j]:
                                sendInd = j
                                currentInd = j
                                break
                tempLine = lines[sendInd].split(" ")
                sendTime = float(tempLine[0])
                tempLine = tempLine[7].split(",")
                id = tempLine[0]
                ip = ""
                for k in range (currentInd + 2, len(lines)):
                        if id in lines[k]:
                                recInd = k - 2
                                ip = lines[k-1].split(">")
                                ip = ip[0].strip()
                                break
                if(recInd == 0):
                        found = False
                        break
                tempLine = lines[recInd].split(" ")
                recTime = float(tempLine[0])
                time = (recTime - sendTime) * 1000

                if (i == 0):
                        print ("TTL " + str(ttlNumber))
                        print (ip)
                print (str(time) + " ms")
                currentInd+= 2
        ttlNumber+= 1
