class Mobile:
    _mob_price = 12323
    _mob_color = "Black"
    _mob_model = "J2342"
    _mob_company = "Nokia"

class Nokia(Mobile):
    def show(self):
        print(self._mob_price)
        print(self._mob_color)
        print(self._mob_model)
        print(self._mob_company)

obj = Nokia()
obj.show()