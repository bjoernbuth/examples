def bubble_sort(data: list[int]) -> list[int]:
    print(f"Data before sorting: {data}")
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def do_operations(data: list[int]) -> None:
    # multiply each element by 2
    data = [item * 2 for item in data]

    # add 10 to each element
    data = [item + 10 for item in data]

    result = bubble_sort(data)

    print(f"Result after sorting: {result}")


def main() -> None:
    data = [1, 5, 3, 4, 2]
    do_operations(data)


if __name__ == "__main__":
    main()
