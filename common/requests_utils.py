import requests
import ast
import jsonpath
import re
from requests.exceptions import RequestException
from requests.exceptions import ProxyError
from requests.exceptions import ConnectionError

from common.check_utils import CheckUtils
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
        try:
            url = self.hosts + get_info["请求地址"]
            response = self.session.get(url=url,
                                        params=ast.literal_eval(get_info["请求参数(get)"]),
                                        headers=self.headers
                                        )
            response.encoding = response.apparent_encoding
            if get_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath(response.json(), get_info["取值代码"])[0]
                self.temp_variables[get_info["传值变量"]] = value
            elif get_info["取值方式"] == "正则取值":
                value = re.findall(get_info["取值代码"], response.text)[0]
                self.temp_variables[get_info["传值变量"]] = value
            result = CheckUtils(response).run_check(get_info['期望结果类型'], get_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求:代理错误异常' % (get_info["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求:连接超时异常' % (get_info["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求:Request异常,原因: %s' % (get_info["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求:系统异常,原因:%s'%(get_info["接口名称"], e.__str__())}
        return result

    def __post(self, post_info):
        try:
            url = self.hosts + post_info["请求地址"]
            response = self.session.post(url=url,
                                         headers=self.headers,
                                         json=ast.literal_eval(post_info["提交数据(post)"])
                                         )
            response.encoding = response.apparent_encoding
            if post_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath(response.json(), post_info["取值代码"])[0]
                self.temp_variables[post_info["传值变量"]] = value
            elif post_info["取值方式"] == "正则取值":
                value = re.findall(post_info["取值代码"], response.text)[0]
                self.temp_variables[post_info["传值变量"]] = value
            result = CheckUtils(response).run_check(post_info['期望结果类型'], post_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求:代理错误异常' % (post_info["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求:连接超时异常' % (post_info["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求:Request异常,原因: %s' % (post_info["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求:系统异常,原因:%s' % (post_info["接口名称"], e.__str__())}
        return result

    def __put(self, put_info):
        try:
            url = self.hosts + put_info["请求地址"]
            response = self.session.put(url=url,
                                        headers=self.headers,
                                        params=ast.literal_eval(put_info["请求参数(get)"]),
                                        json=ast.literal_eval(put_info["提交数据(post)"])
                                        )
            response.encoding = response.apparent_encoding
            if put_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath(response.json(), put_info["取值代码"])[0]
                self.temp_variables[put_info["传值变量"]] = value
            elif put_info["取值方式"] == "正则取值":
                value = re.findall(put_info["取值代码"], response.text)[0]
                self.temp_variables[put_info["传值变量"]] = value
            result = CheckUtils(response).run_check(put_info['期望结果类型'], put_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求:代理错误异常' % (put_info["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求:连接超时异常' % (put_info["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求:Request异常,原因: %s' % (put_info["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求:系统异常,原因:%s' % (put_info["接口名称"], e.__str__())}
        return result

    def __delete(self, delete_info):
        try:
            url = self.hosts + delete_info["请求地址"]
            response = self.session.delete(url=url,
                                           headers=self.headers,
                                           params=ast.literal_eval(delete_info["请求参数(get)"]),
                                           json=ast.literal_eval(delete_info["提交数据(post)"])
                                           )
            response.encoding = response.apparent_encoding
            if delete_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath(response.json(), delete_info["取值代码"])[0]
                self.temp_variables[delete_info["传值变量"]] = value
            elif delete_info["取值方式"] == "正则取值":
                value = re.findall(delete_info["取值代码"], response.text)[0]
                self.temp_variables[delete_info["传值变量"]] = value
            result = CheckUtils(response).run_check(delete_info['期望结果类型'], delete_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求:代理错误异常' % (delete_info["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求:连接超时异常' % (delete_info["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求:Request异常,原因: %s' % (delete_info["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求:系统异常,原因:%s' % (delete_info["接口名称"], e.__str__())}
        return result

    def __patch(self, patch_info):
        try:
            url = self.hosts + patch_info["请求地址"]
            response = self.session.delete(url=url,
                                           headers=self.headers,
                                           params=ast.literal_eval(patch_info["请求参数(get)"]),
                                           json=ast.literal_eval(patch_info["提交数据(post)"])
                                           )
            response.encoding = response.apparent_encoding
            if patch_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath(response.json(), patch_info["取值代码"])[0]
                self.temp_variables[patch_info["传值变量"]] = value
            elif patch_info["取值方式"] == "正则取值":
                value = re.findall(patch_info["取值代码"], response.text)[0]
                self.temp_variables[patch_info["传值变量"]] = value
            result = CheckUtils(response).run_check(patch_info['期望结果类型'], patch_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求:代理错误异常' % (patch_info["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求:连接超时异常' % (patch_info["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求:Request异常,原因: %s' % (patch_info["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求:系统异常,原因:%s' % (patch_info["接口名称"], e.__str__())}
        return result

    def request(self, step_info):
        try:
            request_type = step_info["请求方式"]
            param_variable_list = re.findall('\\${\w+}', step_info["请求参数(get)"])
            if param_variable_list:
                for param_variable in param_variable_list:
                    step_info["请求参数(get)"] = step_info["请求参数(get)"].replace(param_variable, '"%s"' % self.temp_variables.get(
                        param_variable[2:-1]))
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
        except Exception as e:
            result = {'code': 4, 'result': '用例编号[%s]的[%s]步骤出现系统异常，原因：%s'%(step_info['测试用例编号'], step_info["测试用例步骤"], e.__str__())}
        return result

    def request_by_step(self, step_infos):
        self.temp_variables = {}
        for step_info in step_infos:
            temp_result = self.request(step_info)
            # print(temp_result)
            if temp_result['code'] != 0:
                break
        return temp_result


if __name__ == '__main__':
    case_info = [
            {'测试用例编号': 'case02', '测试用例名称': '修改城市名称', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '登录获取token', '请求方式': 'post', '请求地址': '/chinaos/userService/api/v1/mulan/login', '请求参数(get)': '', '提交数据(post)': '{"email": "guorong.wu@wework.cn","password": "Abc12345"}', '取值方式': '正则取值', '传值变量': 'token', '取值代码': '"accessToken":"(.+?)"', '期望结果类型': '正则匹配', '期望结果': '"accessToken":"(.+?)"'}]
    RequestsUtils().request_by_step(case_info)



































