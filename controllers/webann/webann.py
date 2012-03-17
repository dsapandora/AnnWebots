## This uses the EpuckBasic code as the interface to webots, and the epuck2 code to connect an ANN
# to webots.

import epuck_basic as epb
#import graph
import prims1
from imagepro import *
import Image

import random

from ann.layer import *
from ann.link import *
from ann.ann import Ann
from ann.parser import AnnParser


# The webann is a descendent of the webot "controller" class, and it has the ANN as an attribute.

class WebAnn(epb.EpuckBasic):

    def __init__(self, ann, tempo = 1.0):
        epb.EpuckBasic.__init__(self)

        self.basic_setup() # defined for EpuckBasic 

        self.ann = ann
        self.ann.init_nodes()

        self.tempo = tempo

    
    def run():

        while True: # main loop

            # Get input proximity and camera.

            # For testing, set random values.
            l = sum([len(n) for n in self.ann.input_layers])
            i = [random.random() for x in range(l)]

            left, right = self.ann.recall(l)

            self.move_wheels(left, right, ms = self.tempo)

            if self.step(64) == -1: break


    def long_run(self,steps = 1000):
        #self.ann.simsteps = steps
        #self.spin_angle(prims1.randab(0,360))
        #
        self.spin_angle(-70)
        self.stop_moving()
        self.backward()
        self.run_timestep(200)
        #self.ann.redman_run()
        image = self.snapshot()
        # print "avg_rgb " , avg_rgb(image)

        #img = Image.open()
        #print "lengde ", len(column_avg(img))
        # print
        #print column_avg(image)

#*** MAIN ***
# Webots expects a controller to be created and activated at the bottom of the controller file.


ini_parse = AnnParser("ann/scripts/test.ini")
gann = ini_parse.create_ann()

controller = WebAnn(gann, tempo = 1.0)
controller.run()

# controller.long_run(40)
#controller.run_toy()