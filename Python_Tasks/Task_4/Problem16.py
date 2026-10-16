# Problem Name: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

def sort_students(names_scores):
    grades = sorted(set(score for name, score in names_scores))
    second_lowest = grades[1]

    names = sorted(name for name, score in names_scores if score == second_lowest)

    for name in names:
        print(name)


if __name__ == '__main__':
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name, score])

    sort_students(names_scores)
