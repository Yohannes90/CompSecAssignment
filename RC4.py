def ksa(key):
    """
    Key Scheduling Algorithm (KSA)
    """
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
    return S

def prga(S):
    """
    Pseudo-Random Generation Algorithm (PRGA)
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4(key, data):
    """
    RC4 encryption/decryption
    """
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    return bytes([c ^ next(keystream) for c in data])

# Example usage
key = input("Please Enter key: ")
plaintext = input("Please Enter plaintext: ")

# Convert plaintext to bytes
plaintext_bytes = plaintext.encode()
print("Convert plaintext to bytes . . . . . . . ")
print("Plaintext in bytes:", plaintext_bytes, '\n')

# Encrypt
ciphertext = rc4(key, plaintext_bytes)
print("Encrypting to ciphertext . . . . . . . . ")
print("Ciphertext:", ciphertext, '\n')

key = input("Please Enter key for decreption(NB: RC4 is symmetric): ")
# Decrypt (RC4 is symmetric)
decrypted = rc4(key, ciphertext)
print("Decrypting to plaintext . . . . . . . . ")
print("Decrypted:", decrypted.decode())
