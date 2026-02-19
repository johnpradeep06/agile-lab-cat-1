def encrypt(text, shift=3):
    """Simple Caesar Cipher encryption."""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
#version 1
def decrypt(text, shift=3):
    return encrypt(text, -shift)
