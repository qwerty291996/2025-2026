def ot_yura_oladimi(x1, y1, x2, y2):
    if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
        return False
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print(ot_yura_oladimi(x1, y1, x2, y2))
