class Elevator:
    def __init__(self):
        self.floor_num = 1
        self.door_open = False

        # Maintenance is SYNONYMOUS with OUT OF SERVICE state
        self.in_maintenance = False
        self.in_emergency_stop = False
        self.floor_request = None
        self.is_idle = True
        pass

    def reset () -> None: 
        pass

    def open_door() -> None:
        pass

    def close_door() -> None:
        pass