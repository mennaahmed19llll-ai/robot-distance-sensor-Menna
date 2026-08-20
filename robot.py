class Robot:
    # Creates a robot with a name and battery level.
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    # Processes a list of distances and returns the robot's actions.
    def process_distances(self, distances):
        actions = []

        for distance in distances:
            try:
                distance = float(distance)

                if distance < 0:
                    actions.append("ERROR")
                elif distance < 0.5:
                    actions.append("STOP")
                elif distance <= 1:
                    actions.append("SLOW")
                else:
                    actions.append("MOVE")

            except (ValueError, TypeError):
                actions.append("ERROR")

        return actions


# Create a Robot object.
robot = Robot("Teo", 100)

# Test case 1
distances1 = [0.3, 1.5, 0.8, 2.0, 0.4]
print("Test 1:", robot.process_distances(distances1))

# Test case 2
distances2 = [0.1, 0.2, 0.49]
print("Test 2:", robot.process_distances(distances2))

# Test case 3
distances3 = [0.5, 0.7, 1.0]
print("Test 3:", robot.process_distances(distances3))

# Test case 4
distances4 = [1.1, 2.5, 5.0]
print("Test 4:", robot.process_distances(distances4))

# Test case 5
distances5 = [-1, "bad", None]
print("Test 5:", robot.process_distances(distances5))

# Test case 6
distances6 = [0.4, 0.9, 1.5]
print("Test 6:", robot.process_distances(distances6))
