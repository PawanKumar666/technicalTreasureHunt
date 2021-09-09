#################################################################################################

                            #Instructions :

#-> The first person to solve the code and show us the correct key wins! (Key is the hidden answer in the code)

#-> Methods of solving other than debugging the code is not allowed !

#-> Those who claim to have found the key has to run the code and show us the answer !

#-> You have to clear out the logical and syntactical errors in the code to get the desired key !

#-> Follow the hints given to debug !

#-> Dialogue of a hero will be the key here!

#-> All the best, make yourselves the first to solve !


#################################################################################################


#Hint : Strings will help defeat your "FOE" here !
                                      #<--

a={True: 01000010 01101000 01100001 01110010 01100111 01100001 01110110 00100000 01110010 01101111 01101101 01100010 01100001 00100000 01101101 01101111 01110011 01100001 01101101 01100001 01101110 01100001 01110110 01100001 01101110 00100000 01100100 01100001 01110111 00100001,
   1: 01000101 01101100 01101100 01100001 01101101 00100000 01110000 01100001 01110100 01101000 01110101 01101011 01101111 01101110 01100111 01100001 00101100 01001110 01100001 01100001 01101110 01110101 01101101 00100000 01110010 01101111 01110111 01100100 01111001 00100000 01100100 01101000 01100001 01100001 01101110 00100001,
   1.0: 01010100 01101000 01100001 01101101 01100010 01101001 00100000 01110100 01100101 01100001 00100000 01101001 01101110 01110101 01101101 00100000 01110110 01100001 01110010 01101100 01100001 00100001}
  
 
#Hint : Different Locks Cant have the same key!


value = a.get(True)

 
listOfValue = value.split()

 
decodedString = ""


if len(a.keys()) > int('0X1',16):
    
    for i in listOfValue :
    
        intValue = int(i,2)
    
        decodedElement = chr(intValue)
    
        decodedString += decodedElement
        
        
else:
    
    print('You are halfway through !');

 
print(decodedString)
