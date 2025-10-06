"""
A6 — По данному N (секунды с начала суток) вывести время h:mm:ss.
h без ведущего нуля, минуты/секунды — с ведущим нулём (2 цифры).
Пример:
Ввод: 3602
Вывод: 1:00:02
"""
def solve(n: int) -> str:
    h = (n // 3600) % 24
    m = (n % 3600) // 60
    s = n % 60
    return f"{h}:{m:02d}:{s:02d}"

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.read().strip())
    print(solve(n))
