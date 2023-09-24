import math


class Insurance:# {{{
    def __init__(self, *, deductible, premium, coinsurance_percent=10,
                 coinsurance_cap=700, maximum_insured=math.inf):
        self._deduct = deductible
        self._premium = premium
        self._coins_percent = coinsurance_percent
        self._coins_cap = coinsurance_cap
        self._max = maximum_insured

    def cost(self, expenses):
        premium = self._premium * 12
        if expenses < self._deduct:
            return round(premium + expenses)
        deduct = self._deduct
        expenses -= deduct
        coins = expenses * self._coins_percent / 100
        if coins > self._coins_cap:
            coins = self._coins_cap
        return round(premium + deduct + coins)
# }}}


def average(iterable):# {{{
    return round(sum(iterable) / len(iterable))
# }}}


if __name__ == '__main__':
    health_300 = Insurance(deductible=300, premium=360.4)
    health_2500 = Insurance(deductible=2500, premium=232.1)

    expenses_list = (500, 1000, 2000, 2500, 3000, 4000, 6000, 9000, 15000)
    cost_300_list = tuple(health_300.cost(e) for e in expenses_list)
    cost_2500_list = tuple(health_2500.cost(e) for e in expenses_list)

    fmt = '{:>10}   {:>10}   {:>10}'
    print(fmt.format('Expenses', '300 CHF', '2500 CHF'))
    for expenses, cost_300, cost_2500 in zip(expenses_list, cost_300_list,
                                             cost_2500_list):
        print(fmt.format(expenses, cost_300, cost_2500))
    print('{:^36}'.format('=== Average ==='))
    print(fmt.format(average(expenses_list), average(cost_300_list),
                     average(cost_2500_list)))
