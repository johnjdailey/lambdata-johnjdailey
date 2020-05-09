# class.py


class Stocks():
    def __init__(self, Date, Open, High, Low, Close, Adj_Close, Volume):
        self.Date = Date
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Close = Close
        self.Adj_Close = Adj_Close
        self.Volume = Volume

    def buyStock(self):
        print("Buying", self.Stock)

    def sellStock(self):
        print("Selling", self.Stock)


class Cryptos(Stocks):
    def __init__(self, Date, Open, High, Low, Close, Adj_Close, Volume):
        super().__init__(Date, Open, High, Low, Close, Adj_Close, Volume)

    def buyCrypto(self):
        print("Buying peer to peer")

    def sellCrypto(self):
        print("Selling peer to peer")


if __name__ == "__main__":
    GOLD = Stocks("May 08, 2020", 27.44, 27.89, 27.24, 27.39, 27.39, 12732300)
    print(GOLD.High, GOLD.Low)
    GOLD.buyStock()
    GOLD.sellStock()

    GLD = Stocks("May 08, 2020", 161.08, 162.00, 160.00, 160.42, 160.42, 12240900) 
    print(GLD.High, GLD.Low)
    GLD.buyStock()
    GLD.sellStock()

    BTC = Cryptos("May 09, 2020", 9820.80, 9908.81, 9796.45, 9802.95, 9802.95, 47370928128)
    print(BTC.High, BTC.Low)
    BTC.buyCrypto()
    BTC.sellCrypto()

    LTC = Cryptos("May 09, 2020", 47.65, 48.85, 47.65, 48.81, 48.81, 4828417024)
    print(LTC.High, LTC.Low)
    LTC.buyCrypto()
    LTC.sellCrypto()
