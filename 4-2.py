key = 42
plaintext = "Phan Thi Bich Nhu"
plaintext = plaintext.upper()

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = ""

for ch in plaintext:
    if ch in char:
        position = char.index(ch)
        position_cipher = (position + key) % 26
        char_cipher = char[position_cipher]
        ciphertext = ciphertext + char_cipher
    else:
        ciphertext = ciphertext + ch

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
