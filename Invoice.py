class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products)-self.totalDiscount(products)
        return total_pure_price

    def totalSalesTax(self, products):  # Calculates NC Sales Tax after discounts
        total_sales_tax = self.totalPurePrice(products) * .0475  # Sales tax of 4.75% calculated
        total_sales_tax = int(total_sales_tax * 100) / 100  # Contribution in rounding
        total_sales_tax = round(total_sales_tax, 2)  # Round to two decimals
        return total_sales_tax  # Returns sales tax calculated with pure price

    def totalPurePriceWithTax(self, products):  # Calculates NC Sales Tax added to pure price
        total_pure_price_with_tax = self.totalPurePrice(products) + self.totalSalesTax(products)  # Adds Sales Tax to Pure Price
        return total_pure_price_with_tax  # Returns total price including sales tax

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

