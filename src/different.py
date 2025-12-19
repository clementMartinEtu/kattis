#https://open.kattis.com/problems/different

def solve(input_str):
    """
    Computes the absolute differences between pairs of integers
    from a string, where each pair is separated by a comma.

    Args:
        input_str (str): Input string with each line separated by ','.
                         Each line contains two integers separated by space.

    Returns:
        list[int]: List of absolute differences.
    """
    results = []

    lines = input_str.split(',')

    for line in lines:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        a, b = map(int, line.split())
        results.append(abs(a - b))

    return results


# Example usage
input_str = "5 2, 100 100, 0 50"
differences = solve(input_str)