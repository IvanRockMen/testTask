from pycbrf.toolbox import ExchangeRates
import datetime
from decimal import Decimal

# valut start and valut and writes like RUB or EUR
def get_valute_pair(valut_start: str, valute_end: str)-> Decimal:
    now = datetime.datetime.now()

    rates = ExchangeRates(now.strftime("%Y-%m-%d"))

    if(valut_start != "RUB"):
        valut_start_in_ruble = rates[valut_start].value / rates[valut_start].par
        valut_end_in_ruble = rates[valute_end].value / rates[valute_end].par
        print(valut_start_in_ruble)
        print(valut_end_in_ruble)
        return valut_end_in_ruble/valut_start_in_ruble
    else:
        return rates[valute_end].value / rates[valute_end].par

if __name__ == "__main__":
    print(get_valute_pair("EUR", "KZT"))


