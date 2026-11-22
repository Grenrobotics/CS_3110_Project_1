class Elevator:
    def __init__(self):
        self.floor_num = 1
        self.door_open = False

        # NUMBER of floors is SUBJECT to change
        self.arr_floors = [1,2,3,4,5,6,7,8,9,10,11,12]

        # Maintenance is SYNONYMOUS with OUT OF SERVICE state
        self.in_maintenance = False
        self.in_emergency_stop = False

        # either up or down
        self.floor_request = None
        self.is_idle = True
        pass

    def reset() -> None: 
        pass

    def open_door(self) -> None:
        self.door_open = True
        pass

    def close_door(self) -> None:
        self.door_open = False
        pass

    def floor_request(self, direction) -> None:
        if direction.lower() == "up" or direction.lower() == "down":
            self.floor_request = direction.lower()
            return "Elevator is going " + direction
        else:
            return "INVALID input!"
        pass

    def emergency_stop(self) -> None:
        pass

    def arrive_at_floor(self, new_floor) -> None:
        self.floor_num = new_floor