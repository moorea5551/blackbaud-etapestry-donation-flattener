import sys
import csv
import Donor

def main():
    fileName = sys.argv[1]
    if not fileName:
        print("Expecting csv file path as first argument")
        exit()

    donorNames = []
    donors = []
    with open(fileName, newline='') as csvFile:
        reader = csv.DictReader(csvFile, delimiter=',')
        dictCsv = list(reader)

        for value in dictCsv:
            if value['donorname'] not in donorNames:
                donorNames.append(value['donorname'])

        for value in donorNames:
            tempDonor = Donor.Donor(value)
            tempDonor.marshal(dictCsv)
            donors.append(tempDonor)

if __name__ == "__main__":
    main()