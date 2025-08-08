class hardwareSet:
    def __init__(self):
        self.__capacity = {}
        self.__availability = {}
        self.__checkedOut = {}

    def initialize_capacity(self, hardware):
        hardware_id = hardware["hardware_id"]
        self.__capacity[hardware_id] = hardware["total_capacity"]


    def initialize_availability(self, hardware):
        hardware_id = hardware["hardware_id"]
        self.__availability[hardware_id] = hardware["available"]

    def get_availability(self):
        return self.__availability
    
    def get_capacity(self):
        return self.__capacity
    
    def check_out(self, qty, project_ID, hardware_id):
        if project_ID not in self.__checkedOut:
            self.__checkedOut[project_ID] = {1: 0, 2: 0}

        available = self.__availability.get(hardware_id, 0)    
        if available == 0:
            return -1, 0

        if qty <= self.__availability.get(hardware_id, 0):
            self.__availability[hardware_id] -= qty
            self.__checkedOut[project_ID][hardware_id] += qty
            return 0, self.__availability[hardware_id]
        else:
            self.__checkedOut[project_ID][hardware_id] += self.__availability[hardware_id]
            self.__availability[hardware_id] = 0
            return 1, 0

    def check_in(self, qty, project_ID, hardware_id):
        if qty < 0:
            return -4, self.__availability.get(hardware_id, 0)  # Invalid quantity

        if hardware_id not in self.__capacity or hardware_id not in self.__availability:
            return -5, 0  # Invalid hardware

        # Determine how many units can actually be accepted based on capacity
        capacity_limit = self.__capacity[hardware_id] - self.__availability[hardware_id]
        actual_checkin = min(qty, capacity_limit)

        if actual_checkin == 0:
            return -3, self.__availability[hardware_id]  # Cannot check in more (at capacity)

        # Update availability
        self.__availability[hardware_id] += actual_checkin

        # Update project-specific checkedOut only if it already exists
        if project_ID not in self.__checkedOut:
            self.__checkedOut[project_ID] = {1: 0, 2: 0}

        if hardware_id not in self.__checkedOut[project_ID]:
            self.__checkedOut[project_ID][hardware_id] = 0

        self.__checkedOut[project_ID][hardware_id] -= actual_checkin
        if self.__checkedOut[project_ID][hardware_id] < 0:
            self.__checkedOut[project_ID][hardware_id] = 0

        if actual_checkin < qty:
            return 1, self.__availability[hardware_id]  # Partial check-in
        return 0, self.__availability[hardware_id]  # Full check-in
