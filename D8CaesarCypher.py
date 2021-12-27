alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(text, shift, direction):
    code_letter = ''
   
    if direction == 'encode':
       for i in text:
           if i in alphabet:
               position = alphabet.index(i)
               code_letter += alphabet[position + shift]
           else:
               code_letter += i
       print(f"\nthe {direction}d message is: {code_letter}")
     
    if direction == 'decode':
        for i in text:
           if i in alphabet:
               position = alphabet.index(i)
               code_letter += alphabet[position - shift]
           else:
               code_letter += i
        print(f"\nthe {direction}d message is: {code_letter}")

    
again = 'yes'    
while again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))   
    caesar(text, shift, direction)
    again = input('yes or no ')
 