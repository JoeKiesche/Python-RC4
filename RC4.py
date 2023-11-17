#needed fucntions
#   key scheduling
#   key stream generating
#   Print results 
#   XOR
#   convert to hexidecimal
#   main



#   Key for practical use -- "Password"
#   Plaintext for pratical use -- "joseph"
#   1. key scheduling algo
#   2. pusedo random algo - length of plaintext string
#   3. Then gets xored bit by bit by the stream to find the cipher text



#KSA fucntion that has parameters:
#   Key which was determined to be "password"
#RETURNS -- a list S
def KSA(key):
    #Key-scheduling algorithm
    keysize = len(key)
    #get ord values of the key

    ordinal = []
    for a in key:
        h = ord(a)
        ordinal.append(h)
    print("this is ordinal values", ordinal,"\n")
    #S list to 256 permuatations
    S = list(range(256))
    #counter
    j = 0
    
    for i in range(256):
        j =  (j +S[i] + ordinal[i % keysize]) % 256
        #Swap the values of s[i] and s[j]
        S[i], S[j] = S[j], S[i]

    print(S) 
    return S      

    
#PRGA fucntiont that has parameters:
#   h3 which is the list of values given from the KSA
#   and the plaintext which is hard coded to be my name: joseph
#RETURNS -- array K which is length of plaintext
def Pseudo_random_generation_algorithm(h3, plaintext):
    #i = p counters
    #j = y counters
    p = 0
    y = 0
    k = []
    n = len(plaintext)
    #print("\n this is h3", h3, "\n")
    while n > 0:
        n = n - 1
        p = (p + 1) %256
        print("p is", p)
        y = (y + h3[p]) % 256
        #swaps the values bc we are using lists
        h3[p], h3[y] = h3[y], h3[p]
        
        h2 = h3[(h3[p]+h3[y]) % 256]
        k.append(h2)
        print(k)
    return k


#Print results fucntion with parameters:
#   Plaintext hardcoded to be "joseph"
#   key which was determined to be "password"
#   and the cipherText which is given from KSA and PRGA functions
#RETURNS -- nothing just a print function
def printResults(plaintext, key, ciphertext):
    print("#############################################################################")
    print("\nStarting encryption.....")
    print("the plaintext was: ", plaintext)
    print("the key was: ", key)
    newstr = ""
    for x in ciphertext:
        newstr = newstr + x.replace('0x','')
    print("which makes the cipher text become: \n", newstr,"\n")
    print("##############################################################################")
    



#XOR function that takes has parameters
#   Stream created by PRGA
#   plaintext hardcoded in
#RETURNS -- an array that is XORED then converted to hexidecimals
def XOR(stream, plaintext):
    w = len(plaintext)
    print("THIs is the stream =---------=\n", stream)
    xoredArray = []
    while w > 0:
        w = w - 1
        for d in stream:
            binaryStreamHolder = d
            

        for q in plaintext:
            
            binaryPlainHolder = ord(q)

            xored = binaryStreamHolder ^ binaryPlainHolder
            xoredArray.append(xored)


    
    print("\nxored: ", xoredArray,"\n")
    hexArr = hexi(xoredArray)
    return hexArr


#fucntion to convert to hexidecimal with parameters:
#   XoredArray which is created in the XOR function
#RETURNS -- hexArray which is an array of the values just converted to hexidecimal   
def hexi(XoredArray):
    hexArray = []
    for r in XoredArray:
        h7 = hex(r)
        hexArray.append(h7)
    return hexArray


#MAIN fucntion with parameters:
#   Nothing 
#RETURNS -- nothing 
def main():
    #another holder value
    plaintext = "joseph"
    h3 = KSA("password")
    stream = Pseudo_random_generation_algorithm(h3, "joseph")
    cipherText = XOR(stream, plaintext)

    printResults("joseph", "password", cipherText)
    
    

main()
