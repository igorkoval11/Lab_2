"""
A7 — Проверить, одинаковый ли цвет двух клеток шахматной доски.
(1,1) — белая. Если одинаковый — вывести 'YES' и затем цвет ('White'/'Black'),
иначе — 'NO'.
Вход: x1, y1, x2, y2 (по одному числу на строку)
"""
def same_color(x1: int, y1: int, x2: int, y2: int):
    same = (x1 + y1 + x2 + y2) % 2 == 0
    if same:
        color = "White" if (x1 + y1) % 2 == 0 else "Black"
        return True, color
    return False, None

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    x1, y1, x2, y2 = map(int, data[:4])
    ok, color = same_color(x1, y1, x2, y2)
    if ok:
        print("YES")
        print(color)
    else:
        print("NO")
