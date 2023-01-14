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

    def marshal(self, donationList):
        for value in donationList:
            if value['Account Name'] == self.AccountName:
                self.Donations.append(Donation(value['event'], value['checkdate'], value['donationdate'], value['checkamount'], value['donorname']))


class Donation():
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