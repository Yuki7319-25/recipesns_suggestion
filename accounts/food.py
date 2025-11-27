# accounts/food.py

# 基本クラス
class Itiran:
    def __init__(self, name, country, staple_food):
        self.name = name
        self.country = country
        self.staple_food = staple_food

    def show(self):
        return f"名前: {self.name}, 国名: {self.country}, 主食: {self.staple_food}"


# 和食
class Wasyoku(Itiran):
    def __init__(self, name, country, staple_food, soup_stock):
        super().__init__(name, country, staple_food)
        self.soup_stock = soup_stock

    def show(self):
        return f"{super().show()}, 調味料: {self.soup_stock}"


# 洋食
class Yousyoku(Itiran):
    def __init__(self, name, country, staple_food, sauce):
        super().__init__(name, country, staple_food)
        self.sauce = sauce

    def show(self):
        return f"{super().show()}, 調味料: {self.sauce}"


# 中華
class Chuuka(Itiran):
    def __init__(self, name, country, staple_food, tea):
        super().__init__(name, country, staple_food)
        self.tea = tea

    def show(self):
        return f"{super().show()}, お茶: {self.tea}"


# アジア
class Azia(Itiran):
    def __init__(self, name, country, staple_food, spices):
        super().__init__(name, country, staple_food)
        self.spices = spices

    def show(self):
        return f"{super().show()}, スパイス: {self.spices}"


# 中東
class Chuutou(Itiran):
    def __init__(self, name, country, staple_food, tea):
        super().__init__(name, country, staple_food)
        self.tea = tea

    def show(self):
        return f"{super().show()}, お茶: {self.tea}"
