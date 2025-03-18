import configparser
import requests
import os

class HKBU_ChatGPT():
    def submit(self,message):
        conversation = [{"role": "user", "content": message}]
        url = ((os.environ['LLM_BASIC_URL'])
               + "/deployments/" + (os.environ['LLM_MODEL_NAME'])
               + "/chat/completions/?api-version="
               + (os.environ['LLM_API_VERSION']))
        headers = {'Content-Type': 'application/json',
                   'api-key':(os.environ['LLM_ACCESS_TOKEN'])}
        payload = {'messages': conversation}
        response = requests.post(url,json=payload,headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response
if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    while True:
        user_input = input("请说出你的问题（由Chatgpt4o-mini回答）：\t")
        response = ChatGPT_test.submit(user_input)
        print(response)
