def main(g1, g2, typ):
    cnt1_g1, cnt1_g2 = int(g1[0]), int(g2[0])
    cnt2_g1, cnt2_g2 = int(g1[2]), int(g2[2])

    if typ == 1:
        res = (cnt2_g2 + cnt2_g1) - cnt1_g2 - cnt1_g1
        if res < 0:
            return 0

        elif res == 0:
            if cnt1_g2 > cnt2_g1:
                return 0
            return 1

        if cnt1_g2 + res > cnt2_g1:
            return res
        return res + 1

    res = (cnt2_g2 + cnt2_g1) - cnt1_g2 - cnt1_g1
    if res < 0:
        return 0

    elif res == 0:
        if cnt1_g1 > cnt2_g2:
            return 0
        return 1

    if cnt1_g1 > cnt2_g2:
        return res
    return res + 1

if __name__ == "__main__":
    g1 = input()
    g2 = input()
    typ = int(input())
    print(main(g1, g2, typ))
