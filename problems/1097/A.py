def solve(table_card, five_cards):
    rank, suit = table_card[0], table_card[1]
    for c in five_cards:
        if c[0] in rank or c[1] in suit:
            return "YES"
    return 'NO'


if __name__ == '__main__':
    table_card = input()
    five_cards = list(input().split())
    res = solve(table_card, five_cards)
    print(res)