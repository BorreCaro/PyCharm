while (a := input()) != "0":
    a = int(a)
    transactions = [int(x) for x in input().split()]
    positives = [a for a in transactions if a >= 0]
    negatives = [a for a in transactions if a <= 0]
    d = 0 if not positives else max(positives)
    w = 0 if not negatives else min(negatives)
    r = 0
    left = 0

    while left < a:
        countD = 0
        countW = 0
        for i in range(left, a):
            if transactions[i] > 0:
                countD += 1
            elif transactions[i] < 0:
                countW += 1
            if countD == countW:
                r = max(i - left + 1, r)
        left += 1
    print(f"{d} {w} {r}")