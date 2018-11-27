from calculator import *

if __name__ == '__main__':
    expressions = ["+34", "+3-15", "*+34-23", "+7++34+23",
    "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    [calculator(expr).print_reduction() for expr in expressions]
