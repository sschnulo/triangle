import pylab
import numpy
import scipy


#execfile( 'test_AMlossModelNew_blades.out' )
execfile( 'VSPT_blades.out' )

# input airfoil definition -> camber line plus thickness distribution


# array of x values to generate camber line and thickness distribution
#
# xCamber, yCamber either input or generated using xvals
# ythk either input or generated using a function definition
#
# xUpper, yUpper, xLower, yLower generated from camber line and thickness
#
#
#

#pylab.figure(num=1, figsize=(10,10), dpi=80, facecolor='w', edgecolor='b')


# array of x values to generate airfoil points, weighted towards leading edge
xvals= [ 0.0000, 0.0050, 0.0075, 0.0125, 0.0250, 0.0500, 0.0750, 0.1000, 0.1500,
         0.2000, 0.2500, 0.3000, 0.3500, 0.4000, 0.4500, 0.5000, 0.5500, 0.6000,
         0.6500, 0.7000, 0.7500, 0.8000, 0.8500, 0.9000, 0.9500, 1.0000 ]



# c1 airfoil thickness distribution/definition
xpnts = [  0.0000,  0.0125,  0.0250,  0.0500,  0.0750,  0.1000,  0.1500, 
           0.2000,  0.3000,  0.4000,  0.5000,  0.6000,  0.7000,  0.8000, 
           0.9000,  0.9500,  1.0000 ]

ypnts = [ 0.00000, 0.01375, 0.01940, 0.02675, 0.03225, 0.03600, 0.04175, 
          0.04550, 0.04950, 0.04810, 0.04370, 0.03750, 0.02930, 0.02050, 
          0.01125, 0.00650, 0.00000 ]




# generic turbine thickness distribution/definition
txCamber = [ 0.0000, 0.0010, 0.0022, 0.0056, 0.0100, 0.0153, 0.0216, 0.0289, 
             0.0371, 0.0462, 0.0562, 0.0672, 0.0790, 0.0918, 0.1054, 0.1199, 
             0.1353, 0.1515, 0.1686, 0.1865, 0.2053, 0.2249, 0.2453, 0.2664, 
             0.2884, 0.3112, 0.3348, 0.3591, 0.3842, 0.4100, 0.4365, 0.4639, 
             0.4919, 0.5206, 0.5501, 0.5802, 0.6110, 0.6425, 0.6747, 0.7076, 
             0.7411, 0.7752, 0.8100, 0.8453, 0.8814, 0.9180, 0.9553, 1.0000 ]
tyCamber = [ 0.0000, 0.0179, 0.0353, 0.0683, 0.0996, 0.1291, 0.1569, 0.1830, 
             0.2073, 0.2300, 0.2511, 0.2704, 0.2882, 0.3043, 0.3188, 0.3317, 
             0.3431, 0.3529, 0.3612, 0.3679, 0.3732, 0.3769, 0.3792, 0.3800, 
             0.3794, 0.3773, 0.3739, 0.3690, 0.3628, 0.3553, 0.3463, 0.3361, 
             0.3245, 0.3117, 0.2975, 0.2821, 0.2655, 0.2476, 0.2285, 0.2083, 
             0.1868, 0.1642, 0.1404, 0.1155, 0.0895, 0.0623, 0.0340, 0.0000 ]

thk_upp = [ 0.0000, 0.1800, 0.2650, 0.3700, 0.4520, 0.5099, 0.5704, 0.6290, 
            0.6847, 0.7362, 0.7818, 0.8205, 0.8523, 0.8788, 0.9024, 0.9252, 
            0.9474, 0.9666, 0.9784, 0.9780, 0.9631, 0.9349, 0.8969, 0.8531, 
            0.8068, 0.7602, 0.7144, 0.6702, 0.6277, 0.5871, 0.5483, 0.5114, 
            0.4761, 0.4424, 0.4103, 0.3796, 0.3503, 0.3224, 0.2957, 0.2701, 
            0.2456, 0.2221, 0.1992, 0.1770, 0.1450, 0.1050, 0.0700, 0.0000 ]

thk_low = [ 0.0000, 0.2100, 0.3150, 0.4750, 0.5950, 0.6840, 0.7430, 0.7973, 
            0.8455, 0.8861, 0.9185, 0.9425, 0.9591, 0.9694, 0.9752, 0.9781, 
            0.9793, 0.9796, 0.9790, 0.9769, 0.9726, 0.9645, 0.9516, 0.9326, 
            0.9072, 0.8752, 0.8375, 0.7950, 0.7493, 0.7016, 0.6532, 0.6052, 
            0.5584, 0.5133, 0.4702, 0.4294, 0.3909, 0.3548, 0.3210, 0.2894, 
            0.2600, 0.2326, 0.2072, 0.1836, 0.1500, 0.1150, 0.0750, 0.0000 ]


'''
xCamber = []
yCamber = []
xUpper = []
yUpper = []
xLower = []
yLower = []
'''

s_thk = 0.9   # thickness scalar
s_camber = 0.90  # camber scalar
#shape = 'concave'
lastx = 0.
lasty = 0.


def genCoords( maxCamber ):
    '''generates airfoil coordinates'''

    #
    # generate circular arc camber line given max camber for unity chord length
    #

    # calculate airfoil camber and camber line length from maximum camber
    arcRadius = 0.5*( maxCamber + 1./(4.*maxCamber) )
    h = arcRadius - maxCamber
    theta = numpy.arccos( h/arcRadius )

    airfoilCamber = 2.*theta
    arcLength = 2.*arcRadius*theta
    
    # generate x and y points on the camber line
    if maxCamber < 1. :
        for x in xvals:
            xCamber.append( x )
            y =  numpy.sqrt( arcRadius**2. - (x-0.5)**2. ) - h 
            yCamber.append( y )

    else :
        for x in txCamber:
            xCamber.append( x )
        for y in tyCamber:
            yCamber.append( y*s_camber ) 
        
        theta = 1.55   # fix later



    # calculate x and y points on the airfoil surface based on thickness
    # slope is slope of camber line, s is distance along the camber line
    for i in xrange( len(xCamber) ):
        if i == 0:
            slope = theta
            s = 0.
        else:
            dy = yCamber[i] - yCamber[i-1]
            dx = xCamber[i] - xCamber[i-1] 
            slope = numpy.arctan( dy/dx )
            
            length = numpy.sqrt( dx**2. + dy**2. )
            s = s + length

        # convert camber line distance values to equivalent x values to get
        # thickness at that point
        if maxCamber < 1. :
            xmod = s / arcLength
            thickness = s_thk*numpy.interp( xmod, xpnts, ypnts )

            xUpper.append( xCamber[i] - thickness*numpy.sin(slope) )
            yUpper.append( yCamber[i] + thickness*numpy.cos(slope) )

            xLower.append( xCamber[i] + thickness*numpy.sin(slope) )
            yLower.append( yCamber[i] - thickness*numpy.cos(slope) )

        else :
            thickness = s_thk*thk_upp[i]/5.277
            xUpper.append( xCamber[i] - thickness*numpy.sin(slope) )
            yUpper.append( yCamber[i] + thickness*numpy.cos(slope) )

            thickness = s_thk*thk_low[i]/5.277
            xLower.append( xCamber[i] + thickness*numpy.sin(slope) )
            yLower.append( yCamber[i] - thickness*numpy.cos(slope) )





def scaleAndRotate( chordLength, angle ):

    # scale values to input chord length
    for i in xrange( len(xCamber) ):
        xCamber[i] = chordLength*xCamber[i]
        yCamber[i] = chordLength*yCamber[i]

        xUpper[i]  = chordLength*xUpper[i]
        yUpper[i]  = chordLength*yUpper[i]
        
        xLower[i]  = chordLength*xLower[i]
        yLower[i]  = chordLength*yLower[i]

    # rotate curves based on stagger angle
    for i in xrange( len(xCamber) ):

        length = numpy.sqrt( xCamber[i]**2. + yCamber[i]**2. )
        if i == 0:
            angleOld = 0.
        else:
            angleOld = numpy.arctan( yCamber[i]/xCamber[i] )
        xCamber[i] = length*numpy.cos(angleOld + angle)
        yCamber[i] = length*numpy.sin(angleOld + angle)


        length = numpy.sqrt( xUpper[i]**2. + yUpper[i]**2. )
        if i == 0:
            angleOld = 0.
        else:
            angleOld = numpy.arctan( yUpper[i]/xUpper[i] )\
        

        if  xUpper[i] < 0. and yUpper[i] > 0. :    # reverse sign if negative angle
            xUpper[i] = -length*numpy.cos(angleOld + angle)
            yUpper[i] = -length*numpy.sin(angleOld + angle)
        else:
            xUpper[i] = length*numpy.cos(angleOld + angle)
            yUpper[i] = length*numpy.sin(angleOld + angle)


        length = numpy.sqrt( xLower[i]**2. + yLower[i]**2. )
        if i == 0:
            angleOld = 0.
        else:
            angleOld = numpy.arctan( yLower[i]/xLower[i] )
        xLower[i]  = length*numpy.cos(angleOld + angle)
        yLower[i]  = length*numpy.sin(angleOld + angle)



def master( maxCamber, chordLength, staggerAngle, offset_x, offset_y, shape ):
    '''generates circular arc camber line, C1 airfoil thickness distribution, 
    and plots airfoil'''

    global xCamber
    global yCamber
    global xUpper
    global yUpper
    global xLower
    global yLower
    global lastx
    global lasty
    xCamber = []
    yCamber = []
    xUpper = []
    yUpper = []
    xLower = []
    yLower = []


    genCoords( maxCamber )
    
    scaleAndRotate( chordLength, staggerAngle )

    # plot camber line, upper surface, and lower surface
    # for concave just flip y values
    if shape == 'concave':
        pylab.plot( [x + offset_x for x in xCamber], 
                    [-y- offset_y for y in yCamber], 'red',  linewidth=3. )
        
        pylab.plot( [x + offset_x for x in xUpper], 
                    [-y- offset_y for y in yUpper],  'blue', linewidth=3. )
    
        pylab.plot( [x + offset_x for x in xLower], 
                    [-y- offset_y for y in yLower],  'blue', linewidth=3. )

    else:
        pylab.plot( [x + offset_x for x in xCamber], 
                    [y + offset_y for y in yCamber], 'red',  linewidth=3. )
        
        pylab.plot( [x + offset_x for x in xUpper], 
                    [y + offset_y for y in yUpper],  'blue', linewidth=3. )

        pylab.plot( [x + offset_x for x in xLower], 
                    [y + offset_y for y in yLower],  'blue', linewidth=3. )


    lastx = xCamber[-1]+offset_x
    lasty = yCamber[-1]+offset_y
    xCamber = []
    yCamber = []
    xUpper = []
    yUpper = []
    xLower = []
    yLower = []



def genXYpoints( length, angle ):
    '''Generates a series of XY points starting from 0,0 to the input length
       at the input angle.  Note a positive angle is in the -y direction.'''

    global xpnts
    global ypnts
    xpnts = []
    ypnts = []

    oldx = 0.
    oldy = 0.
    xpnts.append( oldx )
    ypnts.append( oldy )

    for i in xrange(5):

        newx = oldx + length/5*numpy.cos(angle)
        newy = oldy - length/5*numpy.sin(angle)
        xpnts.append( newx )
        ypnts.append( newy )

        oldx = newx
        oldy = newy

w = 0



# for i in range(0,5):
    
#     master( 1.5, 800., -34.*numpy.pi/180., 0, w, 'convex' )
#     w = w + 500
#     print "We're on time %d" % (i)


# w = 0


pylab.arrow( 1, 1, 50, 50, width=6, head_width=40,
                 length_includes_head='true', color='green' )
    

pylab.show()






