import configparser
import requests

class HKBU_ChatGPT():
    def __init__(self,config_='config.ini'):
        if type(config_) == str:
            self.config = configparser.ConfigParser()
            self.config.read(config_)
        elif type(config_) == configparser.ConfigParser:
            self.config = config_

    def submit(self,message):
        conversation = [{"role": "user", "content": message}]
        url = ((self.config["LLM_AI"]["BASIC_URL"])
               + "/deployments/" + (self.config["LLM_AI"]["MODEL_NAME"])
               + "/chat/completions/?api-version="
               + (self.config["LLM_AI"]["API_VERSION"]))
        headers = {'Content-Type': 'application/json',
                   'api-key':(self.config['LLM_AI']['ACCESS_TOKEN'])}
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
