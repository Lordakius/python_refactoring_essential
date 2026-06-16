import unittest

from legacy_code.src.ShippingCalculator import ShippingCalculator, Order


class ShippingCalculatorTest(unittest.TestCase):

    def test_apply_shipping_standard(self):

        order = Order(
            orderId=1000,
            shippingType="STANDARD",
            weightKg=20,
            distanceKm=100,
            fragile=False
        )

        calculator = ShippingCalculator()
        self.assertEqual(10, calculator.apply_shipping(order))

    def test_apply_shipping_express(self):

        order = Order(
            orderId=1000,
            shippingType="EXPRESS",
            weightKg=20,
            distanceKm=100,
            fragile=False
        )

        calculator = ShippingCalculator()
        self.assertEqual(26, calculator.apply_shipping(order))

    def test_apply_shipping_overnight(self):

        order = Order(
            orderId=1000,
            shippingType="OVERNIGHT",
            weightKg=20,
            distanceKm=100,
            fragile=False
        )

        calculator = ShippingCalculator()
        self.assertEqual(49, calculator.apply_shipping(order))

    def test_apply_shipping_international(self):

        order = Order(
            orderId=1000,
            shippingType="INTERNATIONAL",
            weightKg=20,
            distanceKm=100,
            fragile=False
        )

        calculator = ShippingCalculator()
        self.assertEqual(30, calculator.apply_shipping(order))

if __name__ == "__main__":
    unittest.main()