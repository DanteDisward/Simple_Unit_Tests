import unittest
import tests_12_1
import tests_12_2

skull = unittest.TestSuite()
skull.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
skull.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
skull_runner = unittest.TextTestRunner(verbosity=2)
skull_runner.run(skull)
