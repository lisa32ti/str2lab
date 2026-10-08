def tribonacci(n):
    # Base
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    # Recursive 
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


if __name__ == "__main__":
    print("n  | tribonacci(n)")
    print("-----------------")
    for i in range(11):
        print(f"{i:>2} | {tribonacci(i)}")