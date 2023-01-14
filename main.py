import sys
import csv
import Donor

def main():
    fileName = sys.argv[1]
    if not fileName:
        print("Expecting csv file path as first argument")
        exit()

    with open(fileName, newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            print(row)

if __name__ == "__main__":
    main()