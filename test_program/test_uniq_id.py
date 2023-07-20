import unittest
from unittest import TestCase
from parameterized import parameterized
from Test_Code.program import uniq_id

class TestUniqId(TestCase):
    @parameterized.expand([
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35]},
         [213, 15, 54, 119, 98, 35]),
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35],
          'user4': [-213, -98, -98, -35]},
         [213, 15, 54, 119, 98, 35, -213, -98, -35]),
        ({}, []),
        ({'user1': [],
          'user2': [True],
          'user3': [None],
          'user4': [0]},
         [True, None, 0])
        ]
    )
    def test_uniq_id(self, ids, expected):
        result = uniq_id(ids)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()