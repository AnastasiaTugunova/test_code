import unittest
from unittest import TestCase
from parameterized import parameterized
from Test_Code.program import max_volume

class TestMaxVolume(TestCase):
    @parameterized.expand([
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98},
         "yandex"),
        ({},
         None),
        ({'facebook': 5500, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': -98},
         "facebook"),
        ({'facebook': -5500, 'yandex': -120, 'vk': -115, 'google': -99, 'email': 0, 'ok': -98},
         "email")
    ])
    def test_max_volume(self, stats, expected):
        result = max_volume(stats)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

