import unittest
from Transform import Transform


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        fullPath = "/home/";
        stylesheetDir = "/home/";
        transform = Transform();
        cadena = transform.s(fullPath).xsl(stylesheetDir).warnings('silent').run();
        print(cadena)


if __name__ == '__main__':
    unittest.main()
