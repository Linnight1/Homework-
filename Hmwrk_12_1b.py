#https://github.com/Linnight1/Homework-/blob/master/Hmwrk_12_1.py

import Hmwrk_12_1
import unittest
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        self.some_obj = Hmwrk_12_1.Runner("obj")
        for i in range(10):
            Hmwrk_12_1.Runner.walk(self.some_obj)
        self.assertEqual(self.some_obj.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        self.some_obj = Hmwrk_12_1.Runner("obj")
        for i in range(10):
            Hmwrk_12_1.Runner.run(self.some_obj)
        self.assertEqual(self.some_obj.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.some_obj = Hmwrk_12_1.Runner("obj")
        self.some_obj_2 = Hmwrk_12_1.Runner("obj2")
        for i in range(10):
            Hmwrk_12_1.Runner.run(self.some_obj)
            Hmwrk_12_1.Runner.walk(self.some_obj_2)

        self.assertNotEqual(self.some_obj.distance, self.some_obj_2.distance)

if __name__ == "__main__":
    unittest.main()
