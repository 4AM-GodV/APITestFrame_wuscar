#  使用excel驱动


from common.testdata_utils import TestdataUtils
from common.requests_utils import RequestsUtils


all_case_info = TestdataUtils().def_testcase_data_list()
# case_info = all_case_info[1].get('case_info')
# RequestsUtils().request_by_step(case_info)
for case_info in all_case_info:
    RequestsUtils().request_by_step(case_info.get('case_info'))

















