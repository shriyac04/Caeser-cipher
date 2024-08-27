first_char_code = ord("A")
last_char_code = ord("Z")
char_range = last_char_code - first_char_code + 1


def caesar_shift(message, shift):
    # Result placeholder.
    result = ""

    # Go through each of the letters in the message.
    for char in message.upper():
        if char.isalpha():
            # Convert character to the ASCII code.
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > last_char_code:
                new_char_code -= char_range

            if new_char_code < first_char_code:
                new_char_code += char_range

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result


user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift Key (integer): "))
cipher_text = caesar_shift(user_message, user_shift_key)
print(f"Cipher Text: {cipher_text}")
