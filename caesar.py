import argparse
import sys


def doCaesar(text, shifts, alphabet):
    result = ""
    alphabet_len = len(alphabet)
    if len(set(alphabet)) != alphabet_len:
        print("Error: the given alphabet has duplicate letters")
        sys.exit(1)
    alphabet_map = {char: i for i, char in enumerate(alphabet)}
    for char in text:
        if char in alphabet_map:
            original_index = alphabet_map[char]
            new_index = (original_index + shifts) % alphabet_len
            result += alphabet[new_index]
        else:
            result += char
    return result


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str)
    parser.add_argument("-k", "--key", type=str)
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("-d", "--decrypt", action="store_true")
    return parser


def readInputs(input, key):
    with open(input) as inputf, open(key) as keyf:
        shifts = int(keyf.readline())
        alphabet = keyf.readline()
        text = inputf.read()
        return dict(text=text, shifts=shifts, alphabet=alphabet)


def writeToFile(text, filename):
    with open(filename, "w") as outputf:
        outputf.write(text)


def main():
    parser = argParser()
    args = parser.parse_args()
    if not (args.input and args.key):
        parser.print_help()
        sys.exit(1)

    text, shifts, alphabet = readInputs(args.input, args.key).values()
    if args.decrypt:
        shifts = -shifts
    output = doCaesar(text, shifts, alphabet)
    print(f"IN:\t{text}\nOUT:\t{output}\nKEY:\t{shifts} -> {alphabet}")
    writeToFile(output, args.output or "output.txt")


if __name__ == "__main__":
    main()
