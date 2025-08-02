class hardwareSet:
    def __init__(self):
        self.__capacity = 0
        self.__availability = 0
        self.__checkedOut = {} # make dictionary

    def initialize_capacity(self, hardware):
        self.__capacity = hardware["total_capacity"]

    def initialize_availability(self, hardware):
        self.__availability = hardware["available"]

    def get_availability(self):
        return self.__availability
    
    def get_capacity(self):
        return self.__capacity
    
    def check_out(self, qty, project_ID):
        # grow the list so next projectID entered is the right index
        if self.__checkedOut[project_ID] is None:
            self.__checkedOut[project_ID] = [0,0]

        if qty <= self.__availability:
            self.__availability -= qty
            self.__checkedOut[project_ID] += qty
            return 0
        else:
            self.__checkedOut[project_ID] += self.__availability
            self.__availability = 0
            return -1
        
    def check_in(self, qty, project_ID):
        if qty <= self.__checkedOut[project_ID]:
            self.__checkedOut[project_ID] -= qty
            self.__availability += qty
            return 0
        else:
            return -1
        