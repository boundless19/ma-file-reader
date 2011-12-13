###################################################### ATTRIBUTE READER

# all the attributes are like objects themself, so create a vray attribute object
#     - that object should hold it's default value, given value, parent value,
#     if on or off. attr alias, attr long name. 

###################################################### 

LISTVALUE = {}
LISTVALUE['gogdh']  = ('never', 'auto', 'always') # hidden geo
LISTVALUE['goldhl'] = ('never', 'auto', 'always') # hidden lights
LISTVALUE['st'] = ('fixed type', 'adaptive dmc', 'adaptive subd')
LISTVALUE['aaft'] = ('box', 'area', 'triangle', 'lanczos', 'sinc', 'catmullrom', 'gaussian', 'cook')
LISTVALUE['cmtp'] = ('linear multiply', 'exponential', 'hsv exponential', 'intensity exponential', 'gamma correction', 'intesity gamma', 'reinhard')

LISTPARAM = {} # list of parameters and their default values
CATEGORIES = {}

# GLOBAL OPTIONS

CATEGORIES[0] = ('gogd', 'gogdh', 'gobc', 'gorvs', 'gumsfp')
# CATEGORY : 0 Global Options - Geometry
LISTPARAM['gogd'] = ('displacement', 'yes', 'main', 0)
LISTPARAM['gogdh'] = ('hidden geometry', '1', 'main', 0)
LISTPARAM['gobc'] = ('force back face culling', '1', 'main', 0)
LISTPARAM['gorvs'] = ('render viewport subdivision', 'no', 'main', 0)
LISTPARAM['gumsfp'] = ('use maya shader for VRay proxies', 'no', 'main', 0)

CATEGORIES[1] = ('goldl', 'golddl', 'goldhl', 'golds', 'gologi', 'gogdri')
# CATEGORY : 1 Global Options - Lighting and GI
LISTPARAM['goldl'] = ('lights', 'yes', 'main', 1)
LISTPARAM['golddl'] = ('default lights', 'yes', 'main', 1)
LISTPARAM['goldhl'] = ('hidden lights', '1', 'main', 1)
LISTPARAM['golds'] = ('shadows', 'yes', 'main', 1)
LISTPARAM['gologi'] = ('show gi only', 'no', 'main', 1)
LISTPARAM['gogdri'] = ('dont render final image', 'no', 'main', 1)

CATEGORIES[2] = ('gomrr', 'gomld', 'gommd', 'gomdm', 'gomfm', 'gomg', 'gomtml', 'gomtc', 'gomb')
# CATEGORY : 2 Global Options - Materials and Raytracing
LISTPARAM['gomrr'] = ('reflection/refraction', 'yes', 'main', 2)
LISTPARAM['gomld'] = ('global max depth', 'no', 'main', 2)
LISTPARAM['gommd'] = ('max depth', '5', ('gomld', 'yes'), 2)
LISTPARAM['gomdm'] = ('maps', 'yes', 'main', 2)
LISTPARAM['gomfm'] = ('filter maps', 'yes', 'main', 2)
LISTPARAM['gomg'] = ('glossy effects', 'yes', 'main', 2)
LISTPARAM['gomtml'] = ('max transparency levels', '50', 'main', 2)
LISTPARAM['gomtc'] = ('transparency cut-off', '0.001', 'main', 2)
LISTPARAM['gomb'] = ('secondary ray-bias', '0', 'main', 2)

CATEGORIES[3] = ('st', )
# CATEGORY : 3 Global Options - AA type
LISTPARAM['st'] = ('antialiasing type', '2', 'main', 3)

CATEGORIES[4] = ('aafon', 'aaft', 'aafs')
# CATEGORY : 4 Global Options - Filter
LISTPARAM['aafon'] = ('filter on/off', 'yes', 'main', 4)
LISTPARAM['aaft'] = ('aa filter type', '1', ('aafon', 'yes'), 4)
LISTPARAM['aafs'] = ('aa filter size', '1.5', ('aafon', 'yes'), 4)

CATEGORIES[5] = ('smi', 'sma', 'sji', 'tre', 'sde', 'sno', 'snot', 'sss')
# CATEGORY : 5 Global Options - Adaptive Subd
LISTPARAM['smi'] = ('adaptive subd min', '-1', ('st', '2'), 5)
LISTPARAM['sma'] = ('adaptive subd max', '2', ('st', '2'), 5)
LISTPARAM['sji'] = ('jitter', 'yes', ('st', '2'), 5)
LISTPARAM['tre'] = ('threshold', '0.150', ('st', '2'), 5)
LISTPARAM['sde'] = ('edges', 'yes', ('st', '2'), 5)
LISTPARAM['sno'] = ('normals', 'yes', ('st', '2'), 5)
LISTPARAM['snot'] = ('normals threshold', '0.100', ('st', '2'), 5)
LISTPARAM['sss'] = ('show samples', 'no', ('st', '2'), 5)

CATEGORIES[6] = ('dmi', 'dma', 'dmlt', 'dmt', 'dss')
# CATEGORY : 6 Global Options - Adaptive DMC
LISTPARAM['dmi'] = ('antialiasing min samples', '1', ('st', '1'), 6)
LISTPARAM['dma'] = ('antialiasing max samples', '4', ('st', '1'), 6)
LISTPARAM['dmlt'] = ('lock threshold to dmc sampler', 'no', ('st', '1'), 6)
LISTPARAM['dmt'] = ('antialiasing threshold', '0.01', ('dmlt', 'no'), 6) # two parents?
LISTPARAM['dss'] = ('show samples', 'no', ('st', '1'), 6)

CATEGORIES[7] = ('fsd', )
# CATEGORY : 7 Global Options - Fixed
LISTPARAM['fsd'] = ('antialiasing fixed subdivision', '1', ('st', '0'), 7)

CATEGORIES[8] = ('cmtp', 'cmdm', 'cmbm', 'cg', 'cmab', 'cmco', 'cmcl', 'cmsm', 'cmao', 'cmlw', 'cmas')
# CATEGORY : 8 Global Options - Color Mapping
LISTPARAM['cmtp'] = ('color mapping type', '0', 'main', 8)
LISTPARAM['cmdm'] = ('dark multiplier', '1', 'main', 8)
LISTPARAM['cmbm'] = ('bright multiplier', '1', 'main', 8)
LISTPARAM['cg'] = ('gamma', '1', 'main', 8)
LISTPARAM['cmab'] = ('affect background', 'yes', 'main', 8)
LISTPARAM['cmco'] = ('clamp output', 'no', 'main', 8)
LISTPARAM['cmcl'] = ('clamp level', '1', ('cmco', 'yes'), 8)
LISTPARAM['cmsm'] = ('subpixel mapping', 'no', 'main', 8)
LISTPARAM['cmao'] = ('dont affect colors', 'no', 'main', 8)
LISTPARAM['cmlw'] = ('linear workflow', 'no', 'main', 8)
LISTPARAM['cmas'] = ('affect swatches', 'no', 'main', 8)

CATEGORIES[9] = ('camon', 'cammb', 'camdur', 'camic', 'cabias', 'camsd', 'casef', 'capps', 'camgs')
# CATEGORY : 9 Global Options - Camera
LISTPARAM['camon'] = ('motion blur', 'no', 'main', 9)
LISTPARAM['cammb'] = ('camera motion blur', 'yes', 'main', 9)
LISTPARAM['camdur'] = ('duration', '1', ('camon', 'yes'))
LISTPARAM['camic'] = ('interval center', '1', ('camon', 'yes'), 9)
LISTPARAM['cabias'] = ('bias', '0', ('camon', 'yes'), 9)
LISTPARAM['camsd'] = ('subdivs', '6', ('camon', 'yes'), 9)
LISTPARAM['casef'] = ('shutter efficiency', '1', ('camon', 'yes'), 9)
LISTPARAM['capps'] = ('prepass samples', '1', 'main', 9)
LISTPARAM['camgs'] = ('geometry samples', '2', 'main', '9', 9)

CATEGORIES[10] = ('bmpm', 'tfsm', 'phsc', 'neg')
# CATEGORY : 10 Global Options - Misc
LISTPARAM['bmpm'] = ('global bump map multiplier', '1', 'main', 10)
LISTPARAM['tfsm'] = ('global texture filter scale multiplier', '1', 'main', 10)
LISTPARAM['phsc'] = ('photometric lights scale', '20', 'main', 10)
LISTPARAM['neg'] = ('allow negative shader colors', 'no', 'main', 10)

CATEGORIES[11] = ('dmcstd', 'dmcsaa', 'dmcsat', 'dmcsams', 'dmcssm')
# CATEGORY : 11 Global Options - DMC
LISTPARAM['dmcstd'] = ('time dependent', 'no', 'main', 11)
LISTPARAM['dmcsaa'] = ('dmc adaptive amount', '0.850', 'main', 11)
LISTPARAM['dmcsat'] = ('dmc adaptive threshold', '0.01', 'main', 11)
LISTPARAM['dmcsams'] = ('adaptive min amount', '8', 'main', 11)
LISTPARAM['dmcssm'] = ('subdivs multiplier', '1', 'main', 11)

#CATEGORIESAll
CATEGORIES['CATEGORY_ALL'] = LISTPARAM.keys()

###################################################### 

class VRayAttribute(object):
    def __init__(self, alias):
        '''given the alias for the attribute, this object returns:
        fullName
        defaultValue
        value
        valueName
        parent
        category
        '''

        self.alias = alias

    @property
    def fullName(self):
        fullName = LISTPARAM[self.alias][0]
        return fullName

    @property
    def defaultValue(self):
        defaultValue = LISTPARAM[self.alias][1]
        return defaultValue

    @property
    def valueName(self, value):
        value = LISTPARAM[self.alias][1]
        try:
            valueName = self.LISTVALUE[self.alias][value]
            return valueName
        except KeyError:
            print 'value name doesnt exist'
            return False

    @property
    def parent(self):
        parent = LISTPARAM[self.alias][2]
        return parent

    @property
    def category(self):
        category = LISTPARAM[self.alias][3]
        return category

######################################################



###################################################### 

"""
LISTPARAM['gi'] =  ('gi on/off')

LISTPARAM['iminr'] = ('irradiance min amount')
LISTPARAM['imaxr'] = ('irradiance max amount')
LISTPARAM['isds'] = ('irradiance subdivision')
LISTPARAM['itps'] = ('irradiance interpolation')
LISTPARAM['itpfs'] = ('irradiance frames')
LISTPARAM['icts'] = ('irradiance color threshold')
LISTPARAM['ints'] = ('irradiance normal threshold')
LISTPARAM['idts'] = ('irradiance distance threshold')
LISTPARAM['idr'] = ('detail enhancement distance')
LISTPARAM['ids'] = ('detail enhancement subdivs')


LISTPARAM['ddel'] = ('default displacement')
LISTPARAM['ddms'] = ('max subdivs disp')
LISTPARAM['dda'] = ('amount subdivsions')
LISTPARAM['srdml'] = ('dynamic memory limit')
LISTPARAM['srgx'] = ('render region x')
LISTPARAM['srgy'] = ('render region y')
"""
