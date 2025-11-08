# Base64 Encoder

This is a simple program that takes a string input from the user and converts it into Base64 encoding (without using any built-in libraries)

## How It Works ?

1. Converts each character to its ASCII value
2. Turns ASCII values into binary (8 bits each)
3. Joins all bits and splits them into 6-bit chunks
4. Maps each 6-bit chunk to a Base64 character
5. Adds `=` padding if needed

## Example - 
Input - "Hi"
Output - 'SGK='
