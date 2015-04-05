#------------------------------------------------------------------------------
#-- FRIKI:  Freecad, RobotIcs and KInematics
#------------------------------------------------------------------------------
#-- (C) Juan Gonzalez-Gomez (Obijuan)  March - 2015
#------------------------------------------------------------------------------
#-- Releases under the GNU GPL v2
#------------------------------------------------------------------------------

import FreeCAD
import pyooml
import HMatrix

from pyooml import frame, svector, cube, cylinder, link
from FreeCAD import Vector

#-- Exercise. Barrientos book. 79. Example. 3.1
def barrientos_pag79_ex3_1():
	#--- Frame 1 and p vector
	frame()
	p = Vector(6, -3, 8)
	svector(p)

	#--- Frame 2. Translated p
	f2 = frame()
	M = HMatrix.Translation(p)
	f2.T = M

	#-- Vector r in the frame 2
	r = Vector(-2, 7, 3)
	sr = svector(r)
	sr.T = M

	#-- Calculate the r0 vector: r refered to frame 1
	r0 = M.multiply(r)
	sr0 = svector(r0).color("yellow")
	print("r0: {}".format(r0))

def barrientos_ex3_2_pag_80():
	#--- Define the transformation
	p = Vector(6, -3, 8)
	T = HMatrix.Translation(p)
	
	#--- Calculate r and its transformation
	r = Vector(4, 4, 11)
	r2 = T.multiply(r)
	
	#--- Draw all the vectors
	vr = svector(r)
	vp = svector(p).translate(r)
	vr2 = svector(r2).color("yellow")
	
	print("r2: {}".format(r2))

def barrientos_ex3_3_pag_81():
	#-- Define the original frame and the transformation
	fxyz = frame()
	T = HMatrix.Rotz(-90)
	
	#-- Define the frame2
	fuvw = frame()
	fuvw.T = T

	#-- Define the vectors
	r2 = Vector(4, 8, 12)
	r1 = T.multiply(r2)
	print("r1: {}".format(r1))
	
	#-- Draw the vectors
	sr1 = svector(r1)
	sr2 = svector(r2)

def barrientos_ex3_4_pag_84():
	f0 = frame()
	p = Vector(8, -4, 12)
	
	#-- Define the transformation
	T1 = HMatrix.Rotx(90)
	T2 = HMatrix.Translation(p)
	T = T2 * T1
	
	#-- Vector in frame 1
	r1 = Vector(-3, 4, -11)
	r0 = T.multiply(r1)
	
	#-- Frame 1
	f1 = frame()
	f1.T = T
	
	#-- Draw the vectors
	vp = svector(p)
	vr1 = svector(r1).transform(T)
	vr0 = svector(r0).color("yellow")
	print("r0: {}".format(r0))

def barrientos_ex3_5_pag_84():
	f0 = frame()
	p = Vector(8, -4, 12)
	
	#-- Define the transformation
	T1 = HMatrix.Translation(p)
	T2 = HMatrix.Rotx(90)
	T = T2 * T1
	
	#-- Vector in frame 1
	f1 = frame()
	f1.T = T
	
	#-- Vector in frame 1
	r1 = Vector(-3, 4, -11)
	r0 = T.multiply(r1)
	
	#-- Frame 1
	f1 = frame()
	f1.T = T
	
	#-- Draw the vectors
	vp = svector(p)
	vr1 = svector(r1).transform(T)
	vr0 = svector(r0).color("yellow")
	print("r0: {}".format(r0))

def robot_model():
	frame()
	base = cylinder(r = 20, h = 5)
	body = cylinder(r = 10, h = 60)
	shoulder = cube(30,20,15, center = True).translate(0, 0, 15/2. + 60)
	arm = cube(10, 80, 30).translate(-25, -15, 54)
	forehand = cube(10, 60, 15, center = True).rotx(-45).translate(-10., 70, 50)

def barrientos_ex3_6_pag_89():
	#Initial frame
	f0 = frame()
	
	#-- Define the transformations
	M1 = HMatrix.Rotx(-90)
	p = Vector(5, 5, 10)
	M2 = HMatrix.Translation(p)
	M3 = HMatrix.Rotz(90)
	
	#------- Apply the transformations
	#-- 1st transformation
	f1 = frame()
	f1.T = M1
	
	#-- 2nd transformation
	#-- As the transformation is relative to the global xyz frame, 
	#-- the matrices should be multiplied en reverse order
	f2 = frame()
	f2.T = M2 * M1
	
	#-- 3rd transformation
	f3 = frame()
	f3.T = M3 * M2 * M1
	
	print("Result:")
	print(f3.T)

def barrientos_ex3_7_pag_90():
	f0 = frame()
	
	#-- Tranformation 1
	p = Vector(-3, 10, 10)
	f1 = frame()
	M1 = HMatrix.Translation(p)
	f1.T = M1
	
	#------------ Tranformation 2
	f2 = frame()
	M2 = HMatrix.Rotx(-90)
	#-- As this transformation should be relative to the mobile frame (f2)
	#-- the matrices are multipled in normal order
	f2.T = M1 * M2
	
	#--------- Transformation 3
	f3 = frame()
	M3 = HMatrix.Roty(90)
	f3.T = M1 * M2 * M3
	
	print("Result:")
	print(f3.T)

def barrientos_exercise_3_6_pag_106():
	f0 = frame()
	
	#-- Define the transformations
	M1 = HMatrix.Rotz(30)
	M2 = HMatrix.Translation(10, 0, 0)
	
	f2 = frame()
	f2.T = M1 * M2
	
	print("Transformation matrix:")
	print(f2.T)

if __name__ == "__main__":
	#barrientos_pag79_ex3_1()
	#barrientos_ex3_2_pag_80()
	#barrientos_ex3_3_pag_81()
	#barrientos_ex3_4_pag_84()
	#barrientos_ex3_5_pag_84()
	#robot_model()
	#barrientos_ex3_6_pag_89()
	#barrientos_ex3_7_pag_90()
	#barrientos_exercise_3_6_pag_106()
	f0 = frame()
	l1 = link(l = 40, w = 5, D = 10)
	l2 = l1.copy()
	l2.roty(30)
	l2.translate(40, 0, 0)

	