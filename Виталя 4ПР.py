def main(n):
    if n == 0:
        return 0.21
    return main(n-1)**3 / 76 + ((main(n-1)**3 / 44) + 65 / 41)
