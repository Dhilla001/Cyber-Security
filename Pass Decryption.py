import base64


def decrypt(passw):
    dec_data = base64.b64decode(passw)
    dec_pass = dec_data.decode()
    print(f"Original password: {dec_pass}")


password = input("enter the encrypted password: ")
decrypt(password)
