# base64 encoding without using any in-built library

# defining the character set
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

print("WELCOME TO BASE64 TOOL !!")
print()

# function to take input string from user
def takeString():
    a = input("Enter the string you want to convert : ")
    print("Entered string is :", a)
    return a

# function to convert normal string to base64
def convertTobase64(a):
    # making binary form of each character
    b = ""
    for i in a:
        x = ord(i)              # get ASCII value
        y = bin(x)[2:]          # convert to binary (remove 0b)
        while len(y) < 8:       # make sure binary is 8 bits
            y = "0" + y
        b = b + y               # add to full binary string

    # add extra zeros if not multiple of 6
    while len(b) % 6 != 0:
        b = b + "0"

    # now take 6 bits at a time and find matching character
    ans = ""
    i = 0
    while i < len(b):
        s = b[i:i+6]            # take 6 bits
        num = int(s, 2)         # convert binary to number
        ans = ans + alpha[num]  # pick that index from alpha string
        i = i + 6

    # add '=' padding if needed
    if len(a) % 3 == 1:
        ans = ans + "=="
    elif len(a) % 3 == 2:
        ans = ans + "="

    print("Base64 Encoded string is:", ans)
