from pathlib import Path
import easygui
import codecs
import sys

class Padding:
    def __init__(self, start, end):
        self.start = round(start)
        self.end = round(end)

    def print(self, s):
        print(s + " padding start: " + str(self.start))
        print(s + " padding end: " + str(self.end))

class InputData:

    rightLightCount = 35
    leftLightCount = 43
    topLightCount = 63
    bottomLightCount = 82
    screenWidth = 2560
    screenHeight = 1440
    screenWidthIn = 24
    screenHeightIn = 14
    cor = 1
    cog = .64
    cob = .36
    rightP = Padding(2, 3)
    leftP = Padding(2, 3)
    bottomP = Padding(2, 3)
    topP = Padding(2, 3)
    length = 200
    iniFilePath = ""

    def toArray(self):
        return [
            self.rightLightCount,
            self.leftLightCount,
            self.topLightCount,
            self.bottomLightCount,
            self.screenWidth,
            self.screenHeight,
            self.screenWidthIn,
            self.screenHeightIn,
            self.cor,
            self.cog,
            self.cob,
            self.rightP.start,
            self.rightP.end,
            self.leftP.start,
            self.leftP.end,
            self.bottomP.start,
            self.bottomP.end,
            self.topP.start,
            self.topP.end,
            self.length,
            self.iniFilePath
            ]
    
    def print(self):

        print("right light count: " + str(self.rightLightCount))
        print("left light count: " + str(self.leftLightCount))
        print("top light count: " + str(self.topLightCount))
        print("bottom light count: " + str(self.bottomLightCount))
        print("screen width: " + str(self.screenWidth))
        print("screen height: " + str(self.screenHeight))
        print("screen width inches: " + str(self.screenWidthIn))
        print("screen height inches: " + str(self.screenHeightIn))

        self.rightP.print("right side")
        self.leftP.print("left side")
        self.bottomP.print("bottom side")
        self.topP.print("top side")

        print("red color coefficient: " + str(self.cor));
        print("green color coefficient: " + str(self.cog));
        print("blue color coefficient: " + str(self.cob));
        print("grabber length: " + str(self.length));



def retrieveUserInput():
    complete = False
    inData = InputData()

    #if fieldValues is None:
        
    while not complete:

        msg = "Generate light positions for prismatic .ini file"
        title = "Please fill out the information below."
        fieldNames = ["How many lights are on the right side of your screen?", 
                    "How many lights are on the left side of your screen?", 
                    "How many lights are on the top of your screen?",
                    "How many lights are on the bottom of your screen?",
                    "What is the width of your screen in pixels?",
                    "What is the height of your screen in pixels?",
                    "What is the width of your screen in Inches?",
                    "What is the height of your screen in Inches?",
                    "how many inches are the lights away from the bottom corner of the right side of your monitor?",
                    "how many inches are the lights away from the top corner of the right side of your monitor?",
                    "how many inches are the lights away from the right corner of the top of your monitor?",
                    "how many inches are the lights away from the left corner of the top of your monitor?",
                    "how many inches are the lights away from the top corner of the left side of your monitor?",
                    "how many inches are the lights away from the bottom corner of the left side of your monitor?",
                    "how many inches are the lights away from the left corner of the bottom of your monitor?",
                    "how many inches are the lights away from the right corner of the bottom of your monitor?",
                    "What is the red color coefficient of your led lights?",
                    "What is the green color coefficient of your led lights?",
                    "What is the blue color coefficient of your led lights?",
                    "What is the length of the color grabbers? (how close to the center of the screen would you like your lights to detect color? For 1440p I use 200 (px) as reference.)"
                    ]

        defaultValues = inData.toArray()

        for v in defaultValues:
            v = str(v)

        fieldValues = easygui.multenterbox(msg, title, fieldNames, defaultValues)

        if fieldValues is None:
            sys.exit(0)

        if easygui.msgbox("Please select the location of the prismatic .ini file you would like to modify. Normally stored in C:/Users/(name)/Prismatik/Profiles") is None:
            sys.exit(0)
            
        inData.iniFilePath = easygui.fileopenbox()

        if inData.iniFilePath is None:
            sys.exit(0)

        inData.rightLightCount  = int(fieldValues[0])
        inData.leftLightCount   = int(fieldValues[1])
        inData.topLightCount    = int(fieldValues[2])
        inData.bottomLightCount = int(fieldValues[3])
        inData.screenWidth      = int(fieldValues[4])
        inData.screenHeight     = int(fieldValues[5])
        inData.screenWidthIn    = float(fieldValues[6])
        inData.screenHeightIn   = float(fieldValues[7])
        inData.rightP.start     = float(fieldValues[8])
        inData.rightP.end       = float(fieldValues[9])
        inData.topP.start       = float(fieldValues[10])
        inData.topP.end         = float(fieldValues[11])
        inData.leftP.start      = float(fieldValues[12])
        inData.leftP.end        = float(fieldValues[13])
        inData.bottomP.start    = float(fieldValues[14])
        inData.bottomP.end      = float(fieldValues[15])
        inData.cor              = float(fieldValues[16])
        inData.cog              = float(fieldValues[17])
        inData.cob              = float(fieldValues[18])
        inData.length           = float(fieldValues[19])

        complete = True

    return inData    


dta = retrieveUserInput()
     
ScreenHeightPixelsToInch = dta.screenHeight /  dta.screenHeightIn
ScreenWidthPixelsToInch = dta.screenWidth /  dta.screenWidthIn

rightP = Padding(dta.rightP.start * ScreenHeightPixelsToInch, dta.rightP.end * ScreenHeightPixelsToInch)
leftP = Padding(dta.leftP.start * ScreenHeightPixelsToInch, dta.leftP.end  * ScreenHeightPixelsToInch)
topP = Padding( dta.topP.start * ScreenWidthPixelsToInch, dta.topP.end  * ScreenWidthPixelsToInch)
bottomP = Padding(dta.bottomP.start * ScreenWidthPixelsToInch, dta.bottomP.end * ScreenWidthPixelsToInch)
        

lightsR = dta.rightLightCount
lightsL = dta.leftLightCount
lightsT = dta.topLightCount
lightsB = dta.bottomLightCount

screenW = dta.screenWidth
screenH = dta.screenHeight

cor = dta.cor
cog = dta.cog
cob = dta.cob

grabberLength = dta.length

grabberWidth = 0#round(.25 * ScreenWidthPixelsToInch) #set to zero for auto width.

counter = 0

p = Path(dta.iniFilePath)
content = ""
with codecs.open(p, "r", "utf8") as file:
    content = file.read()
    try:
        index = content.index("[LED_1]")
        print(index)
        content = content[0: index:] + content[len(content)::]
    except:
        print("No led found")

content.strip()
content = content.replace('\r', '')

with open(p, "w") as file:
    file.write(content)

def outputLED(id, width, height, x, y, cor, cog, cob):
    with codecs.open(p, "a", "utf8") as f:
        f.write("[LED_" + str(int(id)) + "]\n")
        f.write("IsEnabled=true\n")
        f.write("Size=@Size(" + str(int(width)) + " " + str(int(height)) + ")\n")
        f.write("Position=@Point(" + str(int(x)) + " " + str(int(y)) + ")\n")
        f.write("CoefRed=" + str(cor))
        f.write("\nCoefGreen="+ str(cog))
        f.write("\nCoefBlue="+ str(cob))
        f.write("\n\n")

for x in range(1, lightsR + 1):
    counter = counter + 1
    width = grabberLength
    
    frameHeight = (screenH - rightP.start - rightP.end)
    
    height = round(frameHeight / lightsR) if grabberWidth == 0 else grabberWidth
    
    yp = frameHeight + rightP.end - round(height * x) - round(height / 2)
    xp = round(screenW) - width

    outputLED(counter, width, height, xp, yp, cor, cog, cob)
 
for x in range(1, lightsT + 1):
    counter = counter + 1
        
    frameWidth = (screenW - topP.start - topP.end)
    
    width = round((frameWidth / lightsT)) if grabberWidth == 0 else grabberWidth
    height = grabberLength
    yp = 0
    xp = topP.start + frameWidth - round(frameWidth / lightsT * x)

    outputLED(counter, width, height, xp, yp, cor, cog, cob)

for x in range(lightsL):
    counter = counter + 1
    width = grabberLength

    
    frameHeight = (screenH - leftP.start - leftP.end)
    
    height = round(frameHeight / lightsL) if grabberWidth == 0 else grabberWidth
    yp = round(height * x) + leftP.start - height
    
    xp = 0
    
    outputLED(counter, width, height, xp, yp, cor, cog, cob)
    
for x in range(lightsB):
    counter = counter + 1
    
    if counter >= 188:
        print("")

    frameWidth = (screenW - bottomP.start - bottomP.end)
    
    width = round((frameWidth / lightsB)) if grabberWidth == 0 else grabberWidth
    height = grabberLength
    yp = round(screenH) - height
    xp = round(frameWidth / lightsB * x) + bottomP.start
    
    outputLED(counter, width, height, xp, yp, cor, cog, cob)

if easygui.msgbox("Succesfully generated light values. Please refresh lightpack afterwards and change the appearance of the grab widgets to verify the results are correct.") is None:
    sys.exit(0)