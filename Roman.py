__author__ = 'zacharymelby'
romanlst = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
declst = [1000, 500, 100, 50, 10, 5, 1]


def roman(num):
    '''
    This function will take in one positive integer number and returns the number in Roman
    Numerals(as a string).
    '''
    final = ''
    if num > 0:
        if num >= 1000:
            final = 'M' + roman(num - 1000)
            return final
        elif num  >= 900:
            final = 'CM' + roman(num - 900)
            return final
        elif num >= 500:
            final = 'D' + roman(num - 500)
            return final
        elif num >= 400:
            final = 'CD' + roman(num - 400)
            return final
        elif num >= 100:
            final = 'C' + roman(num - 100)
            return final
        elif num >= 90:
            final = 'XC' + roman(num - 90)
            return final
        elif num >= 50:
            final = 'L' + roman(num - 50)
            return final
        elif num >= 40:
            final = 'XL' + roman(num - 40)
            return final
        elif num >= 10:
            final = 'X' + roman(num - 10)
            return final
        elif num >= 9:
            final = 'IX' + roman(num - 9)
            return final
        elif num >= 5:
            final = 'V' + roman(num - 5)
            return final
        elif num >= 4:
            final = 'IV' + roman(num - 4)
            return final
        elif num >= 1:
            final = 'I' + roman(num - 1)
            return final
    else:
        return final




def main():
    n = int(input('Enter a number to convert: '))
    rom = roman(n)
    print(rom)

main()