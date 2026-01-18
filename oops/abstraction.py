class JarvisAssistant:
    def __init__(self):
        self.__api_key="HEXER-789"
        
    def __autheticate(self):
        print("checking Api..")
        
    def ask_question(self,question):
        self.__autheticate()
        print(f"javis : finding the answer {question} using {self.__api_key}")
        
jarvis=JarvisAssistant()
jarvis.ask_question(input("ask any question : "))