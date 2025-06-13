class User:
    def __init__(self,name,access_code):
        self.__name = name
        self.__access_code = access_code
    def authenticate(self,code):
        if code==self.__access_code:
            return True
        else:
            return False
    def get_username(self):
        return self.__name
        