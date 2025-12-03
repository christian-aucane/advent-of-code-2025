from pathlib import Path


def rotate(value, count, rot):
    n = int(rot[1:-1])
    rotation = -1 if rot[0] == "L" else +1
    for _ in range(n):
        value += rotation
        if rot[0] == "L" and value == -1:
            value = 99
        elif rot[0] == "R" and value == 100:
            value = 0
        if value == 0:
            count += 1
    return value, count


def main():
    day_dir = Path(__file__).parent
    with open(day_dir / "input.txt") as f:
        rotations = f.readlines()
    count = 0
    value = 50
    for rot in rotations:

        value, count = rotate(value, count, rot)

    print(count)


def test():
    day_dir = Path(__file__).parent
    with open(day_dir / "test.txt") as f:
        rotations = f.readlines()
    count = 0
    value = 50
    for rot in rotations:
        value, count = rotate(value, count, rot)
        print(f"rot = {rot[:-1]} | value = {value} | count = {count}")
    print(count)


if __name__ == "__main__":
    main()
    # print("rotate 52 R48 : ", rotate(52, "R48"))
    test()
