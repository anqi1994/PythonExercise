class Portfolio:
    def __init__(self, name,):
        self.name = name
        self.stocks= []

    def buy_stock(self, stock):
        self.stocks.append(stock)

    def sell_stock(self, stock):
        self.stocks.remove(stock)


class Stock:
    def __init__(self, nam, amount, value):
        self.nam = nam
        self.amount = amount
        self.value = value

    def print(self):
        print(f"You have {self.amount}{self.nam} with value{self.value}.")


p = Portfolio("Kimmo's stocks")
s1 = Stock('Nokia', 100, 500)
s2 = Stock('Motorola', 200, 1000)
