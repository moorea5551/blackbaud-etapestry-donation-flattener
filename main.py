import sys
import csv
import Donor

def main():
    fileName = sys.argv[1]
    if not fileName:
        print("Expecting csv file path as first argument")
        exit()

    donations = []
    with open(fileName, newline='') as csvFile:
        reader = csv.DictReader(csvFile, delimiter=',')
        dictCsv = list(reader)

        for value in dictCsv:
            tempDonation = Donor.Donation(value['event'], value['checkdate'], value['donationdate'], value['checkamount'], value['donorname'])
            donations.append(tempDonation)

        print(donations)

if __name__ == "__main__":
    main()