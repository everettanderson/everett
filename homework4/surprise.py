# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

import numpy as np

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list.
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

#1)


def namestars(targets):
	for key in targets.keys():
		print(key)
print(namestars(targets))

#2)

def classify(targets):
	for item in targets:
		print(f"{item} Spectral Type: {targets[item]["Spectral Type"]}")
print(classify(targets))

#3)

def sizemin(targets):
	passminsize = []
	for item in targets:
		if targets[item]["Magnitude"] > 0.1:
			passminsize.append(item)
	return passminsize
print(sizemin(targets))

#4)

targets["Proxima Centauri"] = {"RA": "14h 29m 42.9s", "Dec": "-62° 40' 46\"", "Magnitude": 11, "Spectral Type": "M5.5 Ve"}

#5)

def closest_and_brightest(targets):
	score = []
	for star in targets:
		#add score for angle (logarithmic)
		currentscore = 0
		angle_list = list(targets[star]["Dec"])
		angle_magnitude = int(str(angle_list[1] + str(angle_list[2])))
		if angle_list[0] == "-":
			currentscore = (np.round(np.log10(abs(-20 - angle_magnitude)), 2))
		else:
			currentscore = (np.round(np.log10(abs(20- angle_magnitude)), 2))
		#add score for brightness(geometric ish)
		if targets[star]["Magnitude"] < 1:
			currentscore = currentscore - (np.round((targets[star]["Magnitude"]), 2))
		else:
			currentscore = currentscore - (np.round(np.sqrt((targets[star]["Magnitude"])), 2))
		score.append(currentscore)
	# add stars to a matching star list
	starlist = []
	for key in targets:
		starlist.append(key)
	return starlist[int(np.argmin(score))]

print(closest_and_brightest(targets))

#6) Orion
