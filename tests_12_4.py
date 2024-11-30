import logging
from unittest import *
from rt_with_exceptions import *


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            t_object = Runner('Флейморд', -15)
            for i in range(10):
                t_object.walk()
            self.assertEqual(t_object.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            t_object = Runner(True)
            for i in range(10):
                t_object.run()
            self.assertEqual(t_object.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        t_object_1 = Runner('Рина')
        t_object_2 = Runner('Зейн')
        for i in range(10):
            t_object_1.run()
            t_object_2.walk()
        self.assertNotEqual(t_object_1.distance, t_object_2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
