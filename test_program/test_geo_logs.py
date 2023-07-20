import unittest
from unittest import TestCase
from parameterized import parameterized
from Test_Code.program import geo_log


class TestGeoLogs(TestCase):
    @parameterized.expand([
        ([
             {'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}
         ],
            [{'visit1': ['Москва', 'Россия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}]),

        ([
             {'visit2': ['Дели', 'Индия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
          ],
             []),

        ([
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
          ],
            [{'visit1': ['Москва', 'Россия']},
             {'visit8': ['Тула', 'Россия']}])
    ]
)
    def test_visits_country(self, geo_logs_data, expected):
        result = geo_log(geo_logs_data)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()