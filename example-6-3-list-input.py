
# Run and test
# python example-6-3-list-input.py < colors_input.txt

#reads colors from the user and appends to a list
#until the user presses the Enter key.
def main():
  colors = []
  #notice how we read one time outside the loop
  #check and then enter the loop
  aColor = input("Enter a color: ")
  while (aColor != ''):
    colors.append(aColor)
    aColor = input("Enter a color: ")

  # print(colors)
  
  # print("If you want it formatted better: ")
  # printColors(colors)

  printOneColumn(colors)


def printColors(colors):
  for num in range(len(colors)-1):
    print(colors[num], ", ", sep = '', end = '')
  print(colors[num+1])

# ANSI color codes
COLOR_MAP = {
  'red': '\033[91m',
  'orange': '\033[38;5;208m',
  'yellow': '\033[93m',
  'green': '\033[92m',
  'blue': '\033[94m',
  'indigo': '\033[38;5;39m',
  'violet': '\033[35m',
  'pink': '\033[95m',
  'brown': '\033[38;5;94m',
  'black': '\033[90m',
  'white': '\033[97m',
  'gray': '\033[37m',
  'cyan': '\033[96m',
  'magenta': '\033[35m',
  'teal': '\033[36m',
  'navy': '\033[38;5;18m',
  'olive': '\033[38;5;58m',
  'maroon': '\033[38;5;124m',
  'lavender': '\033[38;5;183m',
  'peach': '\033[38;5;215m',
}
RESET = '\033[0m'
DEFAULT_COLOR = '\033[37m'  # Default to white/default terminal color

def printOneColumn(colors):
  for color in colors:
    color_lower = color.lower()
    color_code = COLOR_MAP.get(color_lower, DEFAULT_COLOR)
    
    # Inform user if color is not in the map
    if color_lower not in COLOR_MAP:
      print(f"(Color '{color}' not found in map - using default)", file=__import__('sys').stderr)
    
    print(f"{color_code}{color.capitalize()}{RESET}")


#call main
main()
