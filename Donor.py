import datetime

class Donor:
    def __init__(self, donorName: str):
        self.DonorName = donorName
        self.Donations = []
        print("hello world")

class Donation():
    def __init__(self, event: str, checkDate: datetime, donationDate: datetime, checkAmount: float, donorName: str):
        self.Event = event
        self.CheckDate = checkDate
        self.DonationDate = donationDate
        self.CheckAmount = checkAmount
        self.DonorName = donorName