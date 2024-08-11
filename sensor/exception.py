import sys

def exception_messege(error_msg,error_details:sys):
    _,_,ex_tb = error_details.exc_info()
    line_no = ex_tb.tb_frame.f_lineno
    filename = ex_tb.tb_frame.f_code.co_filename
    return f'Error occured in file: {filename}, line_number: {line_no}, messege: {error_msg}'

class SensorException(Exception):
    def __init__(self, error_message,error_details):
        super().__init__(error_message)
        self.error = exception_messege(error_message,error_details)

    def __str__(self):
        return self.error
    
if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

