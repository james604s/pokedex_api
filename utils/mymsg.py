from .logger import get_logger


logger = get_logger(__name__)


class RspMsg:
    @staticmethod
    def pack_succ(data, params=None):
        resp_dict = {"result": {"succeed": True, "code": 1000, "msg": "OK"}}
        if data is not None:
            resp_dict["data"] = data

        if params is not None:
            resp_dict["params"] = params

        return resp_dict

    @staticmethod
    def pack_error(data,err_code):
        resp_dict = {"result": {"succeed": False, "code": err_code, "msg": "Fail"}, "data": {}}
        # if params is not None:
        #     resp_dict["params"] = params
        if data is not None:
            resp_dict["data"] = data
        return resp_dict

    @staticmethod
    def pack_part(data, err_code, err_msg):
        resp_dict = {"result": {"succeed": True, "code": err_code, "msg": err_msg}}
        if data is not None:
            resp_dict["data"] = data

        return resp_dict
