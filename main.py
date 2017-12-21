import urllib.request
import datetime
import argparse


def main():
    print("Hi from main")
    filename = "data/btc-marketprice-" + str(datetime.date.today()) + ".csv"
    urllib.request.urlretrieve("https://api.blockchain.info/charts/market-price?format=csv", filename)  # Python 3


if __name__ == "__main__":
    main()
