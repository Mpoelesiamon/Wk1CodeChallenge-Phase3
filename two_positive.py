def two_positive(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    is_exactly_two_positive = positive_count == 2
    print(f"Exactly two numbers are positive: {is_exactly_two_positive}")
    return is_exactly_two_positive

# Example usage
two_positive(2, 4, -3)
