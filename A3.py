# A3.py
"""
A3 — Перевести 1_921_000 байт в мегабайты (1 MB = 1024 * 1024).
Вывод: число в МБ с точностью до 2 знаков.
"""
BYTES = 1_921_000

def to_mb(n_bytes: int) -> float:
    return n_bytes / (1024 * 1024)

if __name__ == "__main__":
    print(f"{to_mb(BYTES):.2f} MB")  # 1.83 MB
