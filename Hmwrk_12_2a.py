import test_12_2
import unittest
#https://github.com/Linnight1/Homework-/blob/master/test_12_2.py

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner_1 = test_12_2.Runner("Усейн", 10)
        self.runner_2 = test_12_2.Runner("Андрей", 9)
        self.runner_3 = test_12_2.Runner("Ник", 3)
    @classmethod
    def tearDownClass(self):
        for key, value in self.all_results.items():
            print(key,":",value)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_Tournament_1(self):
        self.obj = test_12_2.Tournament(90,self.runner_1,self.runner_3)
        self.all_results.update(self.obj.start())

        self.assertTrue(self.all_results[max(self.all_results)],"Ник")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_Tournament_2(self):
        self.obj = test_12_2.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update(self.obj.start())

        self.assertTrue(self.all_results[max(self.all_results)], "Ник")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_Tournament_3(self):
        self.obj = test_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update(self.obj.start())

        self.assertTrue(self.all_results[max(self.all_results)], "Ник")



if __name__ == "__main__":
    unittest.main()