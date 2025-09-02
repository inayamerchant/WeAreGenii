from manim import *

#Defining useful functions
def labelline(self, start, end, color=WHITE, label="", direction=DOWN, rotateangle=0, rotatevector=[OUT]):
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
    
class Scene4(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=85*DEGREES, theta=0*DEGREES, gamma=0)
        
        # Let's start by considering a line segment. 
        one_d_axis = ThreeDAxes([-1,3,1], [-1,3,1], [-1,3,1], 9, 9, 9)
        line = Line(one_d_axis.coords_to_point(0,0,0), one_d_axis.coords_to_point(0,1.3,0), color=RED_C)
        self.play(Create(line))
        
        # It lies on the number line, in a 1 dimensional space. 
        one_d_axis_y = one_d_axis.get_y_axis()
        one_d_axis_y.rotate(90*DEGREES, UP)
        self.play(Create(one_d_axis_y))
        axes_1d_text = MathTex("\\text{Axes: } 1")
        axes_1d_text.rotate(90*DEGREES, UP)
        axes_1d_text.rotate(90*DEGREES, RIGHT)
        axes_1d_text.next_to(one_d_axis_y, IN, buff=0.5)
        self.play(Write(axes_1d_text))
        
        # Its boundaries, its start and end, are 0 dimensional points. 
        dot1 = Dot3D(one_d_axis.coords_to_point(0,0,0), color=RED_C)
        dot2 = Dot3D(one_d_axis.coords_to_point(0,1.3,0), color=RED_C)
        self.play(Create(dot1), Create(dot2))
        self.play(Wiggle(dot1), Wiggle(dot2))
        surface_1d_text = MathTex("\\text{Surface: }")
        surface_1d_text.rotate(90*DEGREES, UP)
        surface_1d_text.rotate(90*DEGREES, RIGHT)
        surface_1d_text.next_to(axes_1d_text, IN, buff=0.5)
        parts_0d_text = MathTex("0\\text{-dimensional parts}")
        parts_0d_text.rotate(90*DEGREES, UP)
        parts_0d_text.rotate(90*DEGREES, RIGHT)
        parts_0d_text.next_to(surface_1d_text, IN, buff=0.5)
        self.play(Write(surface_1d_text))
        self.play(Write(parts_0d_text))
    
       
        one_d_stuff = VGroup(line, one_d_axis_y, dot1, dot2)
        one_d_text = VGroup(axes_1d_text, surface_1d_text, parts_0d_text)
        self.play(one_d_stuff.animate.scale(0.3).move_to([0, -5, 2]))
        self.play(one_d_text.animate.shift(DOWN*5.5))
        
        separator1 = Line([0, -2.5, 4], [0, -2.5, -4], color=GRAY)
        self.play(Create(separator1))
        self.wait(2)

        #2D------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # A square lies on a plane, a 2 dimensional space. 
            # Construct axes (y and z) but don't show yet
        two_d_axes = ThreeDAxes([-1,3,1], [-1,3,1], [-1,3,1], 5, 5, 5)
        two_d_axes.shift([0,3,0])
        unit = two_d_axes.get_x_unit_size()
        
            # Construct square on y-z plane
        square = Square(1.3*unit, color=RED_C, fill_opacity=0.8, stroke_opacity=1)
        square.rotate(90*DEGREES, UP)
        square.move_to(two_d_axes.coords_to_point(0,0,0), square.get_corner(DOWN+IN))
        self.play(DrawBorderThenFill(square))
        
        # To map out points on the square in this space, you'll use 2 perpendicular axes, one to represent each dimension: the x axis and the y axis. 
        two_d_y_axis = two_d_axes.get_y_axis()
        two_d_y_axis.rotate(90*DEGREES, UP)
        two_d_z_axis = two_d_axes.get_z_axis()
        two_d_z_axis.rotate(90*DEGREES, OUT)
        two_d_y_label = MathTex("x").next_to(two_d_y_axis.get_end(), RIGHT)
        two_d_z_label = MathTex("y").next_to(two_d_z_axis.get_end(), UP)
        self.play(Create(two_d_y_axis), Create(two_d_z_axis), Write(two_d_y_label), Write(two_d_z_label))
        axes_2d_text = MathTex("\\text{Axes: } 2")
        axes_2d_text.rotate(90*DEGREES, UP)
        axes_2d_text.rotate(90*DEGREES, RIGHT)
        axes_2d_text.next_to(two_d_axes, IN)
        axes_2d_text.scale(0.9)
        self.play(Write(axes_2d_text))
        self.wait(6)
       
        # The boundary of the square is formed by these 1 dimensional lines. It also has 0 dimensional vertices. 
        square_edges = VGroup(
            Line(two_d_axes.coords_to_point(0,0,0), two_d_axes.coords_to_point(0,1.3,0), color=RED_C),
            Line(two_d_axes.coords_to_point(0,1.3,0), two_d_axes.coords_to_point(0,1.3,1.3), color=RED_C),
            Line(two_d_axes.coords_to_point(0,1.3,1.3), two_d_axes.coords_to_point(0,0,1.3), color=RED_C),
            Line(two_d_axes.coords_to_point(0,0,1.3), two_d_axes.coords_to_point(0,0,0), color=RED_C)
        )
        surface_2d_text = MathTex("\\text{Surface: }")
        surface_2d_text.rotate(90*DEGREES, UP)
        surface_2d_text.rotate(90*DEGREES, RIGHT)
        surface_2d_text.next_to(axes_2d_text, IN)
        surface_2d_text.scale(0.9)
        parts_1d_text = MathTex("1\\text{-dimensional parts}")
        parts_1d_text.rotate(90*DEGREES, UP)
        parts_1d_text.rotate(90*DEGREES, RIGHT)
        parts_1d_text.next_to(surface_2d_text, IN)
        parts_1d_text.scale(0.9)
        self.play(Create(square_edges), Write(surface_2d_text),run_time=1.5)
        self.play(Wiggle(square_edges), Write(parts_1d_text))
        self.wait(1)
        
        
        square_vertices = VGroup(
            Dot3D(two_d_axes.coords_to_point(0,0,0), color=RED_C),
            Dot3D(two_d_axes.coords_to_point(0,1.3,0), color=RED_C),
            Dot3D(two_d_axes.coords_to_point(0,1.3,1.3), color=RED_C),
            Dot3D(two_d_axes.coords_to_point(0,0,1.3), color=RED_C)
        )
        parts_0d_2d_text = MathTex("0\\text{-dimensional parts}")
        parts_0d_2d_text.rotate(90*DEGREES, UP)
        parts_0d_2d_text.rotate(90*DEGREES, RIGHT)
        parts_0d_2d_text.next_to(parts_1d_text, IN)
        parts_0d_2d_text.scale(0.9)
        self.play(Create(square_vertices))
        self.play(Wiggle(square_vertices), Write(parts_0d_2d_text))
        
        
        text_2d_group = VGroup(axes_2d_text, surface_2d_text, parts_0d_2d_text, parts_1d_text)
        two_d_stuff = VGroup(square, two_d_y_axis, two_d_z_axis, two_d_y_label, two_d_z_label, square_edges, square_vertices)
        self.play(two_d_stuff.animate.scale(0.5).move_to([0, 0, 2]))
        self.play(text_2d_group.animate.shift(DOWN*3+OUT*1.1))
        
        separator2 = Line([0, 2.5, 4], [0, 2.5, -4], color=GRAY)
        self.play(Create(separator2))
        
        # 3D------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # A cube lies in a 3 dimensional space. 
        three_d_axes = ThreeDAxes([-1,3], [-1,3], [-1,3], 4, 4, 4)
        three_d_axes.move_to([0,5,1.5])
        unit3d = three_d_axes.get_x_unit_size()
        
        cube = Cube(1.3*unit3d, 0.8, RED_C)
        cube.move_to(three_d_axes.coords_to_point(0,0,0), cube.get_corner(DOWN+LEFT+IN))
        self.play(DrawBorderThenFill(cube))
        
        # To map out points on the cube in this space, you’ll use 3 mutually perpendicular axes: the x axis for the width of the cube, the y axis for its length, and the z axis for its height. 
        # You can’t fully describe a cube in a 2 dimensional space with only 2 axes, because you need that extra axis to describe its height. 
        three_d_x_axis = three_d_axes.get_x_axis()
        three_d_y_axis = three_d_axes.get_y_axis()
        three_d_z_axis = three_d_axes.get_z_axis()
        three_d_labels = three_d_axes.get_axis_labels("x", "y", "z")
        
        axes_3d_text = MathTex("\\text{Axes: } 3")
        axes_3d_text.rotate(90*DEGREES, UP)
        axes_3d_text.rotate(90*DEGREES, RIGHT)
        axes_3d_text.next_to(three_d_axes, IN)
        axes_3d_text.scale(0.9)
        
        self.play(Create(three_d_x_axis))
        self.play(Create(three_d_y_axis)) 
        self.play(Create(three_d_z_axis))
        self.play(Write(axes_3d_text))
        
        self.wait(15)

        # The surface of the cube consists of these 2 dimensional faces, 1 dimensional edges, and 0 dimensional vertices. 
            # Make faces wiggle
        surface_3d_text = MathTex("\\text{Surface:}")
        surface_3d_text.rotate(90*DEGREES, UP)
        surface_3d_text.rotate(90*DEGREES, RIGHT)
        surface_3d_text.next_to(axes_3d_text, IN)
        surface_3d_text.scale(0.9)
        self.play(Write(surface_3d_text))
        
        parts_2d_text = MathTex("2\\text{-dimensional parts}")
        parts_2d_text.rotate(90*DEGREES, UP)
        parts_2d_text.rotate(90*DEGREES, RIGHT)
        parts_2d_text.next_to(surface_3d_text, IN)
        parts_2d_text.scale(0.9)
        
        self.play(Wiggle(cube), Write(parts_2d_text))
        
            # Make edges wiggle
        cube_edges = VGroup(
            # Bottom face edges
            Line(three_d_axes.coords_to_point(0,0,0), three_d_axes.coords_to_point(1.3,0,0), color=RED_C),
            Line(three_d_axes.coords_to_point(1.3,0,0), three_d_axes.coords_to_point(1.3,1.3,0), color=RED_C),
            Line(three_d_axes.coords_to_point(1.3,1.3,0), three_d_axes.coords_to_point(0,1.3,0), color=RED_C),
            Line(three_d_axes.coords_to_point(0,1.3,0), three_d_axes.coords_to_point(0,0,0), color=RED_C),
            # Top face edges
            Line(three_d_axes.coords_to_point(0,0,1.3), three_d_axes.coords_to_point(1.3,0,1.3), color=RED_C),
            Line(three_d_axes.coords_to_point(1.3,0,1.3), three_d_axes.coords_to_point(1.3,1.3,1.3), color=RED_C),
            Line(three_d_axes.coords_to_point(1.3,1.3,1.3), three_d_axes.coords_to_point(0,1.3,1.3), color=RED_C),
            Line(three_d_axes.coords_to_point(0,1.3,1.3), three_d_axes.coords_to_point(0,0,1.3), color=RED_C),
            # Vertical edges
            Line(three_d_axes.coords_to_point(0,0,0), three_d_axes.coords_to_point(0,0,1.3), color=RED_C),
            Line(three_d_axes.coords_to_point(1.3,0,0), three_d_axes.coords_to_point(1.3,0,1.3), color=RED_C),
            Line(three_d_axes.coords_to_point(1.3,1.3,0), three_d_axes.coords_to_point(1.3,1.3,1.3), color=RED_C),
            Line(three_d_axes.coords_to_point(0,1.3,0), three_d_axes.coords_to_point(0,1.3,1.3), color=RED_C)
        )
        
        parts_1d_3d_text = MathTex("1\\text{-dimensional parts}")
        parts_1d_3d_text.rotate(90*DEGREES, UP)
        parts_1d_3d_text.rotate(90*DEGREES, RIGHT)
        parts_1d_3d_text.next_to(parts_2d_text, IN)
        parts_1d_3d_text.scale(0.9)
        
        self.play(Create(cube_edges))
        self.play(Wiggle(cube_edges), Write(parts_1d_3d_text))
        
            # Make vertices wiggle
        cube_vertices = VGroup(
            Dot3D(three_d_axes.coords_to_point(0,0,0), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(1.3,0,0), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(1.3,1.3,0), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(0,1.3,0), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(0,0,1.3), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(1.3,0,1.3), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(1.3,1.3,1.3), color=RED_C),
            Dot3D(three_d_axes.coords_to_point(0,1.3,1.3), color=RED_C)
        )
        
        parts_0d_3d_text = MathTex("0\\text{-dimensional parts}")
        parts_0d_3d_text.rotate(90*DEGREES, UP)
        parts_0d_3d_text.rotate(90*DEGREES, RIGHT)
        parts_0d_3d_text.next_to(parts_1d_3d_text, IN)
        parts_0d_3d_text.scale(0.9)
        
        self.play(Create(cube_vertices))
        self.play(Wiggle(cube_vertices), Write(parts_0d_3d_text))
        
        
        text_3d_group = VGroup(axes_3d_text, surface_3d_text, parts_0d_3d_text, parts_1d_3d_text, parts_2d_text)
        three_d_stuff = VGroup(cube, three_d_x_axis, three_d_y_axis, three_d_z_axis, three_d_labels, cube_edges)
        self.play(FadeOut(cube_vertices))
        self.play(three_d_stuff.animate.scale(0.7).shift(OUT*0.5))
        self.play(text_3d_group.animate.shift(OUT*0.4))
        
        # 4D------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # So what if I had the 4 dimensional equivalent of a cube? Let's call this a 4 dimensional hypercube, or a 4-hypercube for short. 
        self.play(one_d_stuff.animate.shift(OUT).scale(0.6))
        self.play(one_d_text.animate.shift(OUT*3).scale(0.6))
        self.play(two_d_stuff.animate.shift(OUT).scale(0.6))
        self.play(text_2d_group.animate.shift(OUT*3).scale(0.6))
        self.play(three_d_stuff.animate.shift(OUT).scale(0.6))
        self.play(text_3d_group.animate.shift(OUT*3).scale(0.6))
        self.play(Uncreate(separator1), Uncreate(separator2), Create(Line([0, -2.5, 4], [0, -2.5, 0], color=GRAY)), Create(Line([0, 2.5, 4], [0, 2.5, 0], color=GRAY)), Create(Line([0,-7.5,0], [0,7.5,0], color=GRAY)))
        self.play(Create(Line([0,-7.5,0], [0,7.5,0], color=GRAY)))
        
        # We can't visualise that completely. But we know how we might be able to construct it. Remember how we constructed the square and the cube. 
        # To construct the cube, we created lines on 3 axes, and shifted them along the axes like so. 
            # Draw 3 mini-axes and a red cube under the separator, then move lines along axes
        mini_axes = ThreeDAxes([-1,3,1], [-1,3,1], [-1,3,1], 4, 4, 4)
        mini_axes.move_to([0, 0, -2.5])
            #mini_labels = mini_axes.get_axis_labels("x","y","z")
        mini_unit = mini_axes.get_x_unit_size()
        mini_a = 1.0
        mini_a_abs = mini_unit*mini_a
        self.play(FadeIn(mini_axes))

            # Red lines on axes 
        mini_xa = labelline(self, mini_axes.coords_to_point(0,0,0), mini_axes.coords_to_point(mini_a,0,0), RED_D, "", IN, PI/2, [RIGHT,OUT])
        mini_ya = labelline(self, mini_axes.coords_to_point(0,0,0), mini_axes.coords_to_point(0,mini_a,0), RED_D, "", LEFT, PI/2, [RIGHT,OUT])
        mini_za = labelline(self, mini_axes.coords_to_point(0,0,0), mini_axes.coords_to_point(0,0,mini_a), RED_D, "", RIGHT, PI/2, [RIGHT,OUT])
        self.play(Create(mini_xa), Create(mini_ya), Create(mini_za))
        
            # Place a small cube at origin of mini-axes
        mini_cube = Cube(mini_a_abs, 0.8, RED_C)
        mini_cube.move_to(mini_axes.coords_to_point(0,0,0), mini_cube.get_corner(DOWN+LEFT+IN))
        
            # Move red lines along perpendicular axes to mimic square construction in 3D
        mini_xa_copy_y = VGroup(mini_xa.copy())
        mini_ya_copy_x = VGroup(mini_ya.copy())
        mini_ya_copy_z = VGroup(mini_ya.copy())
        mini_za_copy_y = VGroup(mini_za.copy())
        mini_za_copy_x = VGroup(mini_za.copy())
        mini_xa_copy_z = VGroup(mini_xa.copy())
        self.play(mini_xa_copy_y.animate.shift(UP*mini_a_abs))
        self.play(mini_ya_copy_x.animate.shift(RIGHT*mini_a_abs))
        self.play(mini_ya_copy_z.animate.shift(OUT*mini_a_abs))
        self.play(mini_za_copy_y.animate.shift(UP*mini_a_abs))
        self.play(mini_za_copy_x.animate.shift(RIGHT*mini_a_abs))
        self.play(mini_xa_copy_z.animate.shift(OUT*mini_a_abs))
        
        
        # We then completed the cube by making faces that were parallel to each other.
            # Draw red plane faces and translate them parallel to construct the cube
        face_yz = Square(mini_a_abs, color=RED_C, fill_opacity=0.25, stroke_opacity=0.25)
        face_yz.rotate(-90*DEGREES, UP)
        face_yz.move_to(mini_axes.coords_to_point(0,0,0), face_yz.get_corner(DOWN+IN))
        self.play(DrawBorderThenFill(face_yz))
        face_yz_far = face_yz.copy()
        self.play(face_yz_far.animate.shift(RIGHT*mini_a_abs))

        face_xz = Square(mini_a_abs, color=RED_C, fill_opacity=0.25, stroke_opacity=0)
        face_xz.rotate(90*DEGREES, RIGHT)
        face_xz.move_to(mini_axes.coords_to_point(0,0,0), face_xz.get_corner(DOWN+IN))
        self.play(DrawBorderThenFill(face_xz))
        face_xz_far = face_xz.copy()
        self.play(face_xz_far.animate.shift(UP*mini_a_abs))

        face_xy = Square(mini_a_abs, color=RED_C, fill_opacity=0.25, stroke_opacity=0.25)
        face_xy.move_to(mini_axes.coords_to_point(0,0,0), face_xy.get_corner(DOWN+LEFT))
        self.play(DrawBorderThenFill(face_xy))
        face_xy_far = face_xy.copy()
        self.play(face_xy_far.animate.shift(OUT*mini_a_abs))
        
        
        # Based on this pattern, to create a 4-hypercube, we would need 4 mutually perpendicular axes. Let's call them x, y, z and w. We would create the hypercube by shifting lines, planes and cubes on the axes.
            # Fade out cube faces/lines and draw four separate axes with blanks and labels x,y,z,w
        self.play(FadeOut(mini_cube), FadeOut(mini_xa), FadeOut(mini_ya), FadeOut(mini_za),
                  FadeOut(mini_xa_copy_y), FadeOut(mini_ya_copy_x), FadeOut(mini_ya_copy_z),
                  FadeOut(mini_za_copy_y), FadeOut(mini_za_copy_x), FadeOut(mini_xa_copy_z),
                  FadeOut(face_yz), FadeOut(face_yz_far), FadeOut(face_xz), FadeOut(face_xz_far),
                  FadeOut(face_xy), FadeOut(face_xy_far), FadeOut(mini_axes))

        self.wait(1.5)

         # Four blanks in bottom half with labels and small axis graphics (random orientations)
        x = labelline(self, [0, -4, -3.0], [0, -3.6, -3.0], GRAY, "x", IN, PI/2, [RIGHT,OUT])
        y = labelline(self, [0, -3, -3.0], [0, -2.6, -3.0], GRAY, "y", IN, PI/2, [RIGHT,OUT])
        z = labelline(self, [0, -2, -3.0], [0, -1.6, -3.0], GRAY, "z", IN, PI/2, [RIGHT,OUT])
        w = labelline(self, [0, -1, -3.0], [0, -0.6, -3.0], GRAY, "w", IN, PI/2, [RIGHT,OUT])
        self.play(Create(x), Create(y), Create(z), Create(w))
        
        xgraphic = Arrow3D([0,0,0], [1,0,0], color=WHITE)
        xgraphic.next_to(x, OUT)
        ygraphic = Arrow3D([0,0,0], [0,1,0], color=WHITE)
        ygraphic.next_to(y, OUT)
        zgraphic = Arrow3D([0,0,0], [0,0,1], color=WHITE)
        zgraphic.next_to(z, OUT)
        wgraphic = Arrow3D([0,0,0], [1,0,0], color=WHITE)
        wgraphic.next_to(w, OUT)
        self.play(Create(xgraphic), Create(ygraphic), Create(zgraphic), Create(wgraphic))

        four_axes_group = VGroup(x, y, z, w, xgraphic, ygraphic, zgraphic, wgraphic)
        
        self.wait(11)
        
        # And based on the pattern we've seen so far, on the surface of the 4-hypercube, we'd have 0, 1, 2 and 3 dimensional parts. 
            # Surface list next to axes
        surf4 = MathTex("\\text{Surface:}")
        surf4.rotate(90*DEGREES, UP)
        surf4.rotate(90*DEGREES, RIGHT)
        s0 = MathTex("0\\text{-dimensional parts}")
        s1 = MathTex("1\\text{-dimensional parts}")
        s2 = MathTex("2\\text{-dimensional parts}")
        s3 = MathTex("3\\text{-dimensional parts}")
        for t in [s0,s1,s2,s3]:
            t.rotate(90*DEGREES, UP)
            t.rotate(90*DEGREES, RIGHT)
        surf_group4 = VGroup(surf4, s0, s1, s2, s3)
        surf_group4.arrange(IN, buff=0.4)
        surf_group4.move_to([0, 2, -2])
        surf_group4.scale(0.8)
        self.play(Write(surf4), run_time=0.5)
        self.play(Write(s0), run_time=1) 
        self.play(Write(s1), run_time=1)
        self.play(Write(s2), run_time=1)
        self.play(Write(s3), run_time=1)

        four_dim_group = VGroup(four_axes_group, surf_group4)
        
        # In general, if we want to create an n-dimensional hypercube, we need n mutually perpendicular axes to describe the space it sits in. And on the surface of the n-hypercube, you would be able to identify lower dimensional parts, right from 0 to n-1 dimensions, just as on a cube, you can identify 0 to 2 dimensional parts. 
            # Move 4D stuff to bottom-left; draw general n-axis blanks and surface list
        self.play(four_dim_group.animate.move_to([0, -4, -2]).scale(0.7))
        
        self.play(Create(Line([0,-1,0], [0,-1,-4], color=GRAY)))

        
        nx = labelline(self, [0, -0.4, -3.0], [0, 0, -3.0], GRAY, "x", IN, PI/2, [RIGHT,OUT])
        ny = labelline(self, [0, 0.4, -3.0], [0, 1, -3.0], GRAY, "y", IN, PI/2, [RIGHT,OUT])
        dots = MathTex("\cdots")
        dots.rotate(90*DEGREES, UP)
        dots.rotate(90*DEGREES, RIGHT)
        n = labelline(self, [0, 1.4, -3.0], [0, 2, -3.0], GRAY, "n^{\\text{th}}\\, \\text{axis}", IN, PI/2, [RIGHT,OUT])
        nxgraphic = Arrow3D([0,0,0], [1,0,0], color=WHITE)
        nygraphic = Arrow3D([0,0,0], [0,1,0], color=WHITE)
        ngraphic = Arrow3D([0,0,0], [0,0,1], color=WHITE)
        
        nxgraphic.next_to(nx, OUT)
        nygraphic.next_to(ny, OUT)
        dots.next_to(ny, UP)
        n.next_to(dots, UP)
        ngraphic.next_to(n, OUT)
        
        ngroup = VGroup(nx, ny, dots, n, nxgraphic, nygraphic, ngraphic)
        ngroup.scale(0.7)
    
        self.play(Create(ngroup), run_time=2)
        self.wait(5)

            # Surface: 0..n-1 dimensional
        surfN = MathTex("\\text{Surface:}")
        sn0 = MathTex("0\\text{-dimensional}")
        sn1 = MathTex("1\\text{-dimensional}")
        sndots = MathTex("\cdots")
        snNm1 = MathTex("(n-1)\\text{-dimensional}")
        for t in [surfN, sn0, sn1, sndots, snNm1]:
            t.rotate(90*DEGREES, UP); t.rotate(90*DEGREES, RIGHT)
        surfN_group = VGroup(surfN, sn0, sn1, sndots, snNm1).arrange(IN, buff=0.35)
        surfN_group.scale(0.7)
        surfN_group.move_to([0, 5, -2])
        self.play(Write(surfN), run_time=2); self.play(Write(sn0), run_time=1); self.play(Write(sn1), run_time=1); self.play(Write(sndots), run_time=1); self.play(Write(snNm1), run_time=1)

        self.wait(9)