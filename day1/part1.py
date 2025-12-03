from pathlib import Path


def rotate(value, rot):
    n = int(rot[1:-1])
    rotation = -1 if rot[0] == "L" else +1
    value += n * rotation
    return value % 100


def main():
    day_dir = Path(__file__).parent
    with open(day_dir / "input.txt") as f:
        rotations = f.readlines()
    count = 0
    value = 50
    for rot in rotations:
        value = rotate(value, rot)
        if value == 0:
            count += 1
    print(count)


def test():
    day_dir = Path(__file__).parent
    with open(day_dir / "test.txt") as f:
        rotations = f.readlines()
    count = 0
    value = 50
    for rot in rotations:
        value = rotate(value, rot)
        if value == 0:
            count += 1
        print(f"rot = {rot[:-1]} | value = {value} | count = {count}")

    print(count)


if __name__ == "__main__":
    main()
    # print("rotate 52 R48 : ", rotate(52, "R48"))
    test()
