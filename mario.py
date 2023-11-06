
def main():
    height = get_height()
    for row in range(height):
        space = height - row - 1
        hash = row + 1
        print(space * " ", hash * "#", " ", hash * "#", space * " ", sep="")
        


def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height < 9:
                break
        except ValueError:
            print("Not an integer")

    return height

main()