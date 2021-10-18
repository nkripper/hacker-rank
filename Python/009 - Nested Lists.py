if __name__ == '__main__':
    all_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_scores.append((name, score))

    all_scores.sort(key=lambda x: x[1])

    first_place = all_scores.pop(0)
    second_place = []

    for student in all_scores:
        if student[1] != first_place[1]:
            if len(second_place) == 0 or student[1] == second_place[0][1]:
                second_place.append(student)
            else:
                break

    second_place.sort()
    for student in second_place:
        print(student[0])