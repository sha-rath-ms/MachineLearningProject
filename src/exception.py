import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    error_message = f'Error occured in Python script name "{exc_tb.tb_frame.f_code.co_filename}" in line number {exc_tb.tb_lineno} \nerror message: {str(error)}'

    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


# if __name__ == '__main__':
#     logger = logging.getLogger(__name__)
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logger.info("Number cannot be divided by zero")
#         raise CustomException("Number cannot be divided by zero", sys)
