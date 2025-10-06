
def show(expr_str, value):
    print(f"{expr_str:20s} -> {value!r:10s} | type: {type(value).__name__}")

if __name__ == "__main__":
    width = 17
    height = 12.0
    show("width//2", width // 2)     
    show("width/2.0", width / 2.0)   
    show("height/3", height / 3)   
    show("1 + 2 * 5", 1 + 2 * 5)

