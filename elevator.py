class Elevator(object):

    def __init__(self, type, direction, currentLvl, currentElevatorLevel, futureelevatorlevel):
        self.type = type
        self.direction = direction
        self.currentLvl = currentLvl
        self.currentElevatorLevel = currentElevatorLevel
        self.futureelevatorlevel = futureelevatorlevel

        def retrieveElevator():



            level1 = abs(int(currentElevatorLevel))
            level2 = abs(int(currentLvl))
            differenceInLevels = abs(level1 - level2)


            if self.direction == "up" and self.currentLvl == self.currentElevatorLevel:
                print("door opens")
            elif self.direction == "up" and self.currentLvl > self.currentElevatorLevel:
                print("elevator " + self.type + " moves " + str(differenceInLevels) + " floor up and door opens")
            elif self.direction == "up" and self.currentLvl < self.currentElevatorLevel:
                print("elevator " + self.type + " moves " + str(differenceInLevels) + " floor down and door opens")
            elif self.direction == "down" and self.currentLvl == self.currentElevatorLevel:
                print("door opens")
            elif self.direction == "down" and self.currentLvl > self.currentElevatorLevel:
                print("elevator " + self.type + " moves " + str(differenceInLevels) + " floor up and door opens")
            elif self.direction == "down" and self.currentLvl < self.currentElevatorLevel:
                print("elevator " + self.type + " moves " + str(differenceInLevels) + " floor down and door opens")
            else:
                print("elevator failed take the stairs ")

        def goToFloor():

            levela = abs(int(self.futureelevatorlevel))
            levelb = abs(int(self.currentLvl))
            differenceinlevels = abs(levela - levelb)

            if self.currentLvl == self.futureelevatorlevel:
                print("elevator does not move")
            elif self.currentLvl > self.futureelevatorlevel:
                print("door closes and " + " elevator " + self.type + " moves " + str(differenceinlevels) + " floor down and door opens")
            elif self.currentLvl < self.futureelevatorlevel:
                print("door closes and " + " elevator " + self.type + " moves " + str(differenceinlevels) + " floor up and door opens")
            else:
                print("elevator failed take the stairs ")

        retrieveElevator()
        goToFloor()

