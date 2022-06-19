from datetime import datetime

class Transaction():

    def __init__(self, id, desc, amount, location):
        self.id = id
        self.desc = desc
        self.amount = amount
        self.location = location
        self.purchase_time = datetime.now()
    
    def to_dict(self):
        dict = {'id': self.id, 'desc': self.desc, 'amount': self.amount, 'location': self.location, 'purchase_time': self.purchase_time}
        return dict