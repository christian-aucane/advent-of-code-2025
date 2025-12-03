from pathlib import Path


def main():
    path = Path(__file__).parent / "input.txt"
    with open(path) as f:
        line = f.readline()
    ranges = line.split(",")
    result = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for val in range(start, end + 1):
            str_val = str(val)
            lenght = len(str_val)
            if (lenght % 2 == 0):
                center = lenght // 2
                if str_val[:center] == str_val[center:]:
                    result += val
    print(result)


def test():
    path = Path(__file__).parent / "test.txt"
    with open(path) as f:
        line = f.readline()
    print(f"line = {line}")
    ranges = line.split(",")
    result = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for val in range(start, end + 1):
            str_val = str(val)
            lenght = len(str_val)
            if (lenght % 2 == 0):
                center = lenght // 2
                if str_val[:center] == str_val[center:]:
                    result += val
    print(result)


if __name__ == "__main__":
    main()
    test()
