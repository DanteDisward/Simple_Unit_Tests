import unittest
from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        t_object = Runner('Флейморд')
        for i in range(10):
            t_object.walk()
        self.assertEqual(t_object.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        t_object = Runner('Норд')
        for i in range(10):
            t_object.run()
        self.assertEqual(t_object.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        t_object_1 = Runner('Рина')
        t_object_2 = Runner('Зейн')
        for i in range(10):
            t_object_1.run()
            t_object_2.walk()
        self.assertNotEqual(t_object_1.distance, t_object_2.distance)
