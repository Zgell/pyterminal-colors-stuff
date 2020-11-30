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
    The main class for changing text colours.
    '''
    def __init__(self):
        pass

    # Block characters
    BLOCK0 = '\u2591'  # Emptiest block
    BLOCK1 = '\u2592'  # Semi-empty block
    BLOCK2 = '\u2593'  # Semi-full block
    BLOCK3 = '\u2588'  # Fullest block

    # 4-bit ANSI codes (should be supported by most terminals)
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = LIGHTGRAY = LIGHTGREY = '\033[37m'
    GRAY = GREY = BLACK2 = '\033[90m'
    BRIGHTRED = RED2 = FAIL = ERROR = '\033[91m'
    BRIGHTGREEN = GREEN2 = OKGREEN = '\033[92m'
    BRIGHTYELLOW = YELLOW2 = WARNING = '\033[93m'
    BRIGHTBLUE = BLUE2 = OKBLUE = '\033[94m'
    BRIGHTMAGENTA = MAGENTA2 = HEADER = '\033[95m'
    BRIGHTCYAN = CYAN2 = OKCYAN = '\033[96m'
    BRIGHTWHITE = WHITE2 = '\033[97m'

    ENDC = RESET = '\033[0m'
    #BOLD = '\033[1m'
    #UNDERLINE = '\033[4m'

    def text8(n):
        '''
        From ANSI escape code wiki:
        0-7: Standard colours
        8-15: High intensity colours
        16-231: 6x6x6 cube (216 colours): 16 + 36 x r + 6 x g + b
        (0 <= r, g, b <= 5)
        232-255: grayscale from black to white in 24 steps
        '''
        return ('\u001b[38;5;' + str(n) + 'm')

    def back8(n):
        '''
        Same idea as "text8", but for background colour
        '''
        return ('\u001b[48;5;' + str(n) + 'm')

    def Colour8BitTest():
        '''
        Example adapted from resources (1)
        '''
        # [NOTE]: Adapt this from O(n^2) to O(n) in the future

        for i in range(0, 16):
            for j in range(0, 16):
                string = str(16 * i + j)
                # Coloured Background Test
                sys.stdout.write("\u001b[48;5;" + string + 'm ' + ' ')
            print("\u001b[0m")  # Reset formatting and end of each line


class Format:
    '''
    The main class used for handling text formatting.
    '''

    def __init__(self):
        pass

    BOLD = '\033[1m'
    FAINT = DIM = '\033[2m'
    ITALIC = SLANT = SLANTED = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = SLOW_BLINK = '\033[5m'
    FAST_BLINK = '\033[6m'  # Very rarely supported according to wikipedia
    REVERSE = INVERT = '\033[7m'  # Also rarely works
    CONCEAL = HIDE = '\033[8m'  # Again, rarely works
    CROSSED_OUT = STRIKETHROUGH = MARKED = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    OVERLINE = '\033[53m'


class Colors(Colours):
    '''
    A derivation of the Colours class for the American spelling.
    '''
    def __init__(self):
        super().__init__(self)

    def Color8Bit(n):
        #super(Colors, self).Colour8Bit(n)
        Colours.Colour8Bit(n)

def SGR(text, start, end):
    for i in range(start, end+1):
        print(str(i) + ': ' + '\033[' + str(i) + 'm ' + text + '\033[0m')

def main():
    '''
    A default function to run when the file is run directly.
    Performs a couple of test operations to ensure all of the ANSI codes
    are functioning as intended and are supported on the user's system.
    '''
    Colours.Colour8BitTest()
    SGR('Sample text sentence.', 1, 74)
    pass

if __name__ == '__main__':
    main()

'''
References:

[1] "Build your own Command Line with ANSI escape codes" 
Haoyi's Programming Blog
https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html/
'''