from unittest import TestCase


def fizzbuzz(number):
    if number%15 ==0:
        return "fizzbuzz"
    if number %5 ==0:
        return "buzz"
    if number %3 ==0:
        return "fizz"
    return str(number)


def do_a_lot_of_fizzbuzz( number):
    # go through all the numbers for fizzbuzz
    lst=[fizzbuzz(i) for i in range(1, number+1)]
    return", ".join(lst)


class FizzBuzzTest(TestCase):
    def test_1(self):
        self._assert_helper(1, "1")

    def _assert_helper(self, number, expected):
        result = fizzbuzz(number)
        self.assertEqual(expected, result)

    def test_2(self):
        self._assert_helper(2, "2")

    def test_3(self):
        self._assert_helper(3, "fizz")


    def test_4(self):

        self._assert_helper(4, "4")

    def test_5(self):

        self._assert_helper(5, "buzz")


    def test_15(self):
        self._assert_helper(15, "fizzbuzz")

    def test_30(self):
        self._assert_helper(30, "fizzbuzz")

    def test_everything(self):
        result = do_a_lot_of_fizzbuzz(5)
        self.assertEquals("1, 2, fizz, 4, buzz", result)
        #when you give fizzbuzz a 5
        #it will return 1, 2, fizz, 4, buzz