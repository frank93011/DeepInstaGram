import pickle
import json

pic_file = open('user_personality', 'rb')
data = pickle.load(pic_file)
print(data)
# hehe = json.dumps(data,ensure_ascii=False, sort_keys = False, indent = 4, separators=(',', ': '))
# with open('hehe.json', 'w') as file:
# 	file.write(hehe)

