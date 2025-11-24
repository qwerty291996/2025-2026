def baholash(baho):
    if 0 <= baho <= 54:
        return "Qoniqarsiz"
    elif 55 <= baho <= 70:
        return "Qoniqarli"
    elif 71 <= baho <= 85:
        return "Yaxshi"
    elif 86 <= baho <= 100:
        return "A’lo"
    else:
        return "Noto‘g‘ri baho!"

baholar = [45, 67, 82, 95]
for b in baholar:
    print(b, "->", baholash(b))
