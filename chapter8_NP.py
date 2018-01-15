fruits = set(["avocado","tomato","banana"])
vegetables = set(["beets","carrots","tomato"])
bing = fruits | vegetables
jiao = fruits & vegetables
cha  = fruits - vegetables

##################
covered = states_needed & states_for_station
if len(covered) > len(states_needed) :
	best_station = station
	states_covered = covered
	final_station.add(best_station)
	states_needed -= states_covered
	
while states_needed:
	best_station = None
	states_covered = set()
	for station, states in station.items():
		covered = states_needed & states
		if len(covered) > len(states_covered) :
			best_station = station
			states_covered = covered

	states_needed -= states_covered
	final_station.add(best_station)		

print final_station
