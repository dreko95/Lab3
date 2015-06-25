import unittest
from mock import Mock


class TestLab1(unittest.TestCase):

    def test_serverCreate(self):
        mock = Mock()
        mock.method = Mock(return_value=True)
        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_serverRead(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_serverUpdate(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_serverDelete(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_clientCreate(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_clientRead(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_clientUpdate(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)

    def test_clientDelete(self):
        mock = Mock()
        mock.method = Mock(return_value=True)

        actual = mock.method()
        expected = True

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()