import base64

def encrypt(passw):
    enc_pass = base64.b64encode(passw.encode())
    print(enc_pass)

password = input("enter your password: ")
encrypt(password)
