from dataclasses import dataclass
from typing import List, Literal


@dataclass(frozen=True)
class Customer:
    loyal: bool

    def is_loyal(self) -> bool:
        return self.loyal


@dataclass(frozen=True)
class OrderItem:
    price: float
    quantity: float


@dataclass(frozen=True)
class OrderSummary:
    subtotal: float
    discount: float
    tax: float
    total: float


class Order:
    def __init__(self, items: List[OrderItem], customer: Customer):
        self.items = items
        self.customer = customer

    def summarise(self) -> OrderSummary:
        self.validate_items()

        subtotal = self.calculate_subtotal()

        discount = self.calculate_discount(subtotal)

        tax, taxable_amount = self.calculate_tax(discount, subtotal)

        total = self.calculate_total(tax, taxable_amount)

        return OrderSummary(subtotal, discount, tax, total)

    def calculate_total(self, tax: float, taxable_amount: float) -> float:
        # Total calculation
        total = taxable_amount + tax
        return total

    def calculate_tax(self, discount: float, subtotal: float | Literal[0]) -> tuple[float, float]:
        # Tax calculation
        taxable_amount = subtotal - discount
        tax = taxable_amount * 0.20
        return tax, taxable_amount

    def calculate_discount(self, subtotal: float | Literal[0]) -> float:
        # Discount rules
        discount = 0.0
        if self.customer.is_loyal():
            discount = subtotal * 0.10
        elif subtotal > 100:
            discount = subtotal * 0.05
        return discount

    def calculate_subtotal(self) -> float | Literal[0]:
        # Subtotal calculation
        subtotal = sum(item.price * item.quantity for item in self.items)
        return subtotal

    def validate_items(self):
        # Validation
        if self.items is None:
            raise ValueError("Items cannot be None")
        if len(self.items) == 0:
            raise ValueError("Order must contain items")