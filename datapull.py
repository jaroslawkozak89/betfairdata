import simplejson as json
import matplotlib.pyplot as plt

eventName = ""
firstTime = 0
idHome = 0
idDraw = 0
idAway = 0
oddsHome = []
oddsDraw = []
oddsAway = []
timeline = []
lastTradedHome = 0
lastTradedDraw = 0
lastTradedAway = 0

file = open("1.161331077", "r")

for line in file:

	tempdict = json.loads(line)

	if eventName == "":
		eventName = tempdict["mc"][0]["marketDefinition"]["eventName"]
		idHome = tempdict["mc"][0]["marketDefinition"]["runners"][0]["id"]
		idDraw = tempdict["mc"][0]["marketDefinition"]["runners"][2]["id"]
		idAway = tempdict["mc"][0]["marketDefinition"]["runners"][1]["id"]

	if "marketDefinition" in tempdict["mc"][0]:
		if tempdict["mc"][0]["marketDefinition"]["inPlay"] == True:
			break

	if "rc" in tempdict["mc"][0].keys():

		if firstTime == 0:
			firstTime = tempdict["pt"]

		if lastTradedHome == 0 or lastTradedDraw == 0 or lastTradedAway == 0:

			for i in tempdict["mc"][0]["rc"]:

				if i["id"] == idHome:
					lastTradedHome = i["ltp"]

				if i["id"] == idDraw:
					lastTradedDraw = i["ltp"]

				if i["id"] == idAway:
					lastTradedAway = i["ltp"]

		else:

			timeline.append((tempdict["pt"]-firstTime)/60000)
			changes = []

			for i in tempdict["mc"][0]["rc"]:

				if i["id"] == idHome:
					oddsHome.append(i["ltp"])
					lastTradedHome = i["ltp"]
					changes.append(i["id"])

				if i["id"] == idDraw:
					oddsDraw.append(i["ltp"])
					lastTradedDraw = i["ltp"]
					changes.append(i["id"])

				if i["id"] == idAway:
					oddsAway.append(i["ltp"])
					lastTradedAway = i["ltp"]
					changes.append(i["id"])

			if idHome not in changes:
				oddsHome.append(lastTradedHome)
			if idDraw not in changes:
				oddsDraw.append(lastTradedDraw)
			if idAway not in changes:
				oddsAway.append(lastTradedAway)


print(timeline)
print(len(oddsHome))
print(len(oddsDraw))
print(len(oddsAway))
print(len(timeline))


plt.plot(timeline, oddsHome, label = "Home")
plt.plot(timeline, oddsDraw, label = "Draw")
plt.plot(timeline, oddsAway, label = "Away")
plt.xlabel("time")
plt.ylabel("odds")
plt.legend()
plt.show()

print(timeline)
print(len(oddsHome))
print(len(oddsDraw))
print(len(oddsAway))
print(len(timeline))
