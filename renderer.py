x0=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x1=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x2=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x3=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x4=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x5=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

class InvalidCoordinate(BaseException):
    pass


def render_screen():
    toberend=''
    for char in x0:
        toberend+=char
    toberend+='\n'
    for char in x1:
        toberend+=char
    toberend+='\n'
    for char in x2:
        toberend+=char
    toberend+='\n'
    for char in x3:
        toberend+=char
    toberend+='\n'
    for char in x4:
        toberend+=char
    toberend+='\n'
    for char in x5:
        toberend+=char
    return toberend

def set_chars(towrite=[]):
    """chars must be in form x,y,char in a tuple"""
    for charset in towrite:
        if charset[0]==0:
            x0[charset[1]]=charset[2]
        elif charset[0]==1:
            x1[charset[1]]=charset[2]
        elif charset[0]==2:
            x2[charset[1]]=charset[2]
        elif charset[0]==3:
            x3[charset[1]]=charset[2]
        elif charset[0]==4:
            x4[charset[1]]=charset[2]

        elif charset[0]==5:
            x5[charset[1]-1]=charset[2]

            
def ResetMatrice():
    global x0
    global x1
    global x2
    global x3
    global x4
    global x5
    x0=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    x1=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    x2=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    x3=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    x4=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    x5=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
