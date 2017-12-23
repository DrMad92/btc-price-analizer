import urllib.request
import datetime
import argparse

defaultName = "data/btc-marketprice-" + str(datetime.date.today()) + ".csv"


def main(filename=defaultName):
    print("Hi from main: " + filename)
    #urllib.request.urlretrieve("https://api.blockchain.info/charts/market-price?format=csv", filename)  # Python 3


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shows info about BTC market based on csv file')
    parser.add_argument('-f', dest='filename', help='path to a file')
    args = parser.parse_args()
    if args.filename is not None:
        main(args.filename)
    else:
        main()
