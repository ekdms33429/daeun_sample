import logging

# 유효성 검사 및 체크 포인트 관련
class CheckFunc():
    def __init__(self):
        self.logger = logging.getLogger()
        formatter = logging.Formatter("%(filename)s > %(funcName)s: %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(stream_handler)

    def check_equal(self, exp_result, act_result, err_msg=None, soft_check=False):
        """ :param soft_check: 실패 시 True = 계속 실행, False = 테스트 종료 """
        if err_msg is None:
            err_msg = "[Fail] Expected Result: {} | Actual Result: {}".format(exp_result, act_result)
        if soft_check:
            if exp_result != act_result:
                self.logger.info(err_msg)
        else:
            assert exp_result == act_result, err_msg

