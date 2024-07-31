class FileLogger:
    def __init__(self, log_files="basic_log.log"):
        self.log_file = log_files
        self._setup_log_file()

    def _setup_log_file(self):
        with open(self.log_file, 'w') as file:
            file.write("Log start\n")

    def log(self, level, message):
        with open(self.log_file, 'a') as file:
            file.write(f"{level}: {message}\n")

    def info(self, message: str):
        self.log("INFO", message)

    def warning(self, message: str):
        self.log("WARNING", message)

    def error(self, message: str):
        self.log("ERROR", message)

class ConsoleLogger:
    def log(self, level, message):
        print(f"{level}: {message}")

    def info(self, message: str):
        self.log("INFO", message)

    def warning(self, message: str):
        self.log("WARNING", message)

    def error(self, message: str):
        self.log("ERROR", message)

class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        else:
            raise ValueError(f"Unknown logger type: {logger_type}")

