# Function for Encryption()
def encrypt(key, message):
    message = message.lower()   # lower fuction to change the message in lowerr case.
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""                 # store the result
    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result    #return back the result
# Function for Decryption()
def decrypt(key, message):
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result
def main():
    print("*****************************WELCOME*********************************")
    print()
    print("*****************MESSAGE ENCRYPTOR AND DECRYPTOR*********************")
    print()
    ch=input("Enterr your choice......'en' to encroyt and 'de' to decrypt...... ")  # ch=choice
    print()
    if(ch=='en' or ch=='En'):
       msg=input("Enter your message you want to encrypt.... ")                         # msg=message
       shift=int(input("Enter the shift key(0-25)..... "))         # this key shift the letters from there place and replace it by other letter 
       #encrypt() function is called
       en_msg = encrypt(shift,msg)                                                    # en_msg=encrypted message
       print("Your encrypted message is...... ", en_msg)
    elif(ch=='de' or ch=='De'):
       en_msg=input("Enter your encrypted messagee to decrypt it.... ")
       shift==int(input("Enter the shift key(0-25)..... "))
       #decrypt() function is called
       de_msg = decrypt(shift,en_msg)                                                 # de_msg=decrypted message
       print("Your decrypted message is...... ", de_msg) 
    print()
    print("**********************THANK YOU FOR YOUR VISIT***********************")

if __name__ == "__main__":
    main()