class hardwareSet:
    def __init__(self):
        self.__capacity = 0
        self.__availability = 0
        self.__checkedOut = {}

    def initialize_capacity(self, hardware):
        self.__capacity = hardware["total_capacity"]

    def initialize_availability(self, hardware):
        self.__availability = hardware["available"]

    def get_availability(self):
        return self.__availability
    
    def get_capacity(self):
        return self.__capacity
    
    def check_out(self, qty, project_ID, hardware_id):
        if project_ID not in self.__checkedOut:
            self.__checkedOut[project_ID] = {1: 0, 2: 0}

        if qty <= self.__availability:
            self.__availability -= qty
            self.__checkedOut[project_ID][hardware_id] += qty
            return 0
        else:
            self.__checkedOut[project_ID][hardware_id] += self.__availability
            self.__availability = 0
            return -1
        
    def check_in(self, qty, project_ID, hardware_id):
        # Ensure project and hardware exist
        if project_ID not in self.__checkedOut or hardware_id not in self.__checkedOut[project_ID]:
            return -1
        if qty <= self.__checkedOut[project_ID][hardware_id]:
            self.__checkedOut[project_ID][hardware_id] -= qty
            self.__availability += qty
            return 0
        else:
            return -1
        