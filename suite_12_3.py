#https://github.com/Linnight1/Homework-/blob/master/Hmwrk_12_2a.py
#https://github.com/Linnight1/Homework-/blob/master/Hmwrk_12_1b.py
import unittest
import Hmwrk_12_2a
import Hmwrk_12_1b
HmST = unittest.TestSuite()
HmST.addTest(unittest.TestLoader().loadTestsFromTestCase(Hmwrk_12_1b.RunnerTest))
HmST.addTest(unittest.TestLoader().loadTestsFromTestCase(Hmwrk_12_2a.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(HmST)