# Copyright 2022 Timmy Olsson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is a logger to use with any python script, we can log both to console and file

Usage:
from logger import AppLogger

# Create an instance of the logger
logger = AppLogger(__name__).get_logger()

# Use the logger to log messages
logger.info("This is shown in the console")
logger.warning("This is shown in the console and added to the file")
logger.error("This is shown in the console and added to the file")
"""

import logging

class AppLogger:
    _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    version = 1.2

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self._get_file_handler(name))
        self.logger.addHandler(self._get_stream_handler())

    def _get_file_handler(self, log_file_name):
        """Write log warnings level to a file

        Args:
            log_file_name (string): The name of the logfile

        Returns:
            FileHandler: FileHandler for logging warnings to file
        """
        file_handler = logging.FileHandler(f"{log_file_name}.log")
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter(self._log_format))
        return file_handler

    def _get_stream_handler(self):
        """Write log info level to console

        Returns:
            StreamHandler: StreamHandler for logging info to console
        """
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter(self._log_format))
        return stream_handler

    def get_logger(self):
        """Get the logger with both file log and console log on different levels

        Args:
            name (string): The name of the logger

        Returns:
            logging: A logging object to use when logging in the code
        """
        return self.logger

    def get_version(self):
        """Get the current version of the logger
        """
        return self.version
