# user.py
#class definition for users
from encryption import encrypt, decrypt

class User:   ### Set N and D to None to get it running
    def __init__(self, user_data = None, user_id = None, name = None, password = None, project_id = None, encrypted = False, N=None, D=None):
        self.N = N
        self.D = D
        if user_data:  # to read in user document from database
            self.__user_id = user_data.get("user_id", "")
            self.__name = user_data.get("name", "")
            self.__password = user_data.get("password", "")
            self.__project_id = user_data.get("project_id", [])
        else:  # to initialize new user with input from frontend
            self.__user_id = user_id   # username input on the frontend
            self.__name = name      # name input on the frontend
            self.__password = password if encrypted else encrypt(password, N, D) # password input on the frontend
            self.__project_id = project_id if project_id is not None else []

    def check_password(self, user_input):
        " decrypts stored user password and checks against input "
        return decrypt(self.__password, self.D, self.N) == user_input
    
    def add_to_project(self, project_id):
        if project_id not in self.__project_id:
            self.__project_id.append(project_id)

    def remove_from_project(self, project_id):
        if project_id in self.__project_id:
            self.__project_id.remove(project_id)
    
    def get_projects(self):
        return self.__project_id

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name
    
    def to_dict(self):
        """turns info back into dict format to save to db"""
        return {
            "user_id": self.__user_id,
            "name": self.__name,
            "password": self.__password,
            "project_id": self.__project_id
        }
