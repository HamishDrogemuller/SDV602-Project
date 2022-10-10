import pandas as pd
import model.datacontroller as dc


def merge(newFile, currentFile):
    dc.append(newFile, currentFile)


def Diameter():  # piechart data
    data = dc.getData(dc.filePath)
    dictPie = {}
    for row in data:

        if row[3] in dictPie.keys():
            dictPie[row[3]] += 1
        else:
            dictPie[row[3]] = 1

    labels = list(dictPie.keys())
    values = list(dictPie.values())
    return labels, values


def moonCount():
    data = dc.getData(dc.filePath)
    data.pop(0)
    barData = {
        '0': 0,
        '1-10': 0,
        '11-20': 0,
        '21-50': 0,
        '51-100': 0
    }
    for row in data:
        size = float(row[19])

        if size in range(0, 0):
            barData['0'] += 1
        elif size in range(1, 10):
            barData['1-10'] += 1
        elif size in range(11, 20):
            barData['11-20'] += 1
        elif size in range(21, 50):
            barData['21-50'] += 1
        elif size in range(51, 100):
            barData['51-100'] += 1
    labels = list(barData.keys())
    values = list(barData.values())
    return labels, values



def locationData():
    locationData = dc.readLocation(dc.filePath)
    return locationData


if __name__ == "__main__":
    # print(Diameter())
    print(Diameter())
    # print(moonCount())
    print(moonCount())
    
