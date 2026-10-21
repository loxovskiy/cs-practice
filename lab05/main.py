
from tablestats import *

with open('events.csv', mode='r', encoding='utf-8', newline='') as f:

    print(read_rows(f))

from tablestats import *


def main():

    with open(input(), encoding="utf-8") as table:

        rows = read_rows(table)

    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))

    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

if __name__ == "__main__":
    main()