import requests

currencies = ["EUR", "USD", "CNY"]


# def picker():
#     pick = input("Pick currencies")
#     return pick


Cur_dict = [
    {
        "CNY": {"to_eur": "0.13", "to_usd": "0.14", "to_gryvna": "5.5"},
        "USD": {"to_cny": "7.35", "to_eur": "0.93", "to_gryvna": "36.7"},
        "EUR": {"to_usd": "1.07", "to_cny": "7.85", "to_gryvna": "38.3"},
    }
]


class CurrentData:
    # @property
    def curr_getter(self, cur):
        link = (
            f"https://bank.gov.ua/NBUStatService/v1/statdirectory/"
            f"exchange?json&valcode={cur}&date=20230101"
        )
        try:
            res = requests.request("GET", link)
            print(res.json())
        except Exception as e:
            print(e)
        else:
            return Price(
                res.json()[0]["rate"], res.json()[0]["cc"], int(input("how many?"))
            )


Currency = CurrentData()


class Price:
    def __init__(self, rate: int, currency: str, amount: int) -> None:
        self.rate: int = rate
        self.currency: str = currency
        self.amount = amount
        self.sum_to_grivna = int(self.rate) * int(amount)

    def __str__(self):
        return (
            f"here is the currency you "
            f"looked for: {self.amount} {self.currency}, {self.rate}"
        )

    def __add__(self, other):
        if self.currency == other.currency:
            return self.sum_to_grivna + other.sum_to_grivna
        else:
            if self.currency != "USD":
                if self.currency == "CNY":
                    """
                    Hardcode_option
                    """
                    if other.currency == "EUR":
                        return (
                            self.amount * float(Cur_dict[0]["CNY"]["to_usd"])
                            + (other.amount * float(Cur_dict[0]["EUR"]["to_usd"]))
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
                    elif other.currency == "USD":
                        return (
                            self.amount * float(Cur_dict[0]["CNY"]["to_usd"])
                            + (other.amount)
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
                elif self.currency == "EUR":
                    if other.currency == "CNY":
                        return (
                            (self.amount * float(Cur_dict[0]["EUR"]["to_usd"]))
                            + (other.amount * float(Cur_dict[0]["CNY"]["to_usd"]))
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
                    elif other.currency == "USD":
                        return (self.amount * float(Cur_dict[0]["EUR"]["to_usd"])) + (
                            other.amount
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])

            else:
                """Dymanic option"""
                return f"{self.currency} to {other.currency} exchange rate is: {self.amount * (self.rate / other.rate)}"

    def __sub__(self, other):
        if self.currency == other.currency:
            return self.sum_to_grivna - other.sum_to_grivna
        else:
            if self.currency != "USD":
                if self.currency == "CNY":
                    """
                    Hardcode_option
                    """
                    if other.currency == "EUR":
                        return (
                            self.amount * float(Cur_dict[0]["CNY"]["to_usd"])
                            - (other.amount * float(Cur_dict[0]["EUR"]["to_usd"]))
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
                    elif other.currency == "USD":
                        return (
                            self.amount * float(Cur_dict[0]["CNY"]["to_usd"])
                            - (other.amount)
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
                elif self.currency == "EUR":
                    if other.currency == "CNY":
                        return (
                            (self.amount * float(Cur_dict[0]["EUR"]["to_usd"]))
                            - (other.amount * float(Cur_dict[0]["CNY"]["to_usd"]))
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
                    elif other.currency == "USD":
                        return (self.amount * float(Cur_dict[0]["EUR"]["to_usd"])) - (
                            other.amount
                        ) * float(Cur_dict[0]["USD"]["to_gryvna"])
            else:
                """Dymanic option"""
                return (
                    f"{self.currency} to {other.currency} exchange "
                    f"rate is: {(self.rate / other.rate)},"
                    f"you will get -> {self.amount * (self.rate / other.rate)} for {self.amount}{self.currency}"
                )


while True:
    try:
        res = Currency.curr_getter(input("Pick currencies"))
        res2 = Currency.curr_getter(input("Pick currencies"))
        print(res, res2)
        print(res + res2)
        print("______________________________________________________________")
        print(res - res2)

    except Exception as e:
        print(e)
        break
    finally:
        break
