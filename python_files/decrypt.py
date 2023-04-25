def decryptText(ciphertext, key):
    a = 0
    b = 1
    c = 0
    m = 0
    k = 0
    j = 0
    decrypted = ""
    temp = ""
 
    # Reverse the key and add to ciphertext
    pw = key[::-1] + ciphertext
 
    # For future Purpose
    temp = pw
    stringArray = list(temp)
    evenString = ""
    oddString = ""
 
    # Declare EvenArray for storing
    # even index of stringArray
    evenArray = ""
 
    # Declare OddArray for storing
    # odd index of stringArray
    oddArray = ""
 
    # Storing the positions in their
    # respective arrays
    for i in range(len(stringArray)):
 
        if (i % 2 == 0):
 
            oddString = oddString + stringArray[i]
 
        else:
            evenString = evenString + stringArray[i]
 
    evenArray = ["" for _ in range(len(evenString))]
    oddArray = ["" for _ in range(len(oddString))]
 
    # Generate a Fibonacci Series
    # Upto the Key Length
    while (m <= len(key)):
 
        # As it always starts with 1
        if (m == 0):
            m = 1
 
        else:
 
            # Logic For Fibonacci Series
            a = b
            b = c
            c = a + b
 
            for i in range(len(evenString)):
 
                # Caesar Cipher Algorithm Start
                # for even positions
                p = evenString[i]
                cip = 0
 
                if p in "1234567890":
                    cip = ord(p) + c
 
                    if (cip > ord('9')):
                        cip = cip - 9
 
                else:
                    cip = ord(p) + c
                    if (cip > ord('z')):
                        cip = cip - 26
 
                evenArray[i] = chr(cip)
 
                # Caesar Cipher Algorithm End
 
            for i in range(len(oddString)):
 
                # Caesar Cipher Algorithm
                # Start for odd positions
                p = oddString[i]
                cip = 0
 
                if p in "0123456789":
                    cip = ord(p) - c
                    if (cip < ord('0')):
                        cip = cip + 9
 
                else:
 
                    cip = ord(p) - c
                    if (cip < ord('a')):
 
                        cip = cip + 26
 
                oddArray[i] = chr(cip)
 
                # Caesar Cipher Algorithm End
            m += 1
 
    # Storing content of even and
    # odd array to the string array
    for i in range(len(stringArray)):
 
        if (i % 2 == 0):
 
            stringArray[i] = oddArray[k]
            k += 1
 
        else:
 
            stringArray[i] = evenArray[j]
            j += 1
 
    # Generating a Decrypted Text
    # by stringArray (Caesar Cipher)
    for d in stringArray:
        decrypted = decrypted + d
 
    # Return the Decrypted Text
    return decrypted[::-1]

# Driver code
cipher = input("Enter the ciphertext: ")
key = input("Enter the key: ")

print(decryptText(cipher))
