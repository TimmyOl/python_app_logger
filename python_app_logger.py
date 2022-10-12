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
There is three different loggers, console logger, file logger and both file and console logger.
Most usual is both since INFO will be printed to console and WARNING or ERROR will be written to file.

Logger for file write:
logger = app_logger.get_file_handler(__name__)

Logger for console:
logger = app_logger.get_file_handler(__name__)

Logger for both file and console:
logger = app_logger.get_logger(__name__)

To write a log message add following code anywhere in the code where the logger is imported and created.
Log levels:
logger.info('This is shown in console')
logger.warning('This is shown in console and added to file')
logger.error('This is shown in console and added to file')

Returns:
Logger: A logger with file handler, stream handler or both
    """

import logging

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler(log_file_name):
    """Write log warnings level to a file

    Args:
        log_file_name (string): The name of the logfile

    Returns:
        FileHandler: FileHandler for logging warnings to file
    """
    file_handler = logging.FileHandler(f"{log_file_name}.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler

def get_stream_handler():
    """Write log info level to console

    Returns:
        StreamHandler: StreamHandler for logging info to console
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler

def get_logger(name):
    """Get the logger with both file log and console log on different levels

    Args:
        name (string): The name of the logger

    Returns:
        logging: A logging object to use when logging in the code
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler(name))
    logger.addHandler(get_stream_handler())
    return logger