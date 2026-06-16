from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    price: float
    on_sale: bool

    def calculate_final_price(self) -> float:
        price = self.get_price()

        if self.is_on_sale():
            price *= 0.8

        return price

    def get_price(self) -> float:
        return self.price

    def is_on_sale(self) -> bool:
        return self.on_sale