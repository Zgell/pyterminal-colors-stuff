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

    BLOCK0 = '\u2591'  # Emptiest block
    BLOCK1 = '\u2592'  # Semi-empty block
    BLOCK2 = '\u2593'  # Semi-full block
    BLOCK3 = '\u2588'  # Fullest block

    HEADER = '\033[95m'
    ENDC = '\033[0m'

    def Colour8Bit(n):
        print(n)

    def Colour8BitTest():
        '''
        Example adapted from resources (1)
        '''
        # [NOTE]: Adapt this from O(n^2) to O(n) in the future

        for i in range(0, 16):
            for j in range(0, 16):
                string = str(16 * i + j)
                #sys.stdout.write("\u001b[38;5;"+string+'m '+string.ljust(4))
                # Coloured Background Test
                sys.stdout.write("\u001b[48;5;" + string + 'm ' + ' ') #+ string.ljust(4))
            print("\u001b[0m")  # Reset formatting and end of each line


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
    #print(Colors.HEADER + 'Header Text' + Colours.ENDC + ' Not Header Text')
    Colours.Colour8BitTest()
    pass

if __name__ == '__main__':
    main()

'''
References:

[1] "Build your own Command Line with ANSI escape codes" 
Haoyi's Programming Blog
https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html/
'''