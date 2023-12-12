def find_coeffs(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    return a, b, c
a, b, c = find_coeffs(3, 2, 5, 7)
print("Коефіцієнти:", a, b, c)

def equation_string(a, b, c):
    a_str = f"{a}x" if a >= 0 else f"- {-a}x"
    b_str = f"+ {b}y" if b >= 0 else f"- {-b}y"
    return f"{a_str} {b_str} = {c}"
equation = equation_string(a, b, c)
print("Рівняння прямої:", equation)
