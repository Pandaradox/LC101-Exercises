# def alphabet_position(char):
#     import string
#     if char in string.ascii_uppercase:
#         return((string.ascii_uppercase).find(char))
#     elif char in string.ascii_lowercase:
#         return((string.ascii_lowercase).find(char))
#
#
# def rotate_character(char, rot):
#     import string
#     if char in string.ascii_uppercase:
#         return((string.ascii_uppercase)[(alphabet_position(char)+rot) % 26])
#     elif char in string.ascii_lowercase:
#         return((string.ascii_lowercase)[(alphabet_position(char)+rot) % 26])
#
#
# def encrypt(text, keyword):
#     keyword = keyword.lower()
#     l_alphabet = "abcdefghijklmnopqrstuvwxyz"
#     u_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     key = []
#     for k in keyword:
#         key += [l_alphabet.index(k)]
#
#     secret = ""
#     keypos = 0
#
#     for char in text:
#         if char.isalpha():
#             if char in l_alphabet:
#                 secret += rotate_character(char, key[keypos%len(key)])
#             elif char in u_alphabet:
#                 secret += rotate_character(char, key[keypos%len(key)])
#             keypos += 1
#         else:
#             secret += char
#     return(secret)
#
# def main():
#     text = input("Phrase? ")
#     key = input("Key? ")
#     print(encrypt(text, key))
#
#
# if __name__ == "__main__":
#     main()


# ########################################
def alphabet_position(char):
    import string
    if char in string.ascii_lowercase:
        return(string.ascii_lowercase.index(char))
    if char in string.ascii_uppercase:
        return(string.ascii_uppercase.index(char))
    return("error")


def rotate_character(char = 'a', rot = 13):
    import string
    if char in string.ascii_lowercase:
        return(string.ascii_lowercase[((alphabet_position(char)+rot)%26)])
    if char in string.ascii_uppercase:
        return(string.ascii_uppercase[((alphabet_position(char)+rot)%26)])
    else:
        return(char)

#
# def encrypt(text, rot = 13):
#     secret = ""
#     for char in text:
#         secret += rotate_character(char, rot)
#     return(secret)


def encrypt(text, keyword):
    key = []
    for k in keyword:
        key += [alphabet_position(k)]

    secret = ""
    keypos = 0

    for char in text:
        if char.isalpha():
            secret += rotate_character(char, key[keypos % len(key)])
            keypos += 1
        else:
            secret += char

    return(secret)


def main():
    text = input("Text to translate? ")
    keyword = input("Key?")
    print(encrypt(text, keyword))

if __name__ == "__main__":
    main()
