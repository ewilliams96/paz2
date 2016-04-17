from parameters import FAT_DECREASE_RATE
class Player:
	def __init__(self):
		self.fat = 16 # kilograms 
		self.muscle = 16 # kilograms

		# initialize player to center of screen
		self.xPos = 0
		self.yPos = 0

		# decrease fat every 8 steps
		self.fatDecreaseCounter = FAT_DECREASE_RATE

	def fatDecrease(self):
		self.fatDecreaseCounter -= 1
		if self.fatDecreaseCounter == 0:
			self.fat -= 1
			self.fatDecreaseCounter = FAT_DECREASE_RATE

