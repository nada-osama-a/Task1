#Another solution just in case we're not allowed to use the bin() built in function.

hexa = input()
binary = str()
for x in hexa[2:]:
    if x == '0': binary += '0000'
    elif x == '1': binary += '0001'
    elif x == '2': binary += '0010'
    elif x == '3': binary += '0011'
    elif x == '4': binary += '0100'
    elif x == '5': binary += '0101'
    elif x == '6': binary += '0110'
    elif x == '7': binary += '0111'
    elif x == '8': binary += '1000'
    elif x == '9': binary += '1001'
    elif x == 'A': binary += '1010'
    elif x == 'B': binary += '1011'
    elif x == 'C': binary += '1100'
    elif x == 'D': binary += '1101'
    elif x == 'E': binary += '1110'
    elif x == 'F': binary += '1111'

print('"' + binary + '"')
