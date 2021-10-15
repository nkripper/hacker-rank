if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    race_results = list(arr)
    race_results.sort(reverse=True)

    first_place = race_results.pop(0)

    for player in race_results:
        if player != first_place:
            break

    print(player)