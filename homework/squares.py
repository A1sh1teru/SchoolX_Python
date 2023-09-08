def generate_squares(N: int) -> int:
    return [i ** 2 for i in range(-N, N+1)]
N = int(input())

result = generate_squares(N)

print(result)