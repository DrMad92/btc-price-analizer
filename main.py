import urllib.request
import datetime
import argparse
import csv
from collections import namedtuple

defaultName = "data/btc-marketprice-" + str(datetime.date.today()) + ".csv"
days = []
values = []
Point = namedtuple('Point', ['day', 'value'])


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
                    values.append(float(row[1]))
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

    raw_data = list(zip(days, values))
    data = [Point(day=day, value=value) for day, value in raw_data]

    result = greatest_increase(data)
    print('\nBiggest percent increase: ', result[0])
    print('Day: ', result[1])

    result = greatest_decrease(data)
    print('\nBiggest percent decrease: ', result[0])
    print('Day: ', result[1])

    result = highest_price(data)
    print('\nHighest price: ', result[0])
    print('Day: ', result[1])


def greatest_increase(data):
    biggest_change = 0
    day_of_biggest_change = None

    for i in range(len(data) - 1):
        previous = data[i].value
        current = data[i + 1].value
        if current > previous:
            change = current * 100 / previous
            change = change - 100
            if change >= biggest_change:
                biggest_change = change
                day_of_biggest_change = data[i + 1].day
        else:
            continue

    return biggest_change, day_of_biggest_change


def greatest_decrease(data):
    biggest_change = 0
    day_of_biggest_change = None

    for i in range(len(data) - 1):
        previous = data[i].value
        current = data[i + 1].value
        if current < previous:
            change = current * 100 / previous
            change = 100 - change
            if change >= biggest_change:
                biggest_change = change
                day_of_biggest_change = data[i + 1].day
        else:
            continue

    return biggest_change, day_of_biggest_change


def highest_price(data):
    max_price = 0
    day_of_max_price = None

    for data_point in data:
        if max_price <= data_point.value:
            max_price = data_point.value
            day_of_max_price = data_point.day

    return max_price, day_of_max_price


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shows info about BTC price changes from csv file')
    parser.add_argument('-f', dest='filename', help='path to a file')
    args = parser.parse_args()
    main(args.filename)
