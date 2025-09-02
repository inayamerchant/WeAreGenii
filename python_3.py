from manim import *
import numpy as np

#Defining useful functions
def labelline(self, start, end, color=WHITE, label="", direction=DOWN, rotateangle=0, rotatevector=DOWN):
     line = Line(start, end, 0, None, color=color)
     l = MathTex(label)
     l.next_to(line, direction)
     for r in rotatevector:
        l.rotate(rotateangle, r)
     group = VGroup(line, l)
     return group
    
def move(self, mobjects, position=0, mag=0, direction=DOWN, duration=1):
    group = VGroup(*mobjects)
    if position != 0:
        self.play(group.animate.move_to(position), run_time=duration)
    if position == 0:
        self.play(group.animate.shift(direction*mag), run_time=duration)
        
    

def move_copy(self, mobjects, position, duration=1):
    copies =[]
    for m in mobjects:
        copies.append(m.copy())
    
    groupcopy = VGroup(*copies)
    self.play(groupcopy.animate.move_to(position, duration))
    return(groupcopy)


class Scene3(ThreeDScene):
    def construct(self):
        # Our final goal is to answer this question: ,  
        self.wait(2.5)
        quest = Text("The question:").scale(0.7)
        self.add_fixed_in_frame_mobjects(quest)
        quest.move_to([0, 3.5, 0])
        self.play(Write(quest))
        
        cuaxes = ThreeDAxes([-1,3,1], [-1,3,1], [-1,3,1], 6, 6, 6)
        cuaxes.move_to([0,0,0])
        labels2 = cuaxes.get_axis_labels("x","y","z")
        unit3d = cuaxes.get_x_unit_size()
        a3dax = 1.3
        a3dabs = unit3d*1.3
        b3dax = 0.7
        b3dabs = unit3d*0.7
        
        self.set_camera_orientation(phi=80*DEGREES, theta=20*DEGREES, gamma=0)
        
        self.play(FadeIn(cuaxes, labels2))
        
        # if you have an n-dimensional hypercube with side length a
        
        x5a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(a3dax,0,0), RED_D, "", IN, PI/2, [RIGHT])
        y5a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(0,a3dax,0), RED_D, "", LEFT, PI/2, [RIGHT])
        z5a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(0,0,a3dax), RED_D, "", RIGHT, PI/2, [RIGHT])
        self.play(Create(x5a), Create(y5a), Create(z5a))
        
        a3 = Cube(a3dabs, 0.8, RED_C)
        a3_corner = a3.get_corner(DOWN+LEFT+IN)
        a3.move_to(cuaxes.coords_to_point(0,0,0), a3_corner)
        
        self.play(DrawBorderThenFill(a3))
        
        
        # and you increase the side length by b,
        
        x6b = labelline(self, cuaxes.coords_to_point(a3dax,0,0), cuaxes.coords_to_point(a3dax+b3dax,0,0), BLUE_D, "", IN, PI/2, [RIGHT])
        y6b = labelline(self, cuaxes.coords_to_point(0,a3dax,0), cuaxes.coords_to_point(0,a3dax+b3dax,0), BLUE_D, "", LEFT, PI/2, [RIGHT])
        z6b = labelline(self, cuaxes.coords_to_point(0,0,a3dax), cuaxes.coords_to_point(0,0,a3dax+b3dax), BLUE_D, "", RIGHT, PI/2, [RIGHT])
        self.play(Create(x6b), Create(y6b), Create(z6b), run_time=1.5)
        
        # how much space does the new, bigger hypercube occupy?
        
        big_cube = Cube(a3dabs+b3dabs, 0.8, PURPLE_A)
        big_cube_corner = a3.get_corner(DOWN+LEFT+IN)
        big_cube.move_to(cuaxes.coords_to_point(0,0,0), big_cube_corner)
        self.play(FadeOut(a3), DrawBorderThenFill(big_cube))
        
        question = Text("Space occupied = ?").scale(0.7)
        self.add_fixed_in_frame_mobjects(question)
        question.move_to([0, -3.5, 0])
        self.play(Write(question))
        
        self.wait(3)