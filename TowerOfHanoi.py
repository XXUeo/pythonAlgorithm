def printMove(fr,terget):
    print('move from ' + str(fr) + 'to ' + str(terget))


def Towers(n, fr, terget, space):
    if n == 1:
        printMove(fr, terget)
    else:
        Towers(n-1,fr,space,terget)
        Towers(n,fr,terget,space)
        Towers(n-1,fr,space,terget)
