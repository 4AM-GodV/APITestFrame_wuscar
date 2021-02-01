import requests
import ast
import jsonpath

from common.localconfig_utils import local_config


class RequestsUtils():
    def __init__(self):
        self.hosts = local_config.URL
        self.headers = {'Authorization': 'X-CAT',
                        'Content-Type': 'application/json;charset=UTF-8',
                        'Sec-Fetch-Site': 'same-site',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Dest': 'empty',
                        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
                        }
        self.session = requests.session()
        self.temp_variables = {}  # 存放临时变量，用来传值

    def __get(self, get_info):
        url = self.hosts + get_info["请求地址"]
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_info["请求参数(get)"])
                                    )
        result = {
            'code': 0,
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
                 }
        return result

    def __post(self, post_info):
        url = self.hosts + post_info["请求地址"]
        response = self.session.post(url=url,
                                     headers=self.headers,
                                     json=ast.literal_eval(post_info["提交数据(post)"])
                                     )
        response.encoding = response.apparent_encoding
        if post_info["取值方式"] == "json取值":
            value = jsonpath.jsonpath(response.json(), post_info["取值代码"])[0]
            self.temp_variables[post_info["传值变量"]] = value
            print(self.temp_variables)

        result = {
            'code': 0,
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def __put(self, put_info):
        url = self.hosts + put_info["请求地址"]
        response = self.session.put(url=url,
                                    headers=self.headers,
                                    json=ast.literal_eval(put_info["提交数据(post)"])
                                    )
        response.encoding = response.apparent_encoding
        result = {
            'code': 0,
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def __delete(self, delete_info):
        url = self.hosts + delete_info["请求地址"]
        response = self.session.delete(url=url,
                                       headers=self.headers,
                                       params=ast.literal_eval(delete_info["提交数据(post)"])
                                       )
        response.encoding = response.apparent_encoding
        result = {
            'code': 0,
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def __patch(self, patch_info):
        url = self.hosts + patch_info["请求地址"]
        response = self.session.delete(url=url,
                                       headers=self.headers,
                                       params=ast.literal_eval(patch_info["提交数据(post)"])
                                       )
        response.encoding = response.apparent_encoding
        result = {
            'code': 0,
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def request(self, step_info):
        request_type = step_info["请求方式"]
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        elif request_type == "put":
            result = self.__put(step_info)
        elif request_type == "delete":
            result = self.__delete(step_info)
        elif request_type == "patch":
            result = self.__patch(step_info)
        else:
            result = {'code': 1, 'result': '请求方式不支持'}
        return result

    def request_by_step(self, step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code'] != 0:
                break
        return temp_result


if __name__ == '__main__':
    post_info = {'测试用例编号': 'case01', '测试用例名称': '登录int环境', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取token', '请求方式': 'post', '请求地址': '/chinaos/userService/api/v1/mulan/login', '请求参数(get)': '', '提交数据(post)': '{"email": "guorong.wu@wework.cn","password": "Abc12345"}', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.data.accessToken', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in'}
    RequestsUtils().request(post_info)



































