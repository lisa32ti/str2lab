def recursive_poly(word):
    if len(word) <= 1:
        return "YES"
    if word[0] != word[-1]:
        return "NO"
    return recursive_poly(word[1:-1])


if __name__ == "__main__":
    tests = ["level", "radar", "hello", "abba", "a", "", "abcba", "abca"]
    print(f"{'word':>10} | result")
    print("-" * 20)
    for t in tests:
        print(f"{t!r:>10} | {recursive_poly(t)}")