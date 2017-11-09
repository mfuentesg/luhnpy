import unittest
import luhnpy


class LuhnTest(unittest.TestCase):
    def test_digit_invalid_argument(self):
        with self.assertRaises(ValueError):
            luhnpy.digit('00x')

    def test_complete_invalid_argument(self):
        with self.assertRaises(ValueError):
            luhnpy.digit('')

    def test_rand_invalid_argument(self):
        with self.assertRaises(ValueError):
            luhnpy.digit('123a1_')

    def test_verify_invalid_argument(self):
        with self.assertRaises(ValueError):
            luhnpy.digit('_')

    def test_digit(self):
        tests = [('7', 5), ('0', 0), ('383', 0), ('101099877719', 5)]
        for test, expected in tests:
            self.assertEqual(luhnpy.digit(test), expected)

    def test_verify_wrong_cases(self):
        tests = ['73', '01', '3836', '1010998777197', '1']
        for test in tests:
            self.assertFalse(luhnpy.verify(test))

    def test_verify_success_cases(self):
        tests = ['75', '00', '3830', '1010998777195', '18']
        for test in tests:
            self.assertTrue(luhnpy.verify(test))

    def test_complete(self):
        tests = [('7', '75'), ('0', '00'), ('383', '3830'), ('101099877719', '1010998777195'), ('1', '18')]
        for test, expected in tests:
            self.assertEqual(luhnpy.complete(test), expected)

    def test_random_length(self):
        rand_str = luhnpy.rand(10)
        self.assertEqual(len(rand_str), 10)

    def test_valid_random_digit(self):
        rand_str = luhnpy.rand(10)
        self.assertEqual(int(rand_str[-1]), luhnpy.digit(rand_str[:-1]))

    def test_success_random(self):
        self.assertTrue(luhnpy.verify(luhnpy.rand()))

    def test_success_random_complete(self):
        rand_str = luhnpy.rand()
        self.assertEqual(luhnpy.complete(rand_str[:-1]), rand_str)


if __name__ == '__main__':
    unittest.main()
