# Collatz Conjecture
# by:xxbr
#2022年4月10日

def bingbaocaixiang(n):
    #冰雹猜想
    print(n)
    if n > 1:
        if n % 2 == 0:
            bingbaocaixiang(n // 2)
        else:
            bingbaocaixiang(3 * n + 1)

def main():
    #输入数字
    n = int(input("请输入一个数字："))
    bingbaocaixiang(n)


if __name__ == '__main__':
    main()
