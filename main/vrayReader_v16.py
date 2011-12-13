# -*- coding: utf-8 -*-

#################################################################

def printLine(x, y):
    ''' a function to get the line number you desire and print it for you, x is the file path, y is the line number '''

    filePath01 = x
    counter = 1 # to count the lines
    file01 = open(filePath01) # file object for the file at the path.
    fileDict = {} # dictionary to hold the line information (line, line lenght(optional), characters)
    readingFile = True # just a variable for the while loop

    while readingFile != '':
      readingFile = file01.readline()
      readingFile
      #print readingFile
      positionFile = file01.tell()
      fileDict[counter] = positionFile
      counter += 1

    if y <= counter and y != 1:
      file01.seek(fileDict[y-1])
      result = file01.readline()
      resultWithoutSpecial = result[:-1]
      file01.seek(0)
      return resultWithoutSpecial
    elif y == 1:
      file01.seek(0)
      result = file01.readline()
      file01.seek(0)
      return result
    else:
      print "there is only %s lines in the file, please enter a smaller number" % counter
      return

#################################################################

def returnToLine(x, y):
    ''' a function to return the line at the line number you desire, x is the file object, y is the line number '''

    counter = 1 # to count the lines
    file01 = x # file object given
    fileDict = {} # dictionary to hold the line information (line, line lenght(optional), characters)
    readingFile = True # just a variable for the while loop

    while readingFile != '':
      readingFile = file01.readline()
      readingFile
      positionFile = file01.tell()
      fileDict[counter] = positionFile
      counter += 1

    if y <= counter and y != 1:
      file01.seek(fileDict[y-1])
      result = file01.readline()
      resultWithoutSpecial = result[:-1]
      #print fileDict
      file01.seek(0)
      return resultWithoutSpecial
    elif y == 1:
      file01.seek(0)
      result = file01.readline()
      resultWithoutSpecial = result[:-1]
      #print fileDict
      file01.seek(0)
      return resultWithoutSpecial
    else:
      print "there is only %s lines in the file, please enter a smaller number" % counter
      file01.seek(0)
      return False

#################################################################

def giveLine(x, y):
    ''' a function to return the line location for the line number you desire (for .seek method), x is the file object, y is the line number '''

    counter = 1 # to count the lines
    file01 = x # file object given
    fileDict = {} # dictionary to hold the line information (line, line lenght(optional), characters)
    readingFile = True # just a variable for the while loop
    file01.seek(0)

    while readingFile != '':
      readingFile = file01.readline()
      readingFile
      positionFile = file01.tell()
      fileDict[counter] = positionFile
      counter += 1

    if y <= counter and y != 1:
      #print fileDict
      file01.seek(0)
      return fileDict[y-1]
    elif y == 1:
      #print fileFict
      file01.seek(0)
      return 0
    else:
      #print fileDict
      file01.seek(0)
      return False

#################################################################

def filename(x):
    """gets a filename, returns the basename and the extension"""
    value = -1
    counter = -1
    name = x
    lenName = len(name)
    while abs(counter) < lenName:
      if name[counter] == ".":
          value = counter
          break
      else:
          counter -= 1
    if abs(counter) == lenName:
      print "there are no '.' in this file name"
      return None
    #print counter
    return (name[:counter],name[lenName + counter :])
    # add one to the counter if you dont want to get the "."

#################################################################

def createFileCorrected(x,y):
    """ gets a path for a file and creates a similarly named filed called, x_y.(extension for x)
    - x and y are strings"""
   
    import os.path as osp
   
    xInfo = osp.split(x)
    zFilename = filename(xInfo[1]) # gets you the basefilename and the extension in a tuple
    postscript = "_" + y # _extension for the file
    z = xInfo[0] + "/" +zFilename[0] + postscript + zFilename[1]
    exists = osp.exists(z) # does the file exist?
    if exists == True:
        print "a file of given name exists, please choose a different name"
        #raise ("a file of given name exists, please choose a different name")
    else:
        return z

#################################################################

def compareAtoB(a,b,extension, errorLine):
    """ compares the a to b, and overwrites any line that both file has with the 'errorLine' """

    a_corr = createFileCorrected(a,extension) # createTheNecessaryFile

    readingFile_a = True # variable for the while loop
    readingFile_b = True # variable for the while loop

    file_a = open(a)
    file_b = open(b)
    file_a_corr = file(a_corr, "wt")

    while readingFile_a != '':
       aTrue = False
       readingFile_a = file_a.readline()
       while readingFile_b != '':
         readingFile_b = file_b.readline()
         if readingFile_a == readingFile_b:
             file_a_corr.write(errorLine)
             aTrue = True
             break
       file_b.seek(0)
       readingFile_b = True
       if aTrue == False:
          file_a_corr.write(readingFile_a)

    file_a.close()
    file_b.close()
    file_a_corr.flush()
    return a_corr

#################################################################

def compareBoth(a,b,extension,errorLine):
    """takes two file, a and b, creates copies of them '*_extension' and overwrites the lines that are common in both files on the copies"""
    compareAtoB(a,b,extension,errorLine)
    compareAtoB(b,a,extension,errorLine)
    print "comparison is done"
    return

#################################################################

def truncateComparisonFile(c, extension_c, errorLine):

    c_truncated = createFileCorrected(c,extension_c)
  
    file_c = open(c)
    file_c_truncated = file(c_truncated, "wt")
  
    beginningStatement = "\nBEGINNING OF FILE:\n%s\n\n" % c
    endStatement = "\nEND OF FILE:\n%s\n\n" % c

    currentLine = 0
    readingFile = True
    file_c_truncated.write(beginningStatement)
    while currentLine != '':
       previousLine = currentLine
       currentLine = file_c.readline()
       if currentLine != errorLine:
           if previousLine == errorLine:
               file_c_truncated.write(errorLine)
               file_c_truncated.write(currentLine)
           else:
               file_c_truncated.write(currentLine)
    file_c_truncated.write(endStatement)
    file_c_truncated.flush()
    return c_truncated

#################################################################

def createUnifyFileName(a,b,extensionUnify):
    """ given two file paths 'a' and 'b' creates a file path for c called 'a_b_extension', in the folder of a and the extension of a """

    import os.path as osp
 
    aInfo = osp.split(a)
    bInfo = osp.split(b)
  
    aFilename = filename(aInfo[1]) # gets you the basefilename and the extension in a tuple
    bFilename = filename(bInfo[1]) # gets you the basefilename and the extension in a tuple
    postscript = "_" + extensionUnify # _extension for the file
    unifiedName = aInfo[0] + "/" + aFilename[0]+ "_" + bFilename[0] + postscript + aFilename[1]
    exists = osp.exists(unifiedName) # does the file exist?
    if exists == True:
      print "a file of given name exists, please choose a different name"
      #raise ("a file of given name exists, please choose a different name")
    else:
      return unifiedName

#################################################################


#d = "/home/engin/Documents/python_file_testing/01_corrected_truncated.ma"
#e = "/home/engin/Documents/python_file_testing/01_corrected_truncated_02.ma"

def unifyFile(d,e):
    """ combines two seperate files in one file, (for my truncate script) """
    file_d = open(d)
    file_e = open(e)

    line_d = True # initialize some variables
    line_e = True

    extensionUnify = "unified"
    unifiedFile = createUnifyFileName(d,e,extensionUnify)
    fileUnify = file(unifiedFile, "wt")

    while line_d != '':
       line_d = file_d.readline()
       fileUnify.write(line_d)
    while line_e != '':
       line_e = file_e.readline()
       fileUnify.write(line_e)
    fileUnify.flush()
    return fileUnify

#################################################################

def compareTruncate(a,b,extension, errorLine):
    """takes two file, a and a, creates copies of them '*_extension' and overwrites the lines that are common in both files on the copies"""
    extension_c = "truncated"
    file01 = compareAtoB(a,b,extension,errorLine)
    file02 = compareAtoB(b,a,extension,errorLine)
    file01_t = truncateComparisonFile(file01, extension_c, errorLine)
    file02_t = truncateComparisonFile(file02, extension_c, errorLine)
    unifyFile(file01_t, file02_t)
    print "comparison is done"
    return

###################################################### COMPARE TRUNCATE WORK AREA

"""

#work:
#a = '/USERS/engin/testing/test_light.ma'
#b = '/USERS/engin/testing/test_light_02.ma'

a = '/USERS/engin/testing/v01/backup/defaultValues_06.ma'
# a_c = '/USERS/engin/testing/v02/ND480_lighting_v18_corrected.ma'
b = '/USERS/engin/testing/v01/backup/defaultValues_06_a.ma'
# b_c = '/USERS/engin/testing/v01/ND480_lighting_v19_corrected.ma'

#home:
#a = "/home/engin/Documents/python_file_testing/00.ma"
#b = "/home/engin/Documents/python_file_testing/01.ma"

extension = "corrected"
extensionUnify = "unified"
errorLine = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
#c = "/home/engin/Documents/python_file_testing/01_corrected.ma"
#extension_c= "truncated"

compareTruncate(a,b,extension, errorLine)

"""

######################################################

"""
filePath = '/USERS/engin/testing/v01/a_c_t.ma'
fileActive = open(filePath)
readingFile = True
counter = 0
while readingFile != '':
    readingFile = fileActive.readline()
    counter += 1
    #print "%d" % len(readingFile) + " " + "%d" % counter
    if counter == 21:
        print readingFile[:21]
    if readingFile[:22] == '    setAttr ".mSceneName"':
        print "success"
        print counter
        break
fileActive.close()
"""

"""
filePath = '/USERS/engin/testing/v01/a_c_t.ma'
fileNewPath = createFileCorrected(filePath,"modified")
fileActive = open(filePath)
fileNew = file(fileNewPath, "wt")
readingFile = True
counter = 0
while readingFile != '':
    readingFile = fileActive.readline()
    counter += 1
    if readingFile[:22] == '    setAttr ".mSceneName"':
        readingFile = '        setAttr ".mSceneName" -type "string" "%s";\n' % fileNewPath
        #setAttr ".mSceneName" -type "string" "/USERS/engin/testing/v01/HE200_v01_anchorIn_5.ma";
        #print counter
    fileNew.write(readingFile)
fileActive.close()
fileNew.close()
"""

"""
filePath = '/USERS/engin/testing/v01/a_c_t.ma'
fileNewPath = createFileCorrected(filePath,"modified")
fileActive = open(filePath)
fileNew = file(fileNewPath, "wt")
readingFile = True
counter = 0
vraySettings = []

while readingFile != '':
    readingFile = fileActive.readline()
    counter += 1
    if readingFile[:47] == 'createNode VRaySettingsNode -s -n "vraySettings"':
        readingVrayAttribute = fileActive.readline()
        while readingVrayAttribute[:7] == '    setAttr':
            readingVrayAttribute = fileActive.readline()
           


           
        #readingFile = '        setAttr ".mSceneName" -type "string" "%s";\n' % fileNewPath
        #setAttr ".mSceneName" -type "string" "/USERS/engin/testing/v01/HE200_v01_anchorIn_5.ma";
    fileNew.write(readingFile)

fileActive.close()
fileNew.close()
"""

###################################################### ATTRIBUTE READER

listValue = {}
listValue['gogdh']  = ('never', 'auto', 'always') # hidden geo
listValue['goldhl'] = ('never', 'auto', 'always') # hidden lights
listValue['st'] = ('fixed type', 'adaptive dmc', 'adaptive subd')
listValue['aaft'] = ('box', 'area', 'triangle', 'lanczos', 'sinc', 'catmullrom', 'gaussian', 'cook')
listValue['cmtp'] = ('linear multiply', 'exponential', 'hsv exponential', 'intensity exponential', 'gamma correction', 'intesity gamma', 'reinhard')

listParam = {} # list of parameters and their default values
categories = {}

# GLOBAL OPTIONS

categories[0] = ('gogd', 'gogdh', 'gobc', 'gorvs', 'gumsfp')
# CATEGORY : 0 Global Options - Geometry
listParam['gogd'] = ('displacement', 'yes', 'main')
listParam['gogdh'] = ('hidden geometry', '1', 'main')
listParam['gobc'] = ('force back face culling', '1', 'main')
listParam['gorvs'] = ('render viewport subdivision', 'no', 'main')
listParam['gumsfp'] = ('use maya shader for VRay proxies', 'no', 'main')

categories[1] = ('goldl', 'golddl', 'goldhl', 'golds', 'gologi', 'gogdri')
# CATEGORY : 1 Global Options - Lighting and GI
listParam['goldl'] = ('lights', 'yes', 'main')
listParam['golddl'] = ('default lights', 'yes', 'main')
listParam['goldhl'] = ('hidden lights', '1', 'main')
listParam['golds'] = ('shadows', 'yes', 'main')
listParam['gologi'] = ('show gi only', 'no', 'main')
listParam['gogdri'] = ('dont render final image', 'no', 'main')

categories[2] = ('gomrr', 'gomld', 'gommd', 'gomdm', 'gomfm', 'gomg', 'gomtml', 'gomtc', 'gomb')
# CATEGORY : 2 Global Options - Materials and Raytracing
listParam['gomrr'] = ('reflection/refraction', 'yes', 'main')
listParam['gomld'] = ('global max depth', 'no', 'main')
listParam['gommd'] = ('max depth', '5', ('gomld', 'yes'))
listParam['gomdm'] = ('maps', 'yes', 'main')
listParam['gomfm'] = ('filter maps', 'yes', 'main')
listParam['gomg'] = ('glossy effects', 'yes', 'main')
listParam['gomtml'] = ('max transparency levels', '50', 'main')
listParam['gomtc'] = ('transparency cut-off', '0.001', 'main')
listParam['gomb'] = ('secondary ray-bias', '0', 'main')

categories[3] = ('st', )
# CATEGORY : 3 Global Options - AA type
listParam['st'] = ('antialiasing type', '2', 'main')

categories[4] = ('aafon', 'aaft', 'aafs')
# CATEGORY : 4 Global Options - Filter
listParam['aafon'] = ('filter on/off', 'yes', 'main')
listParam['aaft'] = ('aa filter type', '1', ('aafon', 'yes'))
listParam['aafs'] = ('aa filter size', '1.5', ('aafon', 'yes'))

categories[5] = ('smi', 'sma', 'sji', 'tre', 'sde', 'sno', 'snot', 'sss')
# CATEGORY : 5 Global Options - Adaptive Subd
listParam['smi'] = ('adaptive subd min', '-1', ('st', '2'))
listParam['sma'] = ('adaptive subd max', '2', ('st', '2'))
listParam['sji'] = ('jitter', 'yes', ('st', '2'))
listParam['tre'] = ('threshold', '0.150', ('st', '2'))
listParam['sde'] = ('edges', 'yes', ('st', '2'))
listParam['sno'] = ('normals', 'yes', ('st', '2'))
listParam['snot'] = ('normals threshold', '0.100', ('st', '2'))
listParam['sss'] = ('show samples', 'no', ('st', '2'))

categories[6] = ('dmi', 'dma', 'dmlt', 'dmt', 'dss')
# CATEGORY : 6 Global Options - Adaptive DMC
listParam['dmi'] = ('antialiasing min samples', '1', ('st', '1'))
listParam['dma'] = ('antialiasing max samples', '4', ('st', '1'))
listParam['dmlt'] = ('lock threshold to dmc sampler', 'no', ('st', '1'))
listParam['dmt'] = ('antialiasing threshold', '0.01', ('dmlt', 'no')) # two parents?
listParam['dss'] = ('show samples', 'no', ('st', '1'))

categories[7] = ('fsd', )
# CATEGORY : 7 Global Options - Fixed
listParam['fsd'] = ('antialiasing fixed subdivision', '1', ('st', '0'))

categories[8] = ('cmtp', 'cmdm', 'cmbm', 'cg', 'cmab', 'cmco', 'cmcl', 'cmsm', 'cmao', 'cmlw', 'cmas')
# CATEGORY : 8 Global Options - Color Mapping
listParam['cmtp'] = ('color mapping type', '0', 'main')
listParam['cmdm'] = ('dark multiplier', '1', 'main')
listParam['cmbm'] = ('bright multiplier', '1', 'main')
listParam['cg'] = ('gamma', '1', 'main')
listParam['cmab'] = ('affect background', 'yes', 'main')
listParam['cmco'] = ('clamp output', 'no', 'main')
listParam['cmcl'] = ('clamp level', '1', ('cmco', 'yes'))
listParam['cmsm'] = ('subpixel mapping', 'no', 'main')
listParam['cmao'] = ('dont affect colors', 'no', 'main')
listParam['cmlw'] = ('linear workflow', 'no', 'main')
listParam['cmas'] = ('affect swatches', 'no', 'main')

categories[9] = ('camon', 'cammb', 'camdur', 'camic', 'cabias', 'camsd', 'casef', 'capps', 'camgs')
# CATEGORY : 9 Global Options - Camera
listParam['camon'] = ('motion blur', 'no', 'main')
listParam['cammb'] = ('camera motion blur', 'yes', 'main')
listParam['camdur'] = ('duration', '1', ('camon', 'yes'))
listParam['camic'] = ('interval center', '1', ('camon', 'yes'))
listParam['cabias'] = ('bias', '0', ('camon', 'yes'))
listParam['camsd'] = ('subdivs', '6', ('camon', 'yes'))
listParam['casef'] = ('shutter efficiency', '1', ('camon', 'yes'))
listParam['capps'] = ('prepass samples', '1', 'main')
listParam['camgs'] = ('geometry samples', '2', 'main')

categories[10] = ('bmpm', 'tfsm', 'phsc', 'neg')
# CATEGORY : 10 Global Options - Misc
listParam['bmpm'] = ('global bump map multiplier', '1', 'main')
listParam['tfsm'] = ('global texture filter scale multiplier', '1', 'main')
listParam['phsc'] = ('photometric lights scale', '20', 'main')
listParam['neg'] = ('allow negative shader colors', 'no', 'main')

categories[11] = ('dmcstd', 'dmcsaa', 'dmcsat', 'dmcsams', 'dmcssm')
# CATEGORY : 11 Global Options - DMC
listParam['dmcstd'] = ('time dependent', 'no', 'main')
listParam['dmcsaa'] = ('dmc adaptive amount', '0.850', 'main')
listParam['dmcsat'] = ('dmc adaptive threshold', '0.01', 'main')
listParam['dmcsams'] = ('adaptive min amount', '8', 'main')
listParam['dmcssm'] = ('subdivs multiplier', '1', 'main')

#categoriesAll
categories['categoryMax'] = listParam.keys()

"""
listParam['gi'] =  ('gi on/off')

listParam['iminr'] = ('irradiance min amount')
listParam['imaxr'] = ('irradiance max amount')
listParam['isds'] = ('irradiance subdivision')
listParam['itps'] = ('irradiance interpolation')
listParam['itpfs'] = ('irradiance frames')
listParam['icts'] = ('irradiance color threshold')
listParam['ints'] = ('irradiance normal threshold')
listParam['idts'] = ('irradiance distance threshold')
listParam['idr'] = ('detail enhancement distance')
listParam['ids'] = ('detail enhancement subdivs')


listParam['ddel'] = ('default displacement')
listParam['ddms'] = ('max subdivs disp')
listParam['dda'] = ('amount subdivsions')
listParam['srdml'] = ('dynamic memory limit')
listParam['srgx'] = ('render region x')
listParam['srgy'] = ('render region y')
"""


######################################################################
filePath = '/USERS/engin/testing/v01/backup/defaultValues_06_d.ma'
######################################################################

def setAttrReader(varName):
    """return the attribute alias and the value"""

    lenghtVariable = len(varName)
    counter = 0

    variable = [] # list for the variable
    flag = [] # list for the flag
    value = [] # list for the characters

    variableFinal = " "
    flagFinal = " "
    valueFinal = 0

    varNameInv = varName[::-1]
   
    varName = varName.strip() #get rid of the whitespace, actually dangerous because you want the setAttrs with whitespace infront of it...
    if varName[:7] == 'setAttr':
        counter = 0
        for i in varName:
            if i == '"': # check for the first statement in "..."
                internalCounterVar = counter + 2 # to skip the '"' and the '.'
                while varName[internalCounterVar] != '"' and counter <= lenghtVariable:
                    variable.append(varName[internalCounterVar])
                    internalCounterVar += 1
                variableFinal = "".join(variable) # convert the list of characters into a string
                break # done with whatever inside "...."
            else:
                pass
            counter += 1

        for m in varNameInv: # reading the list from the opposite, for the value
            counter = 0
            if m == ";": #checking for the value
                internalCounterValue = counter -2 # to skip the ';'
                while varName[internalCounterValue] != " " and -counter <= lenghtVariable:
                    value.append(varName[internalCounterValue])
                    internalCounterValue -= 1
                value.reverse()
                valueFinal = "".join(value)
                if valueFinal[0] == '"': #for the strings you will need the string flag
                    valueFinal = '-type "string" ' + valueFinal
                break
            else:
                pass
            counter += 1
       
    else:
        print "not a setAttr line"
        return
    result = [variableFinal, valueFinal]
    return result

def VRayProperties(filePath):
    """ returns a dictionary of variable and value couples, uses the setAttrReader function """
    fileActive = open(filePath)
    readingFile = True
    containsVray = False
    VRayPropertyDict = {}

    while readingFile != '':
        readingFile = fileActive.readline()
        if readingFile[:27] == 'createNode VRaySettingsNode':
            containsVray = True
            startVrayAtts = True
            while startVrayAtts == True:
                readingFile = fileActive.readline()
                if readingFile[:8] == '    setAttr':
                    result = setAttrReader(readingFile)
                    VRayPropertyDict[result[0]] = result[1]
                else:
                    startVrayAtts = False
        else:
            if readingFile == '':
                if containsVray ==False:
                    print "this file does not contain a VRaySettingsNode"

    fileActive.close()
    return VRayPropertyDict


######################################################################
propertyDict = VRayProperties(filePath)
######################################################################

def checkDefault02(propertyDict, categoryNo = 'categoryMax'):
    """ checks the given propertyDict against the dictionary of full values and returns a list of values that are at default, hence not displayed """
    currentCategory = categories[categoryNo]
    propertyDictDefault = {}
    for i in currentCategory:
        isDefaultValue = True
        if propertyDict.get(i) != None:
            isDefaultValue = False ### this means that I am finding a corresponding value, so it is not default...
        if isDefaultValue == True:
            propertyDictDefault[i] = listParam[i][1]
    return propertyDictDefault

######################################################################
aa = checkDefault02(propertyDict)
######################################################################

""" some properties should only be displayed if a parent property is of certain value, this is the function to ensure that"""
""" if a property has the value 'main' in it, it is always displayed """

def eligibleToDisplay(propertyDict, categoryNo = 'categoryMax'):
    """ some properties should only be displayed if a parent property is of certain value, this is the function to ensure that"""
    """ if a property has the value 'main' in it, it is always displayed """
    """ cant work on only default values, should be working on all the values available.. default + given"""

    properties = propertyDict
    eligibleToDisplay = {}
    currentCategory = categories[categoryNo]

    for itemKey in properties:
        for item in currentCategory:
            if itemKey == item:
                if listParam[itemKey][2] == 'main': ### is the listParam[key][2] == main, if so this is a non-child object and should be displayed
                    eligibleToDisplay[itemKey] = properties[itemKey]
                else:
                    #print itemKey
                    if listParam[itemKey][2][1] == propertyDict[listParam[itemKey][2][0]]:
                        ### is the listParam[key][2][1] == parents required value, if true this should be displayed
                        eligibleToDisplay[itemKey] = properties[itemKey]
                    else:
                        pass

    return eligibleToDisplay

def returnVRayPropertyDict(filePath, categoryNo = 'categoryMax'):
    """ returns the dictionary of the values that a file has in a certain category"""
   
    properties = VRayProperties(filePath) # properties in a dictionary as key value couples

    currentCategory = categories[categoryNo]
   
    propertyDict = {} # long names for the properties, switching the alias to the real name
    propertyDictDefault = {} # properties that are not included in the file, the default properties
    tempDict = {}
    finalDict = {}
   
    # listParam is the dictionary containing the long names

    for key in properties:
        if listParam.get(key) != None:
            propertyDict[key] = properties[key]


    # add the default values in, (they dont appear in the .ma file)
    # default values should only be added if they are relavant,
    # meaning if they are parents or a child of a parent in display
   
    propertyDictDefault = checkDefault02(propertyDict, categoryNo = 'categoryMax')

    tempDict = dict(propertyDict.items() + propertyDictDefault.items())

    finalDict = eligibleToDisplay(tempDict, categoryNo)
                        
    return finalDict

def returnVRayPropertyDictNoHier(filePath, categoryNo = 'categoryMax'):
    """ returns the dictionary of the values that a file has in a certain category, without any respect to the hierarchy"""
   
    properties = VRayProperties(filePath) # properties in a dictionary as key value couples

    currentCategory = categories[categoryNo]
   
    propertyDict = {} # long names for the properties, switching the alias to the real name
    propertyDictDefault = {} # properties that are not included in the file, the default properties
    tempDict = {}
    finalDict = {}
   
    # listParam is the dictionary containing the long names

    for key in properties:
        if listParam.get(key) != None:
            propertyDict[key] = properties[key]


    # add the default values in, (they dont appear in the .ma file)
    # default values should only be added if they are relavant,
    # meaning if they are parents or a child of a parent in display
   
    propertyDictDefault = checkDefault02(propertyDict, categoryNo = 'categoryMax')

    finalDict = dict(propertyDict.items() + propertyDictDefault.items())
                        
    return finalDict

######################################################################
bb = returnVRayPropertyDict(filePath)
bbNoHier = returnVRayPropertyDictNoHier(filePath)
######################################################################


def returnTheFullValue02(propertyDict, categoryNo = 'categoryMax'):
    """there are handful of parameters that are not numeric but strings (such as filter typ) that are defined by numbers, this converts the numbers to actual names"""
    """expects a list of shorthand name of parameters to work with, defaults to listParam"""
    """it is for dipslay purposes, the result is not to be used with internal calculations"""
    """ uses the 'listValue' dictionary"""
   
    categoryList = []
    currentCategory = categories[categoryNo]

    for key in propertyDict:
        for item in currentCategory:
            if key == item:
                isTrue = listValue.get(key)
                if isTrue != None:
                    try:
                        itemList01Int = int(propertyDict[key])
                    except ValueError:
                        itemList01Int = None
                    if itemList01Int != None:
                        propertyDict[key] = listValue[key][itemList01Int]

    return propertyDict

def printOutDict(propertyDict, categoryNo = 'categoryMax'):
    """given the dictionary it prints out an legible list of the parameters"""
    printOutDictTemp = {}
    printOutDictFinal = {}
    currentCategory = categories[categoryNo]

    for key in propertyDict:
        for item in currentCategory:
            if key == item:
                printOutDictTemp[key] = propertyDict[key]

    printOutDictTemp = returnTheFullValue02(printOutDictTemp, categoryNo)

    for i in printOutDictTemp:
        printOutDictFinal[listParam[i][0]] = printOutDictTemp[i]

    #for j in printOutDictFinal.iteritems():
    #    print j

    categoryNo = 'categoryMax'
    if categoryNo == 'categoryMax':
        for category in categories:
            if type(category) == int:
                print "category %d:\n" % category
                for item in categories[category]:
                    try:
                        print (listParam[item][0], printOutDictFinal[listParam[item][0]])
                    except KeyError:
                        pass
                print "\n"
       

    return printOutDictFinal

######################################################################
#printOutDictFinal = printOutDict(bbNoHier)
######################################################################


  
def readSceneName(filePath):
    """reads in the mSceneName value and returns the file path part of it"""
   
    listName = []
    listNameFinal = []
    counter = len(filePath)-1
    counter02 = 1
    while counter >= 0 and counter02 <= 2:
        character = filePath[counter]
        listName.append(character)
        counter -= 1
        if character == '"':
            counter02 += 1
    listName.reverse()
    for char in listName:
        if char != '"':
            listNameFinal.append(char)

    name = "".join(listNameFinal)

    return name

def changeExtension(filePath):
    """ given a file path, it turns the same file (and path) but with .txt extension instead """

    import os.path as osp

    targetExtension = '.txt' # desired file extension

    filePathLenght = len(filePath)
    filePathParts = osp.split(filePath)
    fileNameParts = filename(filePathParts[1])
    fileExtension = fileNameParts[1]
    extensionLenght = len(fileExtension)

    newPath = filePath[:filePathLenght - extensionLenght] + targetExtension

    return newPath

def printOutDictWriteOut(filePath, categoryNo = 'categoryMax'):
    """given the dictionary it writes out a legible list of files"""

    propertyDictOriginal = VRayProperties(filePath)
    sceneNameFlag = propertyDictOriginal.get('mSceneName')
    sceneName = readSceneName(sceneNameFlag) #scene name without the flags
    sceneNameTxt = changeExtension(sceneName)

    defaultDestination = createFileCorrected(sceneName, 'default') # default destination path, to be changed by the user.
   
    propertyDict = returnVRayPropertyDictNoHier(filePath, categoryNo = 'categoryMax')
       
    printOutDictTemp = {}
    printOutDictFinal = {}
    currentCategory = categories[categoryNo]

    for key in propertyDict:
        for item in currentCategory:
            if key == item:
                printOutDictTemp[key] = propertyDict[key]

    printOutDictTemp = returnTheFullValue02(printOutDictTemp, categoryNo)

    for i in printOutDictTemp:
        printOutDictFinal[listParam[i][0]] = printOutDictTemp[i]

    propertiesFile = file(sceneNameTxt, "wt")

    propertiesFile.write("scene file:\n")
    propertiesFile.write(sceneName)
    propertiesFile.write("\n")
    propertiesFile.write("destination file:\n")
    propertiesFile.write(defaultDestination)
    propertiesFile.write("\n")
    propertiesFile.write("\n")

       
    if categoryNo == 'categoryMax':
        for category in categories:
            if type(category) == int:
                propertiesFile.write("CATEGORY %d:\n" % category)
                for item in categories[category]:
                    try:
                        propertiesFile.write(listParam[item][0] + ":" + printOutDictFinal[listParam[item][0]] +"\n")
                    except KeyError:
                        pass
                propertiesFile.write("\n")

    propertiesFile.flush()

    return sceneNameTxt


filePath = '/USERS/engin/testing/v01/backup/defaultValues_06_d.ma'
printOutDictFinal = printOutDictWriteOut(filePath)

#################################################################

""" read the txt file that is created by the above script to create a sceneFile from source with the changed settings """

readingFile_a = True # variable for the while loop
readingFile_b = True # variable for the while loop


file_a = open(printOutDictFinal)

while readingFile_a != '':
   aTrue = False
   readingFile_a = file_a.readline()
   while readingFile_b != '':
     readingFile_b = file_b.readline()
     if readingFile_a == readingFile_b:
         file_a_corr.write(errorLine)
         aTrue = True
         break
   file_b.seek(0)
   readingFile_b = True
   if aTrue == False:
      file_a_corr.write(readingFile_a)

file_a.close()






def createFileCorrected(x,y):
    """ gets a path for a file and creates a similarly named filed called, x_y.(extension for x)
    - x and y are strings"""
   
    import os.path as osp
   
    xInfo = osp.split(x)
    zFilename = filename(xInfo[1]) # gets you the basefilename and the extension in a tuple
    postscript = "_" + y # _extension for the file
    z = xInfo[0] + "/" +zFilename[0] + postscript + zFilename[1]
    exists = osp.exists(z) # does the file exist?
    if exists == True:
        print "a file of given name exists, please choose a different name"
        #raise ("a file of given name exists, please choose a different name")
    else:
        return z

#################################################################

def compareAtoB(a,b,extension, errorLine):
    """ compares the a to b, and overwrites any line that both file has with the 'errorLine' """

    a_corr = createFileCorrected(a,extension) # createTheNecessaryFile

    readingFile_a = True # variable for the while loop
    readingFile_b = True # variable for the while loop

    file_a = open(a)
    file_b = open(b)
    file_a_corr = file(a_corr, "wt")

    while readingFile_a != '':
       aTrue = False
       readingFile_a = file_a.readline()
       while readingFile_b != '':
         readingFile_b = file_b.readline()
         if readingFile_a == readingFile_b:
             file_a_corr.write(errorLine)
             aTrue = True
             break
       file_b.seek(0)
       readingFile_b = True
       if aTrue == False:
          file_a_corr.write(readingFile_a)

    file_a.close()
    file_b.close()
    file_a_corr.flush()
    return a_corr


####

        
