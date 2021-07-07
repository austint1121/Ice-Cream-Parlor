def what_flavors(cost, money):
    matches = {}
    indexs = {}
    for x, flavors_cost in enumerate(cost, 1):
        if flavors_cost < money:
            matches[money - flavors_cost] = flavors_cost
            if not indexs.get(flavors_cost, False):
                indexs[flavors_cost] = x
            else:
                if flavors_cost + flavors_cost == money:
                    print(indexs[matches.get(flavors_cost)], x)
        if matches.get(flavors_cost, False) and indexs[matches.get(flavors_cost)] != indexs[flavors_cost]:
            print(indexs[matches.get(flavors_cost)], indexs[flavors_cost])
            break

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        what_flavors(cost, money)
