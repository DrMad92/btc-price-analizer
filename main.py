import urllib.request
import datetime
import argparse
import csv

defaultName = "data/btc-marketprice-" + str(datetime.date.today()) + ".csv"
days = []
values = []


def main(filename):
    if filename is None:
        filename = defaultName
        try:
            urllib.request.urlretrieve("https://api.blockchain.info/charts/market-price?format=csv",
                                       filename)  # Python 3
            with open(filename) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    days.append(row[0])
                    values.append(row[1])
        except Exception as e:
            print(e)
            print('Exiting')
            exit()
    else:
        try:
            with open(filename) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    days.append(row[0])
                    values.append(row[1])
        except Exception as e:
            print(e)
            print('Exiting')
            exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shows info about BTC market based on csv file')
    parser.add_argument('-f', dest='filename', help='path to a file')
    args = parser.parse_args()
    main(args.filename)
