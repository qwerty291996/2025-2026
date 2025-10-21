print("Kiritilish tartibi har bir son probel bilan  x1,y1,x2,y2")
x1,y1,x2,y2=map(int,input().split())
def ot_harakati(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        return True
    else:
        return False
if ot_harakati(x1, y1, x2, y2):
    print("Ot bir yurishda bu maydondan o‘tishi mumkin.")
else:
    print("Ot bir yurishda bu maydondan o‘tishi mumkin emas.")
