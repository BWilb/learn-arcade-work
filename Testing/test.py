def calculate_gdp(c, i , g, e, im):
    gdp = c + i + g + (e - im)
    return gdp

def main():
    consume = int(input("Mr. president, how much did your citizens spend this quarter?"))
    invest = int(input("How much investment went into businesses?"))
    government = int(input("how much did the government spend?"))
    exports = int(input("how much did the united states export?"))
    imports = int(input("what is the total amount of imports"))

    calculate_gdp(consume, invest, government, exports, imports)
    print(calculate_gdp(consume, invest, government, exports, imports))
main()