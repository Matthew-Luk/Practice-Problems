# Reverse Psychology
def reverse_psychology(s="Do not do anything"):
	if s == "Do not do anything":
		return "Do not do anything."
	return "Do not " + s + "."

# Pyramid Lists
def pyramid_lists(n):
	answer = []
	for i in range(1,n+1):
		temp = [i] * i
		answer.append(temp)
	return answer

# How Good is Your Name?
scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
            "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
            "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113, "T": 405,
            "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23, " ": 0}

def name_score(name):
	score = 0
	for i in name:
		score += scores[i]
	if score <= 60:
		return "NOT TOO GOOD"
	elif 61 <= score <= 300:
		return "PRETTY GOOD"
	elif 301 <= score <= 599:  
		return "VERY GOOD"
	else:
		return "THE BEST"