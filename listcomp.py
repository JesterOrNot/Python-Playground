initial = [[1, 3, 5, 3, 1, 2, 4, 5, 99, 8, 83, 32],
           [2, 3, 4, 5, 42, 2, 2, 4, 2, 4, 2, 2]]
evens = [j for i in initial for j in i if j % 2 == 0]


def fizz_buzz():
    return ["FizzBuzz" if i % 15 == 0 else
            "Fizz" if i % 3 == 0 else
            "Buzz" if i % 5 == 0 else i
            for i in range(1, 101)]


if __name__ == "__main__":
    [print(i) for i in fizz_buzz()]
