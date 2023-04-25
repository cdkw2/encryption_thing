import base64

def encrypt_link(link):
    encoded_bytes = base64.b64encode(link.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

link = input("Enter the string: ")
encrypted_link = encrypt_link(link)
print(encrypted_link)

