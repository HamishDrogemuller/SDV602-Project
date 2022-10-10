import csv
import pandas as pd


data = []
# ------ANCHOR IMPORT DATA INTO AN ARRAY AND PRINT------

# def getData ():
#     global data
#     with open("src/data/test_data_1.csv", newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         data = []
#         for row in rows:
#             data.append(row)

#     # headers = data.pop(0)

#     #         data[row[0]] = row[1:]
#     # for key in data:
#     #     print (key, data[key][3])

#     return(data)


def getData(filePath):
    global data
    with open(filePath, 'r', newline="", encoding="utf8") as csvfile:
        # header = ["Planet", "Color", "Mass (10^24kg)", "Diameter (km)", "Density (kg/m^3)", "Escape Velocity (km/s)", "Rotation Period (hours)", "Distance from Sun (10^6 km)", "Perihelion (10^6 km)", "Aphelion (10^6 km)", "Orbital Velocity (km/s)", "Orbital Eccentricity", "Obliquity to Orbit (degrees)", "Mean Temperature (C)", "Number of Moons", "Ring System?", "Global Magnetic Field?"]
        dataset = csv.reader(csvfile)
        output = []
        for row in dataset:
            output.append(row)
    return output


filePath = ".Project\src\data\planets.csv"

# ------ANCHOR IMPORT DATA INTO AN ARRAY AND PRINT------

# def getMerge ():
#     with open("src/data/nzpropertytitleslatest2021.csv", newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         merge = []
#         for row in rows:
#             merge.append(row)

#     headers = merge.pop(0)

#     for row in merge:
#         data.append(row)

#     # data[row[0]] = row[1:]
#     # for key in data:
#     #     print (key, data[key][3])

#     return(data)


def append(newFile, currentFile):
    header = ["Planet", "Color", "Mass (10^24kg)", "Diameter (km)", "Density (kg/m^3)", "Escape Velocity (km/s)", "Rotation Period (hours)", "Distance from Sun (10^6 km)", "Perihelion (10^6 km)", "Aphelion (10^6 km)", "Orbital Velocity (km/s)", "Orbital Eccentricity", "Obliquity to Orbit (degrees)", "Mean Temperature (C)", "Number of Moons", "Ring System?", "Global Magnetic Field?"]
    # change header!!!
    with open(currentFile, 'a', newline="") as target_csvfile:
        writer = csv.writer(target_csvfile, header)
        for row in getData(newFile):
            writer.writerow(row)


newFile = ".Project\src\data\planets_2.csv"
currentFile = ".Project\src\data\planets_1.csv"

# if __name__ == "__main__":
#     print(append(newFile, currentFile))

# date = "2020/12/18 32465746"
# year, month = date.split(" ")[0].split("/")[0:2]
# print(year, month)


def readLocation(filePath):
    locationData = pd.read_csv(filePath,
                               usecols=["planet",
                                        ],
                               )
    return locationData


if __name__ == "__main__":
    print(getData(filePath))
    # print(getMerge())
    print(append(newFile, currentFile))
    print(getData(filePath))
