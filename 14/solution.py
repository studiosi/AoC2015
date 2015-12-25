class Reindeer:
	def __init__(self, name, speed, time_before_rest, rest_time):
		self.__name = name
		self.__speed = int(speed)
		self.__time_before_rest = int(time_before_rest)
		self.__rest_time = int(rest_time)
		self.__current_position = 0
		self.__time_without_resting = 0
		self.__is_resting = False
		self.__time_already_rest = 0
		self.__distance_run = 0
		self.__points = 0
	def step_second(self):
		if self.__is_resting:
			self.__time_already_rest += 1
			if self.__rest_time == self.__time_already_rest:
				self.__time_already_rest = 0
				self.__time_without_resting = 0
				self.__is_resting = False
		else:
			self.__distance_run += self.__speed
			self.__time_without_resting += 1
			if self.__time_without_resting == self.__time_before_rest:
				self.__is_resting = True
	def get_distance_run(self):
		return self.__distance_run
	def increment_points(self):
		self.__points += 1
	def get_points(self):
		return self.__points
	def get_name(self):
		return self.__name
		
def createReindeer(s):
	x = s.split()
	return Reindeer(x[0], x[3], x[6], x[13])
	
inp = open("input.txt").readlines()

# Part 1
reindeers = []
for l in inp:
	reindeers.append(createReindeer(l))
for i in range(2503):
	for r in reindeers:
		r.step_second()
print(max([x.get_distance_run() for x in reindeers]))

# Part 2
reindeers = []
for l in inp:
	reindeers.append(createReindeer(l))
for i in range(2503):
	for r in reindeers:
		r.step_second()
	m = max([r.get_distance_run() for r in reindeers])
	for r in reindeers:
		if r.get_distance_run() == m:
			r.increment_points()
print(max([r.get_points() for r in reindeers]))

			
