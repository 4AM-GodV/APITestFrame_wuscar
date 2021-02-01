
# import urllib3

import requests
# urllib3.disable_warnings()

session = requests.session()

#   登录接口
headers = {
    'Authorization': 'X-CAT',
    'Content-Type': 'application/json;charset=UTF-8',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
res01 = session.post(url='https://api-int.wework.cn/chinaos/userService/api/v1/mulan/login',
                     json={"email": "guorong.wu@wework.cn",
                           "password": "Abc12345"
                           },
                     headers=headers
                     )
# print(res01.json())
token = res01.json()['data']['accessToken']
print(token)

# 增加订单接口
# "Token %s"%token
headers2 = {
    'Authorization': 'X-CAT',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
            }
res02 = session.put(url='https://api-int.wework.cn/chinaos/mulanOrderService/api/v1/thirdparty/order',
                    json={
  "customerUuid": "string",
  "startTime": 0,
  "endTime": 0,
  "grossPrice": 0,
  "currency": "string",
  "locationUuid": "string",
  "remark": "string",
  "contractNo": "string",
  "relatedContractNo": "string",
  "contractUrl": "string",
  "csm": "string",
  "salesPersonEmail": "string",
  "contractType": "NEW_MEMBER-新合同",
  "transferType": "string",
  "overdueFineTerm": "string",
  "salesPolicy": {
    "billingCycle": "string"
  },
  "noticeDay": 0,
  "orderItems": [
    {
      "grossPrice": 0,
      "suggestedCbp": 0,
      "currency": "string",
      "quantity": 0.01,
      "skuUuid": "string",
      "startTime": 0,
      "endTime": 0,
      "type": "string",
      "remark": "string",
      "taxRate": 0,
      "taxCode": "string",
      "srAmount": 0,
      "crmOrderID": "string",
      "orderItemAmount": [
        {
          "discountOff": 0,
          "amount": 0,
          "grossPrice": 0,
          "startTime": 0,
          "endTime": 0
        }
      ]
    }
  ],
  "transferFrom": [
    "string"
  ]
},
                    headers=headers2
                        )
# print(res02.json())



















