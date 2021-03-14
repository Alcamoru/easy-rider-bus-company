# create the planets.txt
planets = open("planets.txt", "w", encoding="utf-8")

all_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for planet in all_planets:
    planets.write(planet + "\n")

planets.close()
