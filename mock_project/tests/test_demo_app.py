import unittest

from src.demo_app import status_message


class StatusMessageTests(unittest.TestCase):
    def test_healthy_service(self):
        self.assertEqual(status_message("demo-api", True), "demo-api: healthy")

    def test_degraded_service(self):
        self.assertEqual(status_message("demo-api", False), "demo-api: degraded")

    def test_empty_service_is_rejected(self):
        with self.assertRaises(ValueError):
            status_message(" ", True)


if __name__ == "__main__":
    unittest.main()