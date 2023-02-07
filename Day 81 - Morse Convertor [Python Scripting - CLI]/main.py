from playsound import playsound
from time import sleep

MORSE_CIPHER = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.','G':'--.', 'H':'....','I':'..', 'J':'.---', 
                'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---',
                'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 
                'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', 
                '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                '0':'-----', " ": "/"
                }
MORSE_CIPHER_DECRYPT = {code: key for key, code in MORSE_CIPHER.items()}

action = input("Encyrpt(E) or Decrypt(D)? \n")

def encrypt(encrypted_msg):
    print(encrypted_msg)
    for beep in encrypted_msg: 
        if beep == '.':
            playsound("audios/short-tone.mp3")
        elif beep == '-':
            playsound("audios/long-tone.mp3")
        else:
            sleep(0.5)

if action == 'e'or action == 'E':
    msg = input("Enter message to Encrypt: ")
    encrypted_msg = " ".join(MORSE_CIPHER[char] for char in msg.upper())
    encrypt(encrypted_msg)
elif action == 'd' or action == 'D':
    secret = input("Enter secret message to Decrypt: ")
    decoded_msg = " ".join(MORSE_CIPHER_DECRYPT[key] for key in secret.split(" "))
    print(decoded_msg)
else:
    print("Invalid action. There are literelly two actions. Try again.")