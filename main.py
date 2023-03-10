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
            if value['Account Name'] not in donorNames and value['Account Name'] is not "Anonymous":
                donorNames.append(value['Account Name'])

        for value in donorNames:
            tempDonor = Donor.Donor(value)
            tempDonor.marshal(dictCsv)
            tempDonor.flatten()
            tempDonor.cleanup()
            donors.append(tempDonor)

    with open("output.csv", 'w') as output:
        fieldnames = donors[0].__dict__.keys()
        writer = csv.DictWriter(output, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for donor in donors:
            writer.writerow(donor.__dict__)


if __name__ == "__main__":
    main()