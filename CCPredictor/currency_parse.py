
def getNames():
    concl = []
    for I in open('currency file', 'r')[1:]:
        I.split(',')
        string = I[0][1:-1]
        if string not in concl: concl += string
    return concl

if __name__ == '__main__':
    getNames()