import unittest
from transpose import transpose


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class TransposeTest(unittest.TestCase):
  
    def test_simple(self):
        input_line = [
            "ABC",
            "123"
        ]
        expected = [
            "A1",
            "B2",
            "C3"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

  

if __name__ == '__main__':
    unittest.main()