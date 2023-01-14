import datetime

class Donor:
    def __init__(self, donorName: str):
        self.AccountName = donorName
        self.FirstName = None
        self.LastName = None
        self.MiddleName = None
        self.ShortSalutation = None
        self.EnvelopeSalutationLine1 = None
        self.EnvelopeSalutationLine2 = None
        self.AddressLine1 = None
        self.AddressLine2 = None
        self.City = None
        self.StateProvince = None
        self.PostalCode = None
        self.AccountType = None
        self.PersonaType = None

        self.Donations = []

        self.FlatCheckDate = ""
        self.FlatCheckAmount = ""
        self.FlatCheckNumber = ""
        self.FlatDate = ""
        self.FlatDesignation = ""

    def marshal(self, donationList):
        for value in donationList:
            tempDonation = Donation()
            if value['Account Name'] == self.AccountName:
                for key in value:
                    # Pop donor object
                    if key == "First Name":
                        self.FirstName = value[key]
                    elif key == "Last Name":
                        self.LastName = value[key]
                    elif key == "Middle Name":
                        self.MiddleName = value[key]
                    elif key == "Short Salutation":
                        self.ShortSalutation = value[key]
                    elif key == "Envelope Salutation Line 1":
                        self.EnvelopeSalutationLine1 = value[key]
                    elif key == "Envelope Salutation Line 2":
                        self.EnvelopeSalutationLine2 = value[key]
                    elif key == "Address Line 1":
                        self.AddressLine1 = value[key]
                    elif key == "Address Line 2":
                        self.AddressLine2 = value[key]
                    elif key == "City":
                        self.City = value[key]
                    elif key == "State/Province":
                        self.StateProvince = value[key]
                    elif key == "Postal Code":
                        self.PostalCode = value[key]
                    elif key == "Account Type":
                        self.AccountType = value[key]
                    elif key == "Persona Type":
                        self.PersonaType = value[key]

                    # Create and pop donation
                    if key == "Date":
                        tempDonation.Date = value[key]
                    elif key == "Type":
                        tempDonation.Type = value[key]
                    elif key == "Pledged":
                        tempDonation.Pledged = value[key]
                    elif key == "Received":
                        tempDonation.Received = value[key]
                    elif key == "Fund":
                        tempDonation.AdditionalGiftType = value[key]
                    elif key == "Approach":
                        tempDonation.Approach = value[key]
                    elif key == "Campaign":
                        tempDonation.Campaign = value[key]
                    elif key == "Check Date":
                        tempDonation.CheckDate = value[key]
                    elif key == "Check Number":
                        tempDonation.CheckNumber = value[key]
                    elif key == "Creation Date (Journal)":
                        tempDonation.CreationDateJournal = value[key]
                    elif key == "Designation":
                        tempDonation.Designation = value[key]
                    elif key == "Gift in Kind Sale Value":
                        tempDonation.GiftInKindSaleValue = value[key]
                    elif key == "Gift Type":
                        tempDonation.GiftType = value[key]
                    elif key == "Gift Type Note":
                        tempDonation.GiftTypeNote = value[key]
                    elif key == "Linked Soft Credit Account Name":
                        tempDonation.LinkedSoftCreditAccountName = value[key]
                    elif key == "Linked Soft Credit Amount":
                        tempDonation.LinkedSoftCreditAmount = value[key]
                    elif key == "Note":
                        tempDonation.Note = value[key]
                    elif key == "Soft Credit Amount":
                        tempDonation.SoftCreditAmount = value[key]
                    elif key == "Transaction Type":
                        tempDonation.TransactionType = value[key]
                    elif key == "Tribute":
                        tempDonation.Tribute = value[key]
                    elif key == "Acknowledged":
                        tempDonation.Acknowledged = value[key]
                    elif key == "Tribute Type":
                        tempDonation.TributeType = value[key]
                    
                self.Donations.append(tempDonation)

    def flatten(self):
        for donation in self.Donations:
            self.FlatCheckDate += str(donation.CheckDate) + ", "
            self.FlatCheckAmount += str(donation.Received) + ", "
            self.FlatCheckNumber += str(donation.CheckNumber) + ", "
            self.FlatDate += str(donation.Date) + ", "
            self.FlatDesignation += str(donation.Designation) + ", "

    def cleanup(self):
        self.FlatCheckAmount = self.FlatCheckAmount[:-2]
        self.FlatCheckDate = self.FlatCheckDate[:-2]
        self.FlatCheckNumber = self.FlatCheckNumber[:-2]
        self.FlatDate = self.FlatDate[:-2]
        self.FlatDesignation = self.FlatDesignation[:-2]

    def __iter__(self):
        return iter([self.AccountName, self.FirstName, self.LastName, self.MiddleName, self.ShortSalutation, self.EnvelopeSalutationLine1, self.EnvelopeSalutationLine2, self.AddressLine1, self.AddressLine2, self.City, self.StateProvince, self.PostalCode, self.AccountType, self.PersonaType, self.FlatCheckDate, self.FlatCheckAmount, self.FlatCheckNumber, self.FlatDate, self.FlatDesignation])
                    

class Donation:
    def __init__(self):
        self.Date = None
        self.Type = None
        self.Pledged = None
        self.Received = None
        self.Fund = None
        self.AdditionalGiftType = None
        self.Approach = None
        self.Campaign = None
        self.CheckDate = None
        self.CheckNumber = None
        self.CreationDateJournal = None
        self.Designation = None
        self.GiftInKindSaleValue = None
        self.GiftType = None
        self.GiftTypeNote = None
        self.LinkedSoftCreditAccountName = None
        self.LinkedSoftCreditAmount = None
        self.Note = None
        self.SoftCreditAmount = None
        self.TransactionType = None
        self.Tribute = None
        self.Acknowledged = None
        self.TributeType = None