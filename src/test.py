import unittest
from Transform import Transform


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        fullPath = "/var/www/desarrollo/comprobantes/colegio/1C332F62-3665-403B-A360-AD4997FEA306.xml";
        stylesheetDir = "/home/misael/Documentos/misproyectos/node/core/src/signati/resources/xslt33/cadenaoriginal_3_3.xslt";
        transform = Transform();
        cadena = transform.s(fullPath).xsl(stylesheetDir).warnings('silent').run();
        # print(transform.commandline)
        print(cadena)


if __name__ == '__main__':
    unittest.main()
