tic = []
tac = []
toe = []

for i in range(3):
    tic.append(input())

for j in range(3):
    tac.append(input())

for k in range(3):
    toe.append(input())

print(tic)
print(tac)
print(toe)

if tic[0]==tic[1]==tic[2]: print(tic[0]) #rows
elif tac[0]==tac[1]==tac[2]: print(tac[0])
elif toe[0]==toe[1]==toe[2]: print(toe[0])

elif tic[0]==tac[0]==toe[0]: print(tic[0]) #columns
elif tic[1]==tac[1]==toe[1]: print(tic[1])
elif tic[2]==tac[2]==toe[2]: print(tic[2])

elif tic[0]==tac[1]==toe[2]: print(tic[0]) #both diagonals
elif tic[2]==tac[1]==toe[0]: print(tic[2])
else: print("Draw")

