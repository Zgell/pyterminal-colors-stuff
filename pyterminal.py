'''
==============================================================================
"PyTerminal" - By Zgell

A small Python library to make ANSI escape codes more accessible in Python
projects.
==============================================================================
'''

import sys

class Colours:
    '''
    The main class for changing text and background colours.
    '''
    def __init__(self):
        pass

    BLOCK0 = ''
    BLOCK1 = ''
    BLOCK2 = ''
    BLOCK3 = ''

    HEADER = '\033[95m'
    ENDC = '\033[0m'

    def Colour8Bit(n):
        print(n)

    def Colour8BitTest():


class Colors(Colours):
    '''
    A derivation of the Colours class for the American spelling.
    '''
    def __init__(self):
        super().__init__(self)
    def Color8Bit(n):
        #super(Colors, self).Colour8Bit(n)
        Colours.Colour8Bit(n)

def main():
    '''
    A default function to run when the file is run directly.
    Performs a couple of test operations to ensure all of the ANSI codes
    are functioning as intended and are supported on the user's system.
    '''
    print(Colors.HEADER + 'Header Text' + Colours.ENDC + ' Not Header Text')
    Colours.Colour8Bit(16)
    Colors.Color8Bit(32)
    pass

if __name__ == '__main__':
    main()

'''
References:
"Build your own Command Line with ANSI escape codes" - Haoyi's Programming 
Blog
https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html/
'''