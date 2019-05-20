import json

a = '{"from":"en","to":"zh","trans_result":[{"src":"apple","dst":"\u82f9\u679c"}]}'
result = json.loads(a)
print(result['trans_result'][0].get('dsst', ''))