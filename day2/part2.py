from pathlib import Path

def run(input_path):
    with open(input_path) as f:
        line = f.readline()
    ranges = line.split(",")
    result = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for val in range(start, end + 1):
            str_val = str(val)
            lenght = len(str_val)
            for i in range(1, lenght // 2 + 1):
                if lenght % i != 0:
                    continue
                part = str_val[:i]
                if part * (lenght // i) == str_val:
                    result += val
                    break
    print(result)

 
def main():
    path = Path(__file__).parent / "input.txt"
    run(path)


def test():
    path = Path(__file__).parent / "test.txt"
    run(path)


if __name__ == "__main__":
    main()
    test()
