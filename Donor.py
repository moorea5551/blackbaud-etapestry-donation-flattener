import datetime

class Donor:
    def __init__(self, donorName: str):
        self.DonorName = donorName
        self.Donations = []

    def marshal(self, donationList):
        for value in donationList:
            if value['donorname'] == self.DonorName:
                self.Donations.append(Donation(value['event'], value['checkdate'], value['donationdate'], value['checkamount'], value['donorname']))


class Donation():
    def __init__(self, event: str, checkDate: datetime, donationDate: datetime, checkAmount: float, donorName: str):
        self.Event = event
        self.CheckDate = checkDate
        self.DonationDate = donationDate
        self.CheckAmount = checkAmount
        self.DonorName = donorName