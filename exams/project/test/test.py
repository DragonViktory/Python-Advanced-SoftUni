from project.second_hand_car import SecondHandCar
from unittest import TestCase


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.second_hand_car = SecondHandCar("Audi", "A3", 1000, 50_000)

    def test_init(self):
        self.assertEqual(self.second_hand_car.model, "Audi")
        self.assertEqual(self.second_hand_car.car_type, "A3")
        self.assertEqual(self.second_hand_car.mileage, 1000)
        self.assertEqual(self.second_hand_car.price, 50_000)
        self.assertEqual(self.second_hand_car.repairs, [])

    def test_props(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 0
        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

    def test_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 0
        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(50_000)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(60_000)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')
        result = self.second_hand_car.set_promotional_price(40000)
        exception_result = 'The promotional price has been successfully set.'
        self.assertEqual(exception_result, result)
        self.assertEqual(self.second_hand_car.price,40000)

    def test_need_repair(self):
        result = self.second_hand_car.re


