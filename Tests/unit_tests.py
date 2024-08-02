import unittest

from src.Logger import FileLogger

class TestFileLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_log.log"
        self.logger = FileLogger(self.log_file)

    def test_info_logging(self):
        self.logger.info("This is an info message")
        with open(self.log_file, 'r') as file:
            lines = file.readlines()
            self.assertIn("INFO: This is an info message\n", lines)

    def test_warning_logging(self):
        self.logger.warning("This is a warning message")
        with open(self.log_file, 'r') as file:
            lines = file.readlines()
            self.assertIn("WARNING: This is a warning message\n", lines)

    def test_error_logging(self):
        self.logger.error("This is an error message")
        with open(self.log_file, 'r') as file:
            lines = file.readlines()
            self.assertIn("ERROR: This is an error message\n", lines)