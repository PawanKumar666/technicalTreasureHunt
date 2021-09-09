#Importing what you need will surely help you
import key
import turtle

a=('Use','Correct','Syntax','Please')

# We Prefer Strings over Numbers

b = "01000011 01101111 01101110 01100111 01110010 01100001 01110100 01110011 00100000 01000010 01110101 01110100 00100000 01110100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01101110 01101111 01110100 00100000 01110100 01101000 01100101 00100000 01101011 01100101 01111001"

c = "01000100 01101111 00100000 01010111 01101000 01100001 01110100 00100000 01101000 01100001 01110011 00100000 01100010 01100101 01100101 01101110 00100000 01110100 01101111 01101100 01100100 00100000 01101001 01101110 00100000 01100110 01101001 01110010 01110011 01110100 00100000 01101100 01101001 01101110 01100101"

val = b.split()

val1 = c.split()

msg =""

msg1 = ""

for i in val :
    
    inte = int(i,2)
    
    achr = chr(inte)
    
    msg += achr

for i in val1 :
    
    inte1 = int(i,2)
    
    achr1 = chr(inte1)
    
    msg1 += achr1
    
turtle. color('black')

style = ('Arial', 30, 'italic')

#Note : Overwriting is Useless bro

turtle. write(msg, font=style, align='center')

#turtle. write(msg1, font=style, align='center')

turtle. hideturtle()
