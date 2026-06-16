import sys

from legacy_code.src.ShippingCalculator import ShippingCalculator


class ShippingApp:
    @staticmethod
    def main():
        if len(sys.argv) != 2:
            print("Usage: python shipping_app.py <orderId>")
            return

        try:
            order_id = int(sys.argv[1])

            calculator = ShippingCalculator()
            cost = calculator.calculate_shipping(order_id)

            print(f"Order ID: {order_id}")
            print(f"Shipping cost: {cost}")

        except ValueError:
            print("orderId must be an integer")

        except Exception as e:
            print(f"Failed to calculate shipping for order {sys.argv[1]}")
            raise


if __name__ == "__main__":
    ShippingApp.main()

    # == == == == == == == == == == == == == ==
    # Running
    # order
    # ID: 1001
    # == == == == == == == == == == == == == ==
    # Order
    # ID: 1001
    # Shipping
    # cost: 2.5
    #
    # == == == == == == == == == == == == == ==
    # Running
    # order
    # ID: 1002
    # == == == == == == == == == == == == == ==
    # Order
    # ID: 1002
    # Shipping
    # cost: 36.8
    #
    # == == == == == == == == == == == == == ==
    # Running
    # order
    # ID: 1003
    # == == == == == == == == == == == == == ==
    # Order
    # ID: 1003
    # Shipping
    # cost: 27.4