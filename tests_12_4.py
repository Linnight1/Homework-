import logging
import unittest
import Test_12_4
logging.basicConfig(level=logging.INFO, filemode="w",filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:

            self.some_obj = Test_12_4.Runner("obj",-10)
            logging.info('"test_walk" выполнен успешно')

            for i in range(10):
                Test_12_4.Runner.walk(self.some_obj)
            self.assertEqual(self.some_obj.distance, 50)
        except ValueError:
            logging.warn("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            self.some_obj = Test_12_4.Runner(123)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                Test_12_4.Runner.run(self.some_obj)
            self.assertEqual(self.some_obj.distance, 100)
        except TypeError:
            logging.warn("Неверный тип данных для объекта Runner", exc_info=True)
if __name__ == "__main__":
    unittest.main()

