import random

def open_file(filename: str) -> list:
    with open(filename) as file:
        contents = file.read() #contents now gives us access to the file
        #print(contents)
        file.close()

    return contents

def clean_text(filename: str) -> list:
    clean = open_file(filename).strip()

    return clean

def create_list(filename: str) -> list:
    res = list()

    res.append(open_file(filename).splitlines())

    return res

def gen_length() -> int:
    res = input("How many words?: ")

    return int(res)

def gen_sentence(filename) -> str:

    res = list()
    names = create_list(filename) # list ((entry1, entry2)) list inside of a list with 1 index of 0
    index = names[0][-1]
    last_index = names[0].index(index)

    for _ in range(gen_length()):

        rand_index = random.randrange(0, last_index -1)
        res.append(names[0][rand_index])

    return res


def run():
    print("run: \n")

    print(gen_sentence("test.txt"))

def main():
    print("Begin main: ")

    run()

if __name__ == '__main__':
    main()