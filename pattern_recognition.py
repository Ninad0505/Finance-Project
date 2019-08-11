import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from functools import reduce
import time

def convert_date(date_bytes):
    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))

date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack = True, delimiter = ',', converters = {0: convert_date})

def percentChange(startpoint, currentpoint):
    try:
        x = ((float(currentpoint)-startpoint)/abs(startpoint))*100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0000001

def pattern_storage():

    x = len(avgLine)-60
    y = 31

    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y-30], avgLine[y-29])
        p2 = percentChange(avgLine[y - 30], avgLine[y - 28])
        p3 = percentChange(avgLine[y - 30], avgLine[y - 27])
        p4 = percentChange(avgLine[y - 30], avgLine[y - 26])
        p5 = percentChange(avgLine[y - 30], avgLine[y - 25])
        p6 = percentChange(avgLine[y - 30], avgLine[y - 24])
        p7 = percentChange(avgLine[y - 30], avgLine[y - 23])
        p8 = percentChange(avgLine[y - 30], avgLine[y - 22])
        p9 = percentChange(avgLine[y - 30], avgLine[y - 21])
        p10 = percentChange(avgLine[y - 30], avgLine[y - 20])

        p11 = percentChange(avgLine[y - 30], avgLine[y - 19])
        p12 = percentChange(avgLine[y - 30], avgLine[y - 18])
        p13 = percentChange(avgLine[y - 30], avgLine[y - 17])
        p14 = percentChange(avgLine[y - 30], avgLine[y - 16])
        p15 = percentChange(avgLine[y - 30], avgLine[y - 15])
        p16 = percentChange(avgLine[y - 30], avgLine[y - 14])
        p17 = percentChange(avgLine[y - 30], avgLine[y - 13])
        p18 = percentChange(avgLine[y - 30], avgLine[y - 12])
        p19 = percentChange(avgLine[y - 30], avgLine[y - 11])
        p20 = percentChange(avgLine[y - 30], avgLine[y - 10])

        p21 = percentChange(avgLine[y - 30], avgLine[y - 9])
        p22 = percentChange(avgLine[y - 30], avgLine[y - 8])
        p23 = percentChange(avgLine[y - 30], avgLine[y - 7])
        p24 = percentChange(avgLine[y - 30], avgLine[y - 6])
        p25 = percentChange(avgLine[y - 30], avgLine[y - 5])
        p26 = percentChange(avgLine[y - 30], avgLine[y - 4])
        p27 = percentChange(avgLine[y - 30], avgLine[y - 3])
        p28 = percentChange(avgLine[y - 30], avgLine[y - 2])
        p29 = percentChange(avgLine[y - 30], avgLine[y - 1])
        p30 = percentChange(avgLine[y - 30], avgLine[y])


        outcomeRange = avgLine[y + 20: y + 30]
        currentpoint = avgLine[y]

        try:
            avgOutcome = reduce(lambda x, y : x+y, outcomeRange)/len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentpoint, avgOutcome)
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)

        patternAR.append(pattern)
        performanceAR.append(futureOutcome)

        y += 1

def current_pattern():
    cp1 = percentChange(avgLine[-31], avgLine[-30])
    cp2 = percentChange(avgLine[-31], avgLine[-29])
    cp3 = percentChange(avgLine[-31], avgLine[-28])
    cp4 = percentChange(avgLine[-31], avgLine[-27])
    cp5 = percentChange(avgLine[-31], avgLine[-26])
    cp6 = percentChange(avgLine[-31], avgLine[-25])
    cp7 = percentChange(avgLine[-31], avgLine[-24])
    cp8 = percentChange(avgLine[-31], avgLine[-23])
    cp9 = percentChange(avgLine[-31], avgLine[-22])
    cp10 = percentChange(avgLine[-31], avgLine[-21])

    cp11 = percentChange(avgLine[-31], avgLine[-20])
    cp12 = percentChange(avgLine[-31], avgLine[-19])
    cp13 = percentChange(avgLine[-31], avgLine[-18])
    cp14 = percentChange(avgLine[-31], avgLine[-17])
    cp15 = percentChange(avgLine[-31], avgLine[-16])
    cp16 = percentChange(avgLine[-31], avgLine[-15])
    cp17 = percentChange(avgLine[-31], avgLine[-14])
    cp18 = percentChange(avgLine[-31], avgLine[-13])
    cp19 = percentChange(avgLine[-31], avgLine[-12])
    cp20 = percentChange(avgLine[-31], avgLine[-11])

    cp21 = percentChange(avgLine[-31], avgLine[-10])
    cp22 = percentChange(avgLine[-31], avgLine[-9])
    cp23 = percentChange(avgLine[-31], avgLine[-8])
    cp24 = percentChange(avgLine[-31], avgLine[-7])
    cp25 = percentChange(avgLine[-31], avgLine[-6])
    cp26 = percentChange(avgLine[-31], avgLine[-5])
    cp27 = percentChange(avgLine[-31], avgLine[-4])
    cp28 = percentChange(avgLine[-31], avgLine[-3])
    cp29 = percentChange(avgLine[-31], avgLine[-2])
    cp30 = percentChange(avgLine[-31], avgLine[-1])

    patforRec.append(cp1)
    patforRec.append(cp2)
    patforRec.append(cp3)
    patforRec.append(cp4)
    patforRec.append(cp5)
    patforRec.append(cp6)
    patforRec.append(cp7)
    patforRec.append(cp8)
    patforRec.append(cp9)
    patforRec.append(cp10)

    patforRec.append(cp11)
    patforRec.append(cp12)
    patforRec.append(cp13)
    patforRec.append(cp14)
    patforRec.append(cp15)
    patforRec.append(cp16)
    patforRec.append(cp17)
    patforRec.append(cp18)
    patforRec.append(cp19)
    patforRec.append(cp20)

    patforRec.append(cp21)
    patforRec.append(cp22)
    patforRec.append(cp23)
    patforRec.append(cp24)
    patforRec.append(cp25)
    patforRec.append(cp26)
    patforRec.append(cp27)
    patforRec.append(cp28)
    patforRec.append(cp29)
    patforRec.append(cp30)

def pattern_recognition():

    predictedOutcomesAR = []
    patfound = 0
    plotpatAR = []

    for eachpattern in patternAR:
        sim1 = 100.00 - abs(percentChange(eachpattern[0], patforRec[0]))
        sim2 = 100.00 - abs(percentChange(eachpattern[1], patforRec[1]))
        sim3 = 100.00 - abs(percentChange(eachpattern[2], patforRec[2]))
        sim4 = 100.00 - abs(percentChange(eachpattern[3], patforRec[3]))
        sim5 = 100.00 - abs(percentChange(eachpattern[4], patforRec[4]))
        sim6 = 100.00 - abs(percentChange(eachpattern[5], patforRec[5]))
        sim7 = 100.00 - abs(percentChange(eachpattern[6], patforRec[6]))
        sim8 = 100.00 - abs(percentChange(eachpattern[7], patforRec[7]))
        sim9 = 100.00 - abs(percentChange(eachpattern[8], patforRec[8]))
        sim10 = 100.00 - abs(percentChange(eachpattern[9], patforRec[9]))

        sim11 = 100.00 - abs(percentChange(eachpattern[10], patforRec[10]))
        sim12 = 100.00 - abs(percentChange(eachpattern[11], patforRec[11]))
        sim13 = 100.00 - abs(percentChange(eachpattern[12], patforRec[12]))
        sim14 = 100.00 - abs(percentChange(eachpattern[13], patforRec[13]))
        sim15 = 100.00 - abs(percentChange(eachpattern[14], patforRec[14]))
        sim16 = 100.00 - abs(percentChange(eachpattern[15], patforRec[15]))
        sim17 = 100.00 - abs(percentChange(eachpattern[16], patforRec[16]))
        sim18 = 100.00 - abs(percentChange(eachpattern[17], patforRec[17]))
        sim19 = 100.00 - abs(percentChange(eachpattern[18], patforRec[18]))
        sim20 = 100.00 - abs(percentChange(eachpattern[19], patforRec[19]))

        sim21 = 100.00 - abs(percentChange(eachpattern[20], patforRec[20]))
        sim22 = 100.00 - abs(percentChange(eachpattern[21], patforRec[21]))
        sim23 = 100.00 - abs(percentChange(eachpattern[22], patforRec[22]))
        sim24 = 100.00 - abs(percentChange(eachpattern[23], patforRec[23]))
        sim25 = 100.00 - abs(percentChange(eachpattern[24], patforRec[24]))
        sim26 = 100.00 - abs(percentChange(eachpattern[25], patforRec[25]))
        sim27 = 100.00 - abs(percentChange(eachpattern[26], patforRec[26]))
        sim28 = 100.00 - abs(percentChange(eachpattern[27], patforRec[27]))
        sim29 = 100.00 - abs(percentChange(eachpattern[28], patforRec[28]))
        sim30 = 100.00 - abs(percentChange(eachpattern[29], patforRec[29]))

        howSim = (sim1 + sim2 + sim3 + sim4 + sim5 + sim6 + sim7 + sim8 + sim9 + sim10 + sim11 + sim12 + sim13 + sim14 + sim15 + sim16 + sim17 + sim18 + sim19 + sim20 + sim21 + sim22 + sim23 + sim24 + sim25 + sim26 + sim27 + sim28 + sim29 + sim30) / 30.00
        # print(howSim)
        if howSim > 70:
            patdex = patternAR.index(eachpattern)
            patfound = 1
            # print('///////////////')
            # print('###############')
            # print(patforRec)
            # print('---------------')
            # print(eachpattern)
            # print('===============')
            # print('predicted outcome is', performanceAR[patdex])
            xp = []
            for x in range(1, 31):
                xp.append(x)

            plotpatAR.append(eachpattern)

    if patfound == 1:
        plt.figure(figsize=(10,6))
        for eachpatt in plotpatAR:
            futurePoints = patternAR.index(eachpatt)

            if performanceAR[futurePoints] > patforRec[29]:
                pcolor = '#24bc00'
            else:
                pcolor = '#d40000'
            plt.plot(xp, eachpatt)
            predictedOutcomesAR.append(performanceAR[futurePoints])
            plt.scatter(35, performanceAR[futurePoints], c = pcolor, alpha = .3)   #here alpha denotes the changing intensity if points overlap

        realOutcomeRange = alldata[toWhat+20:toWhat+30]
        realAvgoutcome = reduce(lambda x,y : x+y, realOutcomeRange)/len(realOutcomeRange)
        realMovement = percentChange(alldata[toWhat], realAvgoutcome)
        predictedAvgoutcome = reduce(lambda x, y: x + y, predictedOutcomesAR) / len(predictedOutcomesAR)

        plt.scatter(40, realMovement, c='#54fff7', s=25)
        plt.scatter(40, predictedAvgoutcome, c='b', s=25)

        plt.plot(xp, patforRec, '#54fff7', linewidth = 5)
        plt.grid(True)
        plt.title('Pattern Recognition')
        plt.show()

dataLength = int(bid.shape[0])
print('data length is', dataLength)

toWhat = 37000
alldata = (ask + bid) / 2

while toWhat < dataLength:
    # avgLine = (ask + bid) / 2
    avgLine = alldata[:toWhat]

    patternAR = []
    performanceAR = []
    patforRec = []

    pattern_storage()
    current_pattern()
    pattern_recognition()
    moveon = input('press ENTER to continue....')
    toWhat += 1











