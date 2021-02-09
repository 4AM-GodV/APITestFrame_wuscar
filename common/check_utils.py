import re
import ast


class CheckUtils():
    def __init__(self, check_response=None):
        self.ck_response = check_response
        self.ck_rules = {
            '无': self.no_check,
            'json键是否存在': self.check_key,
            'json键值对': self.check_keyvalue,
            '正则匹配': self.check_regexp
        }
        self.pass_result = {
            'code': 0,
            'response_reason': self.ck_response.reason,
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result': True,
            'message': ''  # 扩展作为日志输出
        }
        self.fail_result = {
            'code': 2,
            'response_reason': self.ck_response.reason,
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result': False,
            'message': ''  # 扩展作为日志输出
        }

    def no_check(self, check_data=None):
        return self.pass_result

    def check_key(self, check_data=None):
        check_data_list = check_data
        res_list = []  # 存放每次比较的结果
        wrong_key = []  # 存放比较失败key
        for check_data in check_data_list:
            if check_data in self.ck_response.json().keys():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_key.append(check_data)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self, check_data=None):
        res_list = []  # 存放每次比较的结果
        wrong_items = []  # 存放比较失败 key
        for check_item in ast.literal_eval(check_data).items():
            if check_item in self.ck_response.json().items():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_items.append(check_item)
        print(res_list)
        print(wrong_items)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self, check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern, string=self.ck_response.text):
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self, check_type=None, check_data=None):
        code = self.ck_response.status_code
        if code == 200:
            if check_type in self.ck_rules.keys():
                result = self.ck_rules[check_type](check_data)  # self.check_keyvalue(check_data)
                return result
            else:
                self.fail_result['message'] = '不支持%s判断方式'%check_type
                return self.fail_result
        else:
            self.fail_result['message'] = '请求的相应状态码非%s'%str(code)
            return self.fail_result

# if __name__ == '__main__':
#     CheckUtils().check_key({"data": {"accessToken": "(.+?)"}})
#     CheckUtils().check_keyvalue('"accessToken": "(.+?)"')















