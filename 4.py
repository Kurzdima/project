import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import math


def start():
    df = pd.read_csv('SPFB_RTS_010305_210307.csv', sep=';')
    df2 = pd.read_csv("USDCB_010305_210307.csv", sep=',')
    i = 783
    d = 0
    pr = 166
    stop = 4400
    money_0_0 = 100000
    money_0 = money_0_0
    profit_min = money_0_0
    quantity = 0
    profit_plus = 0
    profit_minus = 0
    profit_zero = 0
    profit_plus_money = 0
    profit_minus_money = 0
    profit_max = 0
    profit = 0
    index_plus = 0
    index_minus = 0
    index_plus_max = 0
    index_minus_max = 0
    min_profit = 0
    j = 0
    a = 0
    b = 0
    c = 0
    dat = 0
    check = [money_0_0/1000]
    data = [dat]
    while True:
        try:
            date = str(df['DATE'][i])
        except:
            break
        year =  int(date[:4])
        month = int(date[4:-2])
        day = int(date[6:])
        ans = datetime.date(year, month, day)
        day_of_week = ans.weekday()
        while True:
            if df['DATE'][i] == df2['DATE'][j]:
                break
            elif df['DATE'][i] < df2['DATE'][j]:
                j = j -1
                break
            else:
                j = j + 1
        usd_bay = df2['OPEN'][j]
        while True:
            try:
                usd_sell = df2['OPEN'][j+d]
                break
            except:
                j = j - 1
        if day_of_week == 1:
            range_yesterday = df['HIGH'][i-1] - df['CLOSE'][i-1]
            if (df['OPEN'][i] + ((pr/100) * range_yesterday)) <= df['HIGH'][i]:
                quantity = quantity + 1
                r = 0
                while True:
                    if j+r > 5136 or i+r > 3904:
                        break
                    profit_close = (df['CLOSE'][i+r] - (df['OPEN'][i] + ((pr/100) * range_yesterday))) * df2['OPEN'][j+r] * 0.02
                    profit_low = (df['LOW'][i+r] - (df['OPEN'][i] + ((pr/100) * range_yesterday))) * df2['OPEN'][j+r] * 0.02

                    if profit_low < (0 - stop):
                        profit = (0 - stop)
                        break
                    elif profit_close > 0:
                        profit = profit_close
                        break
                    else:
                        r = r + 1
                if profit < min_profit:
                    min_profit = profit

                elif profit_max < profit:
                    profit_max = profit
                if profit_min > money_0 + profit:
                    profit_min = money_0 + profit
                if profit > 0:
                    profit_plus = profit_plus + 1
                    profit_plus_money = profit_plus_money + profit
                    index_plus = index_plus + 1
                    index_minus = 0
                    a = 0
                    b = 0
                    if index_plus > index_plus_max:
                        index_plus_max = index_plus
                elif profit < 0:
                    profit_minus = profit_minus + 1
                    profit_minus_money = profit_minus_money + profit
                    index_minus = index_minus + 1
                    index_plus = 0
                    if index_minus > index_minus_max:
                        index_minus_max = index_minus
                if profit < 0:
                    if a == 0:
                        b = profit
                        if b < c:
                            c = b
                    if a == 1:
                        b = b + profit
                        if b < c:
                            c = b
                    a = 1
                else:
                    profit_zero = profit_zero + 1
            
                money_0 = money_0 + profit

                money = money_0
                dat = dat + 1
                data.append(dat)
                check.append(money_0/1000)

        i = i + 1
        j = j + 1



    print('-------------Прорыв волотильности (max-close)-------------')
    print('Количество сделок: ', quantity)
    print('Количество прибыльных сделок: ', profit_plus)
    print('Процент прибыльных сделок: ', round(profit_plus / quantity *100, 1))
    print('Самый большой выигрыш за 1 сделку в рублях: ', round(profit_max, 2))
    print('Средний выигрыш в рублях: ', round(profit_plus_money / profit_plus, 2))
    print('Отношение среднего выиграша к среднему проигрышу: ', round((profit_plus_money / profit_plus)/(profit_minus_money / profit_minus), 4))
    print('Максимальное количество последовательных выигрышей: ', index_plus_max)
    print('Количество проигрышных сделок: ',profit_minus)
    print('Самый большой проигрыш за 1 сделку в рублях: ', round(min_profit, 2))
    print('Средний проигрыш в рублях: ', round(profit_minus_money / profit_minus, 2))
    print('Средний результат сделки в рублях: ', round((money - money_0_0) / quantity, 2))
    print('Максимальное количество последовательных проигрышей: ', index_minus_max)
    print('Максимальное проседание от начального счета: ', round(money_0_0 - profit_min, 2))
    print('Чистая прибыль: ', round(money - money_0_0, 2))
    print('Максимальное последовательное проседание: ', round(c, 2))
    print('----------------------------------')

    plt.plot(data, check)
    plt.legend()
    plt.grid(True)
    plt.show()

def start2():
    df = pd.read_csv('SPFB_RTS_010305_210307.csv', sep=';')
    df2 = pd.read_csv("USDCB_010305_210307.csv", sep=',')
    i = 783
    d = 0
    pr = 0.1
    stop = 3800
    money_0_0 = 100000
    money_0 = money_0_0
    profit_min = money_0_0
    quantity = 0
    profit_plus = 0
    profit_minus = 0
    profit_zero = 0
    profit_plus_money = 0
    profit_minus_money = 0
    profit_max = 0
    profit = 0
    index_plus = 0
    index_minus = 0
    index_plus_max = 0
    index_minus_max = 0
    min_profit = 0
    j = 0
    a = 0
    b = 0
    c = 0
    dat = 0
    check = [money_0_0/1000]
    data = [dat]
    while True:
        try:
            date = str(df['DATE'][i])
        except:
            break
        year =  int(date[:4])
        month = int(date[4:-2])
        day = int(date[6:])
        ans = datetime.date(year, month, day)
        day_of_week = ans.weekday()
        while True:
            if df['DATE'][i] == df2['DATE'][j]:
                break
            elif df['DATE'][i] < df2['DATE'][j]:
                j = j -1
                break
            else:
                j = j + 1
        usd_bay = df2['OPEN'][j]
        while True:
            try:
                usd_sell = df2['OPEN'][j+d]
                break
            except:
                j = j - 1
        if day_of_week == 1:
            range_yesterday1 = math.fabs(df['LOW'][i-1] - df['HIGH'][i-4])
            range_yesterday2 = math.fabs(df['HIGH'][i-2] - df['LOW'][i-4])
            if  range_yesterday1 >= range_yesterday2 :
                range_yesterday = range_yesterday1
            else:  range_yesterday = range_yesterday2
            if (df['OPEN'][i] + ((pr/100) * range_yesterday)) <= df['HIGH'][i]:
                quantity = quantity + 1
                r = 0
                while True:
                    if j+r > 5136 or i+r > 3904:
                        break
                    profit_close = (df['CLOSE'][i+r] - (df['OPEN'][i] + ((pr/100) * range_yesterday))) * df2['OPEN'][j+r] * 0.02
                    profit_low = (df['LOW'][i+r] - (df['OPEN'][i] + ((pr/100) * range_yesterday))) * df2['OPEN'][j+r] * 0.02

                    if profit_low < (0 - stop):
                        profit = (0 - stop)
                        break
                    elif profit_close > 0:
                        profit = profit_close
                        break
                    else:
                        r = r + 1
                if profit < min_profit:
                    min_profit = profit

                elif profit_max < profit:
                    profit_max = profit
                if profit_min > money_0 + profit:
                    profit_min = money_0 + profit
                if profit > 0:
                    profit_plus = profit_plus + 1
                    profit_plus_money = profit_plus_money + profit
                    index_plus = index_plus + 1
                    index_minus = 0
                    a = 0
                    b = 0
                    if index_plus > index_plus_max:
                        index_plus_max = index_plus
                elif profit < 0:
                    profit_minus = profit_minus + 1
                    profit_minus_money = profit_minus_money + profit
                    index_minus = index_minus + 1
                    index_plus = 0
                    if index_minus > index_minus_max:
                        index_minus_max = index_minus
                if profit < 0:
                    if a == 0:
                        b = profit
                        if b < c:
                            c = b
                    if a == 1:
                        b = b + profit
                        if b < c:
                            c = b
                    a = 1
                else:
                    profit_zero = profit_zero + 1
            
                money_0 = money_0 + profit

                money = money_0
                dat = dat + 1
                data.append(dat)
                check.append(money_0/1000)

        i = i + 1
        j = j + 1



    print('-------------Прорыв волотильности (3х дневная разница max-close)-------------')
    print('Количество сделок: ', quantity)
    print('Количество прибыльных сделок: ', profit_plus)
    print('Процент прибыльных сделок: ', round(profit_plus / quantity *100, 1))
    print('Самый большой выигрыш за 1 сделку в рублях: ', round(profit_max, 2))
    print('Средний выигрыш в рублях: ', round(profit_plus_money / profit_plus, 2))
    print('Отношение среднего выиграша к среднему проигрышу: ', round((profit_plus_money / profit_plus)/(profit_minus_money / profit_minus), 4))
    print('Максимальное количество последовательных выигрышей: ', index_plus_max)
    print('Количество проигрышных сделок: ',profit_minus)
    print('Самый большой проигрыш за 1 сделку в рублях: ', round(min_profit, 2))
    print('Средний проигрыш в рублях: ', round(profit_minus_money / profit_minus, 2))
    print('Средний результат сделки в рублях: ', round((money - money_0_0) / quantity, 2))
    print('Максимальное количество последовательных проигрышей: ', index_minus_max)
    print('Максимальное проседание от начального счета: ', round(money_0_0 - profit_min, 2))
    print('Чистая прибыль: ', round(money - money_0_0, 2))
    print('Максимальное последовательное проседание: ', round(c, 2))
    print('----------------------------------')

    plt.plot(data, check)
    plt.legend()
    plt.grid(True)
    plt.show()
                              


if __name__ == '__main__':
    #start()
    start2()
    print(' ')
    k = input('Нажмите любую кнопку для завершения программы')





