
# THINGS LEARNED
# - define the folders without the '/' at the end (as a style thing)

# STYLE
# Note that most importantly, the '' that ends a multiline docstring should be
# on a line by itself, and preferably preceded by a blank line

# have the functions print out their name in the style: print '\nfunc functionName'

# 4 spaces
# dont mix with tabs
# 79 line long
# define the folders without the '/' at the end

# things to do:
# 1. check if you are given a .ma file
#   - check the file for extension.
#   - read the file to see if the first line is //Name: mainScene.ma
# check to see if the given .ma file has a 'createNode VRaySettingsNode'.
#     - return true or false
#     - if true, return all the available values
# all the attributes are like objects themself, so create a vray attribute object
#     - that object should hold it's default value, given value, parent value,
#     if on or off. attr alias, attr long name. 

filePath = '/home/engin/Documents/python_file_testing/04.ma'

###########################################################################

import os

class maFile(object):
    def __init__(self, filePath):
        '''creates an object for the .ma file at the given file path'''
        '''with the given object you can do various adjustments and queries'''
        
        self.filePath = filePath
        
        self.validity = self.validity()
        #   self.rootFolder
        #   self.fileName

        if self.validity:
            self.fileNameAndExtension(self.fileName)


    def checkExists(self, filePath):
        '''checks if the filePath exists '''
        '''input: str'''
        '''output: boolean'''
        print '\nfunc checkExists'
        
        exists = os.path.exists(filePath)
        return exists

        
    def folderAndFile(self, filePath):
        '''checks if the filePath points to a file, and sets the root folder
        and the file name
        '''
        '''input: str'''
        print '\nfunc folderAndFile'
        
        if os.path.isfile(filePath):
            filePathTuple = os.path.split(self.filePath)
            self.rootFolder = filePathTuple[0]
            self.fileName = filePathTuple[1]
            return True
        else:
            print 'given path points to a folder, not a file'
            return False


    def checkMa(self, filePath):
        '''checks if the filePath points to a .ma file'''
        '''input: str '''
        '' 'output: boolean '''
        print '\nfunc checkMa'

        if self.fileName[-3:] == '.ma':
            print 'file extension is .ma'
            return True
        else:
            print 'file extension is not .ma'
            return False

        # add one to the counter if you dont want to get the "."

    def validity(self):
        ''' determines the validity of the given file path, to be valid:
        it needs to: exist(1), a file(2), a .ma file(3)
        '''
        conditionOne = self.checkExists(self.filePath) # does it exist
        conditionTwo = self.folderAndFile(self.filePath) # is it a file
        conditionThree = self.checkMa(self.filePath) # is it a .ma file
        if conditionOne and conditionTwo and conditionThree:
            return True
        else:
            return False

    def fileNameAndExtension(self, fileName):
        '''given the fileName, sets the name(only) and extension '''
        '''input: str'''
        '''output: tuple (str,str)'''
        print '\nfunc fileNameAndExtension'

        value = -1
        counter = -1
        name = fileName
        lenName = len(name)
                                      
        while abs(counter) < lenName:
          if name[counter] == ".":
              value = counter
              break
          else:
              counter -= 1
        if abs(counter) == lenName:
          print "there is no '.' in this file name"
          return None
        #print counter
        fileTuple = (name[:counter],name[lenName + counter :])
        print fileTuple
        return fileTuple


    def getRidOfCharacters(self, givenStr):
        '''gets rid of certain characters in a given string, this one for
        white space and "
        '''
        '''input: str'''
        '''output: str'''
        print '\nfunc getRidOfCharacters'

        givenStr = givenStr.strip(' ')
        givenStr = givenStr.strip('"')
        return givenStr

    @property
    def queryMaDefaults(self):
        '''given the .ma file, returns some simple information from the file'''
        '''input: str'''
        '''output: dictionary'''
        print '\nfunc queryMaDefaults'
        #reads the :
        #requires maya ver
        #requires vrayformaya ver

        fileActive = open(self.filePath)
        readingFile = True
        
        var_requiresMaya = False
        var_requiresVRay = False

        stringReqMaya = 'requires maya'
        stringReqVRay = 'requires "vrayformaya"'
        
        VRayPropertyDict = {}

        while readingFile != '':
            readingFile = fileActive.readline()
            
            if readingFile[:len(stringReqMaya)] == stringReqMaya:
                var_requiresMaya = True
                mayaVer = readingFile[len(stringReqMaya):-2]
                mayaVer = self.getRidOfCharacters(mayaVer)
                # get rid of the white space and "
                # -2 is to get rid of \n and ; at the end of line
                print mayaVer

            if readingFile[:len(stringReqVRay)] == stringReqVRay:
                var_requiresVRay = True
                VRayVer = readingFile[len(stringReqVRay):-2]
                VRayVer = self.getRidOfCharacters(VRayVer)
                print VRayVer

        if var_requiresMaya == False:
                print 'cant find the "requires maya" line'
        if var_requiresVRay == False:
                print 'cant find the "requires VRay" line'
                
        fileActive.close()
        return (mayaVer, VRayVer)
    
    @property
    def queryVraySettingsNode(self):
        '''given the .ma file checks to see if the file contains
        a VRaySettingsNode and reads the queries the values for the attributes
        '''
        '''input: str'''
        '''output: '''
        print '\nfunc queryVraySettingsNode'

        fileActive = open(self.filePath)
        readingFile = True
        containsVray = False
        VRayPropertyDict = {}

        stringVRaySetNode = 'createNode VRaySettingsNode'
        stringAttr = 'setAttr'

        while readingFile != '':
            readingFile = fileActive.readline()
            if readingFile[:len(stringVRaySetNode)] == stringVRaySetNode:
                containsVray = True
                startVrayAtts = True
                print 'contains a VraySettingsNode'
                while startVrayAtts == True:
                    readingFile = fileActive.readline()
                    readingFileNoSpaces = readingFile.strip() #gets rid of space
                    print readingFileNoSpaces[:len(stringAttr)]
                    if readingFileNoSpaces[:len(stringAttr)] == stringAttr:
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


def setAttrReader(varName):
    '''return the attribute alias and the value'''

    lenghtVariable = len(varName)
    counter = 0

    variable = [] # list for the variable
    flag = [] # list for the flag
    value = [] # list for the characters

    variableFinal = " "
    flagFinal = " "
    valueFinal = 0

    varNameInv = varName[::-1]
   
    varName = varName.strip() #get rid of the whitespace,
    # actually might be dangerous because you want the setAttrs
    # with whitespace infront of it...
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

###########################################################################

x = maFile(filePath)

###########################################################################
        
