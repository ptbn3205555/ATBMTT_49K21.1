plaintext = "Phan Thi Bich Nhu"
k = 42 % 26  
ceasartext = ""

for p in plaintext:
    if p.isalpha():
        if p.isupper():
            start = ord('A')
            new_char = chr((ord(p) - start + k) % 26 + start)
        else:
            start = ord('a')
            new_char = chr((ord(p) - start + k) % 26 + start)
        ceasartext += new_char
    else:
        ceasartext += p

print("Plaintext:", plaintext)
print("Ceasartext:", ceasartext)
