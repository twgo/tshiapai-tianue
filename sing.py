from random import choice
sooji = ['ling5', 'it4', 'ji7', 'sam1', 'su3',
         'ngoo2', 'liok8', 'tshit4', 'pat4', 'kiu2']
for _ in range(100):
    pai = []
    for _ in range(3):
        pai.append(
            choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        )
    for _ in range(4):
        pai.append(
            choice(sooji)
        )
    print(' '.join(pai))

for _ in range(100):
    ue = ['ling5',  'kiu2']
    for _ in range(8):
        ue.append(
            choice(sooji)
        )
    print(' '.join(ue))
