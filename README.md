# btc-price-analyzer
Hometask for Advanced Python course at TalTech.

BTC price analyzer

The script takes CSV file and tells the user the following information:

* What was the greatest percent increase over the previous day, and what day was it?
* What was the greatest percent decrease over the previous day, and what day was it?
* What is the highest price in the the data, and what day was it?


## Usage
```
main.py [-h] [-f FILENAME]
```
By default the script downloads this [CSV file](https://blockchain.info/charts/market-price):
```
python main.py
```
The script can be run with external csv file by passing path to a file in a command line:
```
python main.py -f example.csv
```
For help:
```
python main.py -h
```
## Test
`test.py` tests functions in `main.py` with known values and invalid inputs such as **infinity**, **NaN**, **string** and **None**.

To run unittest:
```
python test.py
```
More detailed test report use `-v`:
```
python test.py -v
```
For help:
```
python test.py -h
```
## Requirements
See `requirements.txt`

Script works on both Python 2 and 3.

Tested with 2.7 and 3.6.

