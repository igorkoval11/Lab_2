
"""
A1 — Типы и результаты выражений.
Выводит результат каждого выражения и тип результата.
"""
def show(expr_str, value):
    print(f"{expr_str:20s} -> {value!r:10s} | type: {type(value).__name__}")

if __name__ == "__main__":
    width = 17
    height = 12.0
    show("width//2", width // 2)     # 8, int
    show("width/2.0", width / 2.0)   # 8.5, float
    show("height/3", height / 3)     # 4.0, float
    show("1 + 2 * 5", 1 + 2 * 5)     # 11, int
