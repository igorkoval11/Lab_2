"""
A5 — Проверить, делится ли A на B нацело.
Вход: A, B (целые, на отдельных строках)
Выход: 'YES' если A % B == 0, иначе 'NO'
"""
def solve(a: int, b: int) -> str:
    return "YES" if a % b == 0 else "NO"

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    a, b = map(int, data[:2])
    print(solve(a, b))
