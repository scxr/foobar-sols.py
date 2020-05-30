import base64

#The encrypted key
message='GFQEHA8QCh1AFRZZU1AOHhYOGhQeFkQQGAUAFg4JRlcRQ0lXTgkAGwtWX1MHVFtJSxYJCFxAQhBU V1NMVAYAUEBTBxoVBQlUQ04UU1ULGhIfCR4KAEcVFllTUBwCHwANWFdSRF9XTh4SDQxaRkVEU01J SwAOCFYVGkNUEQYDVE9UExVBCh1WThE='

#Your Google username
key='cswilson326'

decrypted_message=[]

#decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

#XOR with Username
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

#The encypted message
print("".join(decrypted_message))
