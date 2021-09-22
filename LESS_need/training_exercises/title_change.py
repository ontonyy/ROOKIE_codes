# Take a book title in file, and change it to first upper letter and phrase length

with open("books.txt", "r+") as file:  # File opening and changing titles
    first = file.readlines()


    def title_chan(first):
        while len(first) != 0:
            bt = str(first[0])
            mod_bt = [bt[0].upper(), len(bt) - bt.count(" ")]
            for x in mod_bt:
                print(x, end="")
            print("")
            first.pop(0)
            title_chan(first)

if __name__ == '__main__':
    title_chan(first)
