class Bill:
    """
    Object for the bill to be saved with parameters amount and period of the bill
    """

    def __init__(self, amount, period) -> object:
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat has a name and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        return round(
            (bill.amount * (int(self.days_in_house) / (int(flatmate.days_in_house) + int(self.days_in_house)))), 2)