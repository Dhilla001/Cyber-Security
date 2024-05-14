import base64


def encrypt(passw):
    enc_pass = base64.b64encode(passw.encode())
    print(f'Encrypted password: {enc_pass}')


password = input("enter your password: ")
encrypt(password)
