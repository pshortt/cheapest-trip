class Trip():
    def __init__(self, dep, ret, price):
        self.dep = dep
        self.ret = ret
        self.price = price
        
    def __str__(self):
        return 'depart: {}, return: {}, price: {}'.format(self.dep, self.ret, self.price)
# (depart flight price, return flight price) on a given day
flights =[(100,200),(150,196),(120,218),(135,172),(250,217),(239,214),(196,126),(224,154),(159,188),(138,189)]
triplength = 5
trips = []

for i,t in enumerate(flights[:-triplength]):
    trips.append(Trip(i, i+triplength, flights[i][0] + flights[i+triplength][1]))
    print(trips[i])
    
