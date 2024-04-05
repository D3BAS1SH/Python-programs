import matplotlib.pyplot as ply

CityTemp={
    "A":(10,31),
    "B":(-6,15),
}

CityName=CityTemp.keys()
minTemp=[x[0] for x in CityTemp.values()]
maxTemp=[x[1] for x in CityTemp.values()]

ply.figure(figsize=(16,9))
ply.scatter(maxTemp,minTemp,marker='o')

ply.grid(True)
ply.show()