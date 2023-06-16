from sort import Sorter
from filetypes import filetypes

def main():
    while True:
        try:
            console = input("Enter directory:")
            sorter = Sorter(console,filetypes)
            sorter.sort_roms()
        except FileNotFoundError:
            print("No such file directory")
        except PermissionError:
            print("Premission Denied")

if __name__ == "__main__":
   main()
    