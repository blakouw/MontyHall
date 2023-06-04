from matplotlib.pyplot import get
from montyhall import monty_interaction
from montyhall import get_user_input
from montyhall import car
import unittest

print(car)

input = int(input("liczba od 1 do 3"))
class Test_monty_interaction(unittest.TestCase):
    def test_check_if_win(self):
        self.assertEqual(monty_interaction(input), True)
    def test_check_if_lose(self):
        self.assertEqual(monty_interaction(input), False)

if __name__ == '__main__':
    unittest.main()