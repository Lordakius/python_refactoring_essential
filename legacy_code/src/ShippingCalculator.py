from dataclasses import dataclass
import requests


@dataclass(frozen=True)
class Order:
    orderId: int
    shippingType: str
    weightKg: float
    distanceKm: float
    fragile: bool


class ShippingCalculator:

    def calculate_shipping(self, order_id: int) -> float:
        try:
            order = self.get_order(order_id)
            return self.apply_shipping(order)

        except Exception as e:
            print(e)
            return -1.0

    def apply_shipping(self, order: Order) -> float:

        match order.shippingType :
            case "STANDARD" :
                return order.weightKg * 0.5
            case "EXPRESS" :
                return order.weightKg * 0.8 + order.distanceKm * 0.1
            case "OVERNIGHT":
                return order.weightKg * 1.2 + 25
            case "INTERNATIONAL":
                return order.weightKg * 1.5
            case _ :
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")


    def get_order(self, order_id: int) -> Order:
        url = f"https://codemanship.co.uk/api/orders.php?orderId={order_id}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        order = Order(
            orderId=data["orderId"],
            shippingType=data["shippingType"],
            weightKg=data["weightKg"],
            distanceKm=data["distanceKm"],
            fragile=data["fragile"]
        )
        return order