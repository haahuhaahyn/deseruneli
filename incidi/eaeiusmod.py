class SmartHome:
    def __init__(self, home_name, location):
        self.home_name = home_name
        self.location = location
        self.devices = []  # List to store smart devices

    def send_notification(self, message):
        for device in self.devices:
            device.receive_notification(message)

# Example usage
my_home = SmartHome("My Home", "City Center")
print(my_home.home_name)  # Output: My Home
print(my_home.location)    # Output: City Center
