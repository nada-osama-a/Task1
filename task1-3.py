word = list(input()[::-1])
newword = str()
count = 0

for x in word[:] :
    if x == 'a': word[count] = '0'
    elif x == 'e': word[count] = '1'
    elif x == 'i': word[count] = '2'
    elif x == 'o': word[count] = '2'
    elif x == 'u': word[count] = '3'
    count += 1

word = word + ['a', 'c', 'a']

for x in word:
    newword += x
print('"' + newword + '"')
