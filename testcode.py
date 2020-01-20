import codecs
def get_args():
    args = []
    args.append(input("Enter platform (e.g.; Facebook)> "))
    args.append(input("Enter first name> "))
    args.append(input("Enter last name> "))
    args.append(input("Enter Birth Year> "))
    args.append(input("Enter Birth Month> "))
    args.append(input("Enter Birth Date> "))     
    l337 = input("Enter (y) for l337_mode, (n) to continue naive version> ")
    if l337 == 'y':
        l337 = "y"
    else:
        l337 = "n"

    file_name = input("Enter the name of the wordlist to be saved as> : ")
    return args, l337, file_name


def l337_m0d3(answers):
    leet = []
    for x in answers:
        leet.append(x.replace('a', '@'))
        leet.append(x.replace('A', '4'))
        leet.append(x.replace('e', '3'))
        leet.append(x.replace('E', '3'))
        leet.append(x.replace('i', '1'))
        leet.append(x.replace('I', '1'))        
        leet.append(x.replace('o', '0'))
        leet.append(x.replace('O', '0'))
        leet.append(x.replace('t', '7'))
        leet.append(x.replace('T', '7'))
        leet.append(x.replace('s', '$'))
        leet.append(x.replace('S', '$'))
        leet.append(x.replace('h', '#'))
        leet.append(x.replace('H', '#'))
        leet.append(x.replace('B', '|3'))
        
    final  = answers + leet
    return final    


def generate(args, file_name,):
    with open(file_name, 'w') as wordlist:
        for x in args:
            wordlist.write(x + '\n')
            wordlist.write(x.lower() + '\n')
            wordlist.write(x.upper() + '\n')
            for y in args:
                wordlist.write(x.lower() + y + '\n')
                wordlist.write(x.upper() + y + '\n')
                wordlist.write(x.upper() + y.lower() + '\n')
                wordlist.write(x.lower() + y.lower() + '\n')
                wordlist.write(x.lower() + y.upper() + '\n')
                wordlist.write(x.upper() + y.upper() + '\n')

    lines = open(file_name, 'r').readlines()
    lines_set = set(lines)
    out  = open(file_name, 'w')
    for line in lines_set:
        out.write(line)


def main():
    (args, l337, file_name) = get_args()
    if l337 == "y":
        args = l337_m0d3(args)
    generate(args, file_name)    
    print("Wordlist generated as " + "\033[91m"+ file_name  + "\033[0m")

if __name__ == "__main__":
    main()