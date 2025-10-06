"""
A4 — Вывести большее из двух целых чисел без условных операторов.
Вход: две строки с целыми A и B (1..1000)
Выход: одно число — max(A, B)
Пример:
Ввод:
7
3
Вывод:
7
"""
def solve(a: int, b: int) -> int:
    return (a + b + abs(a - b)) // 2

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    a, b = map(int, data[:2])
    print(solve(a, b))
