__author__ = 'quek'


import unittest
from headandtail import getHeadTail, renameFile
import os

class TestHeadTail(unittest.TestCase):

    def setUp(self):
        self.mock_file ='test/test_file.txt'
        with open(self.mock_file, 'wb') as f:
            f.write('0001\thead\n0002\ttail\n')
        f.close()

    def testHeadTail(self):
        (head, tail) = getHeadTail(self.mock_file)
        self.assertEqual(head,'0001')
        self.assertEqual(tail, '0002')

    def testrenameFile(self):
        renameFile(self.mock_file)
        content = ["test/%s" % x for x in os.listdir('test') if not x.startswith('.')]
        self.assertEqual(content[0], 'test/test_file.txt_0001_0002')

    def tearDown(self):
        content = ["test/%s" % x for x in os.listdir('test') if not x.startswith('.')]
        [os.unlink(x) for x in content]

class TestBulkHeadTail(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.expected = []
        for x in range(1,10):
            with open('test/test_file_%i.txt' % x, 'w+') as f:
                file_content = '000%i\thead\n000%i\ttail\n' % (x, x+1)
                expected_file = "test/test_file_%i.txt_000%i_000%i" % (x, x, x+1)
                self.expected.append(expected_file)
                f.write(file_content)
                f.close()

    def testrenameBulkFile(self):
        file_list = ['test/%s' % x for x in os.listdir('test')]
        for file in file_list:
            renameFile(file)
        content = ["test/%s" % x for x in os.listdir('test') if not x.startswith('.')]
        self.assertItemsEqual(content, self.expected)

    def tearDown(self):
        content = ["test/%s" % x for x in os.listdir('test') if not x.startswith('.')]
        [os.unlink(x) for x in content]


if __name__ == '__main__':
    unittest.main()




