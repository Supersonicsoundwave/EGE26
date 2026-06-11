with open(r'.\files\26_17643.txt') as file:
    N = int(file.readline())
    goods = dict()
    for line in file:
        art, price, data = map(int, line.split())
        if art not in goods:
            goods[art] = [not data, price, data]
        else:
            old_sold, price, old_left = goods[art]
            goods[art] = [old_sold + (not data), price, old_left + data]

mid_price = sum(val[1] for val in goods.values()) / len(goods)
pricey = [good for good in goods.values() if good[1] > mid_price]

pricey.sort(key=lambda x: (-x[0], -x[1], x[2]))

leader = pricey[0]
print(leader[0] * leader[1], leader[2])
