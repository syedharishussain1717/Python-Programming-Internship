# Name: Syed Haris Hussain Shah
# Internship ID: B9_2265
# PYTHON INTERNSHIP TASK 1

import timeit

def generate_fibonacci(n):
    """Generate a Fibonacci sequence containing n terms."""

    # Validate input
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    sequence = []

    first = 0
    second = 1

    for i in range(n):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def test_fibonacci():
    """Test normal and invalid inputs."""

    test_cases = [10, 5, 1, 0]

    for n in test_cases:
        print(f"Fibonacci({n}):", generate_fibonacci(n))

    # Test invalid inputs
    invalid_cases = [-5, 2.5, "10"]

    for value in invalid_cases:
        try:
            print(generate_fibonacci(value))
        except (TypeError, ValueError) as error:
            print(f"Input {value}: {error}")


def benchmark_fibonacci():
    """Measure the execution time of the function."""

    execution_time = timeit.timeit(
        lambda: generate_fibonacci(1000),
        number=1000
    )

    print("\nBenchmark Results")
    print("Execution time:", execution_time, "seconds")


if __name__ == "__main__":
    print("Fibonacci Generation Module\n")

    test_fibonacci()
    benchmark_fibonacci()

