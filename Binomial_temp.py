from manim import *

#Defining useful functions
def labelline(self, start, end, color=WHITE, label="", direction=DOWN, rotateangle=0, rotatevector=OUT):
     line = Line(start, end, 0, None, color=color)
     l = MathTex(label)
     l.next_to(line, direction)
     l.rotate(rotateangle, rotatevector)
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
    
    

class Intro(Scene):
    def construct(self):
        #Title--------------------------------------------------------------------------------------------------------------------------------
        title = Text("The Binomial Theorem", font_size=80)
        self.play(Write(title), run_time=2)
        self.play(title.animate.move_to([0,3,0]).scale(0.5), run_time=2)
        
    
        
        #Binomial theorem--------------------------------------------------------------------------------------------------------------------------------
        lhs1 = MathTex(r"(", "a", "+", "b", ")", "^", "n")
        rhs1 = MathTex(
            "=", r"\binom{n}{0}", "a", "^", "n", "b", "^0",
            "+", r"\binom{n}{1}", "a", "^{", "n-1", "}", "b", "^1",
            "+", r"\binom{n}{2}", "a", "^{", "n-2", "}", "b", "^2",
            "+", r"\cdots",
            "+", r"\binom{n}{n}", "a", "^0", "b", "^n"
        )
        ncr = MathTex(r"\binom{n}{r} = \frac{n!}{(n-r)!\, r!}")
        where = MathTex("Where")
        
        lhs1.set_color_by_tex("a", RED_C)
        lhs1.set_color_by_tex("b", BLUE_C)
        lhs1.set_color_by_tex("n", GREEN_C)
        rhs1.set_color_by_tex("a", RED_C)
        rhs1.set_color_by_tex("b", BLUE_C)
        rhs1.set_color_by_tex("n", GREEN_C)
        ncr.set_color_by_tex("a", RED_C)
        ncr.set_color_by_tex("b", BLUE_C)
        ncr.set_color_by_tex("n", GREEN_C)
        
        lhs1.scale(0.95)
        rhs1.scale(0.95)
        ncr.scale(0.9)
        where.scale(0.9)
        
        self.play(Write(lhs1), run_time=1.5)
        self.play(lhs1.animate.move_to([-6,0,0]), run_time=1.5)
        rhs1.next_to(lhs1, RIGHT)
        self.play(Write(rhs1))
        where.move_to([-2, -1.5, 0])
        ncr.next_to(where, RIGHT)
        self.play(Write(where))
        self.play(Write(ncr))
        
        lhs1.generate_target()
        lhs1.target.move_to([-6,1,0])
        where.generate_target()
        where.target.move_to([-2,-0.5,0])
        rhs1.generate_target()
        rhs1.target.next_to(lhs1.target, RIGHT)
        ncr.generate_target()
        ncr.target.next_to(where.target, RIGHT)
        
        self.play(MoveToTarget(lhs1), MoveToTarget(rhs1), MoveToTarget(where), MoveToTarget(ncr), run_time = 1)
        
        
        
        #FOIL--------------------------------------------------------------------------------------------------------------------------------
        lhsfoil = MathTex("(", "a", "+", "b", ")", "^", "5")
        rhsfoil1 = MathTex(
            r"=", 
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")"
        )
        
        lhsfoil.set_color_by_tex("a", RED_C)
        lhsfoil.set_color_by_tex("b", BLUE_C)
        lhsfoil.set_color_by_tex("5", GREEN_C)
        
        rhsfoil1.set_color_by_tex("a", RED_C)
        rhsfoil1.set_color_by_tex("b", BLUE_C)
        
        
        self.play(Uncreate(where), Uncreate(ncr))
        
        lhsfoil.move_to([-6,-2,0])
        rhsfoil1.next_to(lhsfoil, RIGHT)
        self.play(Write(lhsfoil))
        self.play(Write(rhsfoil1))
        
        rhsfoil2 = MathTex(
            r"=",
            r"(", r"a", r"^2", r"+", r"2", r"a", r"b", r"+", r"b", r"^2", r")",
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")"
        )
        rhsfoil2.next_to(lhsfoil, RIGHT)
        rhsfoil2.set_color_by_tex("a", RED_C)
        rhsfoil2.set_color_by_tex("b", BLUE_C)
        self.play(TransformMatchingShapes(rhsfoil1, rhsfoil2))
        
        rhsfoil3 = MathTex(
            r"=",
            r"(", r"a", r"^3", r"+", r"3", r"a", r"^2", r"b", r"+", r"3", r"a", r"b", r"^2", r"+", r"b", r"^3", r")",
            r"(", r"a", r"+", r"b", r")",
            r"(", r"a", r"+", r"b", r")"
        )
        rhsfoil3.set_color_by_tex("a", RED_C)
        rhsfoil3.next_to(lhsfoil, RIGHT)
        rhsfoil3.set_color_by_tex("b", BLUE_C)
        self.play(TransformMatchingShapes(rhsfoil2, rhsfoil3))
        
        rhsfoil4 = MathTex(
            r"=",
            r"(", r"a", r"^4", r"+", r"4", r"a", r"^3", r"b", r"+", r"6", r"a", r"^2", r"b", r"^2", r"+", r"4", r"a", r"b", r"^3", r"+", r"b", r"^4", r")",
            r"(", r"a", r"+", r"b", r")"
        )
        rhsfoil4.next_to(lhsfoil, RIGHT)
        rhsfoil4.set_color_by_tex("a", RED_C)
        rhsfoil4.set_color_by_tex("b", BLUE_C)
        self.play(TransformMatchingShapes(rhsfoil3, rhsfoil4))
        
        rhsfoil5 = MathTex(
            r"=",
            r"a", r"^5", r"+",
            r"5", r"a", r"^4", r"b", r"+",
            r"10", r"a", r"^3", r"b", r"^2", r"+",
            r"10", r"a", r"^2", r"b", r"^3", r"+",
            r"5", r"a", r"b", r"^4", r"+",
            r"b", r"^5"
        )
        rhsfoil5.next_to(lhsfoil, RIGHT)
        rhsfoil5.set_color_by_tex("a", RED_C)
        rhsfoil5.set_color_by_tex("b", BLUE_C)
        self.play(TransformMatchingShapes(rhsfoil4, rhsfoil5))
        
        
        
        
        #Plug in numbers--------------------------------------------------------------------------------------------------------------------------------
        lhs2 = MathTex(r"(", "a", "+", "b", ")", "^", "5")
        rhs2l1 = MathTex(
            "=", r"\binom{5}{0}", "a", "^", "5", "b", "^0",
            "+", r"\binom{5}{1}", "a", "^{", "4", "}", "b", "^1",
            "+", r"\binom{5}{2}", "a", "^{", "3", "}", "b", "^2",
            "+", r"\binom{5}{3}", "a", "^{", "2", "}", "b", "^3",
            "+", r"\binom{5}{4}", "a", "^{", "1", "}", "b", "^4",
        )
        rhs2l2 = MathTex("\phantom{+}+", r"\binom{5}{5}", "a", "^0", "b", "^5")
        rhs2 = VGroup(rhs2l1, rhs2l2)
        
        lhs2.set_color_by_tex("a", RED_C)
        lhs2.set_color_by_tex("b", BLUE_C)
        lhs2.set_color_by_tex("5", GREEN_C)
        rhs2l1.set_color_by_tex("a", RED_C)
        rhs2l1.set_color_by_tex("b", BLUE_C)
        rhs2l1.set_color_by_tex("5", GREEN_C)
        rhs2l2.set_color_by_tex("a", RED_C)
        rhs2l2.set_color_by_tex("b", BLUE_C)
        rhs2l2.set_color_by_tex("5", GREEN_C)

        lhs2.scale(0.95)
        rhs2l1.scale(0.95)
        rhs2l2.scale(0.95)
        
        lhs2.move_to([-6,1,0])
        rhs2l1.next_to(lhs2, RIGHT)
        
        rhs3 = MathTex(
            r"=",
            r"a", r"^5", r"+",
            r"5", r"a", r"^4", r"b", r"+",
            r"10", r"a", r"^3", r"b", r"^2", r"+",
            r"10", r"a", r"^2", r"b", r"^3", r"+",
            r"5", r"a", r"b", r"^4", r"+",
            r"b", r"^5"
        )
        rhs3.next_to(lhs2)
        rhs3.set_color_by_tex("a", RED_C)
        rhs3.set_color_by_tex("b", BLUE_C)
        rhs3.set_color_by_tex("5", GREEN_C)
        
        self.play(TransformMatchingShapes(lhs1, lhs2))
        self.play(TransformMatchingShapes(rhs1, rhs2l1))
        self.play(TransformMatchingShapes(rhs2, rhs3))
        
       
        #Summary of visuals----------------------------------------------------------------------------------------------------------------------------------
        
        
class Basic(ThreeDScene):
    def construct(self):
        
        #We start with a pair of axes.
        sqaxes = Axes([-1, 3], [-1, 3], 7, 7)
        unit = sqaxes.get_x_unit_size()
        labels = sqaxes.get_axis_labels("x", "y")
        aabs = 1.3*unit
        aax = 1.3
        babs = 0.7*unit
        bax = 0.7
        
        self.play(FadeIn(sqaxes), FadeIn(labels), run_time=1.5)
        self.wait(1.5)
        
        
        #Let’s say we measure some length, a, along each axis.
        xa = Line(sqaxes.coords_to_point(0,0), sqaxes.coords_to_point(aax,0), color=RED_C)
        ya = Line(sqaxes.coords_to_point(0,0), sqaxes.coords_to_point(0,aax), color=RED_C)
        self.play(Create(xa), Create(ya), run_time=1.5)
        self.wait(1)
        
        
        #We can then use these lines to make a square with side length a. The area of the square, the space it occupies, is a2.
        square = Square(aabs, color=RED_C, fill_opacity=0.8)
        square.align_to(sqaxes.coords_to_point(0,0), DL)
        sqleftlabel = MathTex("a").next_to(square, LEFT)
        sqdownlabel = MathTex("a").next_to(square, DOWN)
        sqleftlabel.set_color(RED_C)
        sqdownlabel.set_color(RED_C)
        area_a2 = MathTex(r"a", r"^2")
        area_a2.move_to(square)
        
        self.play(Write(sqleftlabel), Write(sqdownlabel),run_time=1)
        self.wait(3)
        self.play(DrawBorderThenFill(square), FadeOut(xa), FadeOut(ya),run_time=2)
        self.wait(1)
        self.play(Write(area_a2))
        self.wait(1)
        
                
        #We now increase the length of the sides by b.
        xb = labelline(self, sqaxes.coords_to_point(aax,0), sqaxes.coords_to_point(aax+bax,0), BLUE_D, "b", DOWN)
        yb = labelline(self, sqaxes.coords_to_point(0,aax), sqaxes.coords_to_point(0,aax+bax), BLUE_D, "b", LEFT)
        self.play(Create(xb), Create(yb), FadeOut(area_a2), run_time=1.5)
        
        
        #What is the space occupied by the new square? 
        x2a = Line(sqaxes.coords_to_point(0,0), sqaxes.coords_to_point(aax,0), 0, color=RED_C)
        x2b = Line(sqaxes.coords_to_point(aax,0), sqaxes.coords_to_point(aax+bax,0), 0, color=BLUE_D)
        y2a = Line(sqaxes.coords_to_point(0,0), sqaxes.coords_to_point(0,aax), 0, color=RED_C)
        y2b = Line(sqaxes.coords_to_point(0,aax), sqaxes.coords_to_point(0,aax+bax), 0, color=BLUE_D)
        
        move(self, [x2a, x2b], 0, aabs+babs, UP, duration=1) 
        move(self, [y2a, y2b], 0, aabs+babs, RIGHT, duration=1)
        
        big_square = Square(aabs+babs, color=PURPLE_A, fill_opacity=0.8, stroke_opacity=0)
        big_square.align_to(sqaxes.coords_to_point(0,0), DL)
        self.play(DrawBorderThenFill(big_square), FadeOut(square), run_time=1)
        

        #One algebraic representation of this area is (a+b)2.
        move(self, [sqaxes, labels, sqleftlabel, sqdownlabel, xb, yb, x2a, x2b, y2a, y2b, big_square], 0, 3, LEFT)
        
        x3a = Line(sqaxes.coords_to_point(0,0), sqaxes.coords_to_point(aax,0), color=RED_C)
        x3b = Line(sqaxes.coords_to_point(aax,0), sqaxes.coords_to_point(aax+bax,0), color=BLUE_D)
        x3group = VGroup(x3a,x3b)
        y3a = Line(sqaxes.coords_to_point(0,0), sqaxes.coords_to_point(0, aax), color=RED_C) 
        y3b = Line(sqaxes.coords_to_point(0,aax), sqaxes.coords_to_point(0, aax+bax), color=BLUE_D)
        y3group = VGroup(y3a,y3b)
        
        self.play(x3group.animate.move_to([2,2,0]).scale(0.5))
        
        mult1 = MathTex(r"\times")
        mult1.next_to(x3group, RIGHT)
        self.play(Write(mult1))
        
        y3group.generate_target()
        y3group.target.next_to(mult1, RIGHT)
        y3group.target.scale(0.5)
        self.play(MoveToTarget(y3group), run_time=2)
        
        equals1 = MathTex("=")
        equals1.next_to(y3group, RIGHT)
        self.play(Write(equals1))
        
        rhs4 = MathTex(r"(", "a", "+", "b", ")", "^", "2")
        rhs4.set_color_by_tex("a", RED_C)
        rhs4.set_color_by_tex("b", BLUE_C)
        rhs4.set_color_by_tex("2", GREEN_C)
        rhs4.next_to(equals1, RIGHT)
        self.play(Write(rhs4))
        self.wait(3)
        
        #But another way to represent it is as a polynomial, an expression which only contains terms in the form of a raised to some power times b raised to some power. 
        poly = MathTex(
         r"C_1", r"a", r"^p", r"b", r"^q", 
         r"+", 
         r"C_2", r"a", r"^r", r"b", r"^s",
         r"+", 
         r"C_3", r"a", r"^m", r"b", r"^n",
         r"+", 
         r"\cdots"
        )
        poly.scale(0.85)
        poly.set_color_by_tex("a", RED_C)
        poly.set_color_by_tex("b", BLUE_C)
        poly.move_to([4,0,0])
        self.play(Write(poly), run_time=2)
        self.wait(3)
        
        #We can get the polynomial by breaking the square up into pieces,... 
        x4a = Line(sqaxes.coords_to_point(0,aax), sqaxes.coords_to_point(aax,aax), color=RED_C)
        y4a = Line(sqaxes.coords_to_point(aax,0), sqaxes.coords_to_point(aax, aax), color=RED_C)
        x4b = Line(sqaxes.coords_to_point(aax,aax), sqaxes.coords_to_point(aax+bax, aax), color=BLUE_D)
        y4b = Line(sqaxes.coords_to_point(aax,aax), sqaxes.coords_to_point(aax, aax+bax), color=BLUE_D)
        
        self.play(Create(x4a), Create(y4a))
        self.play(Create(x4b), Create(y4b))
        
        b2_square = Square(babs, color=BLUE_D, fill_opacity=0.8, stroke_opacity=0)
        ab_rect_1 = Rectangle(PURPLE_A, babs, aabs, fill_opacity=0.8, stroke_opacity=0)
        ab_rect_2 = Rectangle(PURPLE_A, aabs, babs, fill_opacity=0.8, stroke_opacity=0)
        
        square.align_to(sqaxes.coords_to_point(0,0), DL)
        b2_square.align_to(sqaxes.coords_to_point(aax,aax), DL)
        ab_rect_1.align_to(sqaxes.coords_to_point(0,aax), DL)
        ab_rect_2.align_to(sqaxes.coords_to_point(aax,0), DL)
        
        self.play(DrawBorderThenFill(square), DrawBorderThenFill(b2_square), DrawBorderThenFill(ab_rect_1), DrawBorderThenFill(ab_rect_2), FadeOut(big_square), run_time=2)
        
        
        #...and then adding up the space each piece occupies.
        a2_copy = square.copy()
        b2_copy = b2_square.copy()
        ab_1_copy = ab_rect_1.copy()
        ab_2_copy = ab_rect_2.copy()
        
        a2_copy.stroke_width = 0
        self.play(FadeOut(poly), a2_copy.animate.move_to([2,0,0]).scale(0.5))
        
        plus1 = MathTex("+")
        plus1.next_to(a2_copy, RIGHT)
        self.play(Write(plus1))
        
        ab_1_copy.generate_target()
        ab_1_copy.target.next_to(plus1, RIGHT, buff=-0.3)
        ab_1_copy.target.scale(0.5)
        self.play(MoveToTarget(ab_1_copy))
        
        ab_2_copy.generate_target()
        ab_2_copy.target.rotate(-PI/2)
        ab_2_copy.target.scale(0.5)
        ab_2_copy.target.next_to(ab_1_copy, DR, buff=-0.5)
        ab_2_copy.target.shift(LEFT*0.5)
        self.play(MoveToTarget(ab_2_copy))
        
        plus2 = MathTex("+")
        plus2.next_to(ab_1_copy, RIGHT, buff=0.6)
        self.play(Write(plus2))
        
        b2_copy.generate_target()
        b2_copy.target.next_to(plus2, RIGHT)
        b2_copy.target.scale(0.5)
        self.play(MoveToTarget(b2_copy))
        self.wait(1)
        
        #So, the total space occupied can be represented by the polynomial a2+2ab+b2. 
        a22abb2 = MathTex(
         r"=", 
         r"a^2", 
         r"+", 
         r"2", r"ab", 
         r"+", 
         r"b^2"
        )
        a22abb2.set_color_by_tex("a^2", RED_C)
        a22abb2.set_color_by_tex("ab", PURPLE_C)
        a22abb2.set_color_by_tex("b^2", BLUE_C)
        a22abb2.next_to(ab_2_copy, DOWN)
        self.play(Write(a22abb2))
        
        self.wait(4)

        aplusbsqfull = MathTex()
        
        #3D-------------------------------------------------------------------------------------------------------------------------------
        
        self.clear()
        
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
        
        # We could do the same with a cube. We create a cube with volume a3,... 
        
        x5a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(a3dax,0,0), RED_D, "", IN, PI/2, RIGHT)
        y5a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(0,a3dax,0), RED_D, "", LEFT, PI/2, RIGHT)
        z5a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(0,0,a3dax), RED_D, "", RIGHT, PI/2, RIGHT)
        self.play(Create(x5a), Create(y5a), Create(z5a))
        
        a3 = Cube(a3dabs, 0.8, RED_C)
        a3_corner = a3.get_corner(DOWN+LEFT+IN)
        a3.move_to(cuaxes.coords_to_point(0,0,0), a3_corner)
        
        self.play(DrawBorderThenFill(a3))
        
        
        # ...and then increase the side length by b. 
        
        x6b = labelline(self, cuaxes.coords_to_point(a3dax,0,0), cuaxes.coords_to_point(a3dax+b3dax,0,0), BLUE_D, "", IN, PI/2, RIGHT)
        y6b = labelline(self, cuaxes.coords_to_point(0,a3dax,0), cuaxes.coords_to_point(0,a3dax+b3dax,0), BLUE_D, "", LEFT, PI/2, RIGHT)
        z6b = labelline(self, cuaxes.coords_to_point(0,0,a3dax), cuaxes.coords_to_point(0,0,a3dax+b3dax), BLUE_D, "", RIGHT, PI/2, RIGHT)
        self.play(Create(x6b), Create(y6b), Create(z6b), run_time=1.5)
        
        
        # The volume, or the space occupied by the new cube is (a+b)3. 
        big_cube = Cube(a3dabs+b3dabs, 0.8, PURPLE_A)
        big_cube_corner = a3.get_corner(DOWN+LEFT+IN)
        big_cube.move_to(cuaxes.coords_to_point(0,0,0), big_cube_corner)
        self.play(FadeOut(a3), DrawBorderThenFill(big_cube))
        
        self.move_camera(phi=80*DEGREES, theta=0*DEGREES)
        self.play(cuaxes.animate.shift(DOWN*3), labels2.animate.shift(DOWN*3), x5a.animate.shift(DOWN*3), y5a.animate.shift(DOWN*3), z5a.animate.shift(DOWN*3), x6b.animate.shift(DOWN*3), y6b.animate.shift(DOWN*3), z6b.animate.shift(DOWN*3), big_cube.animate.shift(DOWN*3))
        
        
        x7a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(a3dax,0,0), RED_C, "", IN, PI/2, RIGHT)
        y7a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(0,a3dax,0), RED_C, "", LEFT, PI/2, RIGHT)
        z7a = labelline(self, cuaxes.coords_to_point(0,0,0), cuaxes.coords_to_point(0,0,a3dax), RED_C, "", RIGHT, PI/2, RIGHT)
        x8b = labelline(self, cuaxes.coords_to_point(a3dax,0,0), cuaxes.coords_to_point(a3dax+b3dax,0,0), BLUE_D, "", IN, PI/2, RIGHT)
        y8b = labelline(self, cuaxes.coords_to_point(0,a3dax,0), cuaxes.coords_to_point(0,a3dax+b3dax,0), BLUE_D, "", LEFT, PI/2, RIGHT)
        z8b = labelline(self, cuaxes.coords_to_point(0,0,a3dax), cuaxes.coords_to_point(0,0,a3dax+b3dax), BLUE_D, "", RIGHT, PI/2, RIGHT)
        
        x7grp = VGroup(x7a,x8b)
        y7grp = VGroup(y7a,y8b)
        z7grp = VGroup(z7a,z8b)
        

        x7grp.scale(0.5)
        x7grp.rotate(-90*DEGREES, UP)
        times1 = MathTex(r"\times")
        times1.scale(0.5)
        times1.rotate(-90*DEGREES, UP)
        y7grp.scale(0.5)
        y7grp.rotate(-90*DEGREES, UP)
        times2 = MathTex(r"\times")
        times2.scale(0.5)
        times2.rotate(-90*DEGREES, UP)
        z7grp.scale(0.5)
        z7grp.rotate(-90*DEGREES, UP)
        equation_group = VGroup(x7grp, times1, y7grp, times2, z7grp)
        equation_group.arrange(UP, buff=0.4)
        equation_group.move_to([0, 2, 3])
        self.play(Create(x7grp))
        self.play(Write(times1))
        self.play(Create(y7grp))
        self.play(Write(times2))
        self.play(Create(z7grp))
        
        aplusbcube = MathTex(r"=", r"(", r"a", r"+", r"b", r")", r"^3")
        aplusbcube.set_color_by_tex("a",RED_C)
        aplusbcube.set_color_by_tex("b",BLUE_C)
        aplusbcube.next_to(z7grp,UP)
        aplusbcube.shift(1*UP)
        aplusbcube.rotate(90*DEGREES, UP)
        aplusbcube.rotate(90*DEGREES, RIGHT)
        self.play(Write(aplusbcube))
        
        
        # If we break the cube down into pieces,... 
        x9grp = VGroup(Line(cuaxes.coords_to_point(0,0,a3dax), cuaxes.coords_to_point(a3dax,0,a3dax), color=RED_C), 
                       Line(cuaxes.coords_to_point(a3dax,0,a3dax), cuaxes.coords_to_point(a3dax+b3dax,0,a3dax), color=BLUE_C))
        x10grp = VGroup(Line(cuaxes.coords_to_point(a3dax+b3dax,0,a3dax), cuaxes.coords_to_point(a3dax+b3dax,a3dax,a3dax), color=RED_C), 
                       Line(cuaxes.coords_to_point(a3dax+b3dax,a3dax,a3dax), cuaxes.coords_to_point(a3dax+b3dax,a3dax+b3dax,a3dax), color=BLUE_C))
        x11grp = VGroup(Line(cuaxes.coords_to_point(a3dax+b3dax,a3dax+b3dax,a3dax), cuaxes.coords_to_point(a3dax,a3dax+b3dax,a3dax), color=BLUE_C), 
                       Line(cuaxes.coords_to_point(a3dax,a3dax+b3dax,a3dax), cuaxes.coords_to_point(0,a3dax+b3dax,a3dax), color=RED_C))
        x12grp = VGroup(Line(cuaxes.coords_to_point(0,a3dax+b3dax,a3dax), cuaxes.coords_to_point(0,a3dax,a3dax), color=BLUE_C), 
                       Line(cuaxes.coords_to_point(0,a3dax,a3dax), cuaxes.coords_to_point(0,0,a3dax), color=RED_C))
        self.play(Create(x9grp), run_time=0.5)
        self.play(Create(x10grp), run_time=0.5)
        self.play(Create(x11grp), run_time=0.5)
        self.play(Create(x12grp), run_time=0.5)
        
        
        y9grp = VGroup(Line(cuaxes.coords_to_point(a3dax,0,0), cuaxes.coords_to_point(a3dax,a3dax,0), color=RED_C), 
                       Line(cuaxes.coords_to_point(a3dax,a3dax,0), cuaxes.coords_to_point(a3dax,a3dax+b3dax,0), color=BLUE_C))
        y10grp = VGroup(Line(cuaxes.coords_to_point(a3dax,a3dax+b3dax,0), cuaxes.coords_to_point(a3dax,a3dax+b3dax,a3dax), color=RED_C), 
                       Line(cuaxes.coords_to_point(a3dax,a3dax+b3dax,a3dax), cuaxes.coords_to_point(a3dax,a3dax+b3dax,a3dax+b3dax), color=BLUE_C))
        y11grp = VGroup(Line(cuaxes.coords_to_point(a3dax,a3dax+b3dax,a3dax+b3dax), cuaxes.coords_to_point(a3dax,a3dax,a3dax+b3dax), color=BLUE_C), 
                       Line(cuaxes.coords_to_point(a3dax,a3dax,a3dax+b3dax), cuaxes.coords_to_point(a3dax,0,a3dax+b3dax), color=RED_C))
        y12grp = VGroup(Line(cuaxes.coords_to_point(a3dax,0,a3dax+b3dax), cuaxes.coords_to_point(a3dax,0,a3dax), color=BLUE_C), 
                       Line(cuaxes.coords_to_point(a3dax,0,a3dax), cuaxes.coords_to_point(a3dax,0,0), color=RED_C))
        self.play(Create(y9grp), run_time=0.5)
        self.play(Create(y10grp), run_time=0.5)
        self.play(Create(y11grp), run_time=0.5)
        self.play(Create(y12grp), run_time=0.5)
        
        
        z9grp = VGroup(Line(cuaxes.coords_to_point(0,a3dax,0), cuaxes.coords_to_point(0,a3dax,a3dax), color=RED_C), 
                       Line(cuaxes.coords_to_point(0,a3dax,a3dax), cuaxes.coords_to_point(0,a3dax,a3dax+b3dax), color=BLUE_C))
        z10grp = VGroup(Line(cuaxes.coords_to_point(0,a3dax,a3dax+b3dax), cuaxes.coords_to_point(a3dax,a3dax,a3dax+b3dax), color=RED_C), 
                       Line(cuaxes.coords_to_point(a3dax,a3dax,a3dax+b3dax), cuaxes.coords_to_point(a3dax+b3dax,a3dax,a3dax+b3dax), color=BLUE_C))
        z11grp = VGroup(Line(cuaxes.coords_to_point(a3dax+b3dax,a3dax,a3dax+b3dax), cuaxes.coords_to_point(a3dax+b3dax,a3dax,a3dax), color=BLUE_C), 
                       Line(cuaxes.coords_to_point(a3dax+b3dax,a3dax,a3dax), cuaxes.coords_to_point(a3dax+b3dax,a3dax,0), color=RED_C))
        z12grp = VGroup(Line(cuaxes.coords_to_point(a3dax+b3dax,a3dax,0), cuaxes.coords_to_point(a3dax,a3dax,0), color=BLUE_C), 
                       Line(cuaxes.coords_to_point(a3dax,a3dax,0), cuaxes.coords_to_point(0,a3dax,0), color=RED_C))
        self.play(Create(z9grp), run_time=0.5)
        self.play(Create(z10grp), run_time=0.5)
        self.play(Create(z11grp), run_time=0.5)
        self.play(Create(z12grp), run_time=0.5)
        
        acubed = Cube(a3dabs, 0.8, RED_C)
        bcubed = Cube(b3dabs, 0.8, BLUE_C)
        aba = Prism([a3dabs, b3dabs, a3dabs], fill_opacity = 0.8, fill_color = MAROON_C)
        aab = Prism([a3dabs, a3dabs, b3dabs], fill_opacity = 0.8, fill_color = MAROON_C)
        baa = Prism([b3dabs, a3dabs, a3dabs], fill_opacity = 0.8, fill_color = MAROON_C)
        bba = Prism([b3dabs, b3dabs, a3dabs], fill_opacity = 0.8, fill_color = PURPLE_C)
        bab = Prism([b3dabs, a3dabs, b3dabs], fill_opacity = 0.8, fill_color = PURPLE_C)
        abb = Prism([a3dabs, b3dabs, b3dabs], fill_opacity = 0.8, fill_color = PURPLE_C)
        
        
        acubed.move_to(cuaxes.coords_to_point(0,0,0), acubed.get_corner(DOWN+LEFT+IN))
        bcubed.move_to(cuaxes.coords_to_point(a3dax,a3dax,a3dax), bcubed.get_corner(DOWN+LEFT+IN))
        aba.move_to(cuaxes.coords_to_point(0,a3dax,0), aba.get_corner(DOWN+LEFT+IN))
        aab.move_to(cuaxes.coords_to_point(0,0,a3dax), aab.get_corner(DOWN+LEFT+IN))
        baa.move_to(cuaxes.coords_to_point(a3dax,0,0), baa.get_corner(DOWN+LEFT+IN))
        bba.move_to(cuaxes.coords_to_point(a3dax,a3dax,0), bba.get_corner(DOWN+LEFT+IN))        
        bab.move_to(cuaxes.coords_to_point(a3dax,0,a3dax), bab.get_corner(DOWN+LEFT+IN))
        abb.move_to(cuaxes.coords_to_point(0,a3dax,a3dax), abb.get_corner(DOWN+LEFT+IN))
        
        self.play(FadeOut(big_cube), DrawBorderThenFill(acubed), DrawBorderThenFill(bcubed), DrawBorderThenFill(aba), DrawBorderThenFill(aab), DrawBorderThenFill(baa), DrawBorderThenFill(bba), DrawBorderThenFill(bab), DrawBorderThenFill(abb))
        self.play(Uncreate(x9grp), Uncreate(y9grp), Uncreate(z9grp), Uncreate(x10grp), Uncreate(y10grp), Uncreate(z10grp), Uncreate(x11grp), Uncreate(y11grp), Uncreate(z11grp), Uncreate(x12grp), Uncreate(y12grp), Uncreate(z12grp))
        
        # ...we get a polynomial by looking at how the space occupied by the smaller pieces add up. 
        acubed_copy = acubed.copy()
        acubed_copy.scale(0.4)
        bcubed_copy = bcubed.copy()
        bcubed_copy.scale(0.4)
        aba_copy = Prism([b3dabs, a3dabs, a3dabs], fill_opacity = 0.8, fill_color = MAROON_C)
        aba_copy.scale(0.4)
        aab_copy = Prism([b3dabs, a3dabs, a3dabs], fill_opacity = 0.8, fill_color = MAROON_C)
        aab_copy.scale(0.4)
        baa_copy = baa.copy()
        baa_copy.scale(0.4)
        bba_copy = Prism([b3dabs, a3dabs, b3dabs], fill_opacity = 0.8, fill_color = PURPLE_C)
        bba_copy.scale(0.4)
        bab_copy = bab.copy()
        bab_copy.scale(0.4)
        abb_copy = Prism([b3dabs, a3dabs, b3dabs], fill_opacity = 0.8, fill_color = PURPLE_C)
        abb_copy.scale(0.4)
        plus3 = MathTex("+")
        plus3.rotate(-90*DEGREES, UP)
        plus4 = MathTex("+")
        plus4.rotate(-90*DEGREES, UP)
        plus5 = MathTex("+")
        plus5.rotate(-90*DEGREES, UP)
        
        a2b_group = VGroup(aba_copy, aab_copy, baa_copy)
        a2b_group.arrange(UP+IN, buff=-0.5)
        ab2_group = VGroup(abb_copy, bba_copy, bab_copy)
        ab2_group.arrange(UP+IN, buff=-0.2)
        bba_copy.shift(DOWN*0.5)
        bab_copy.shift(DOWN*0.5)
        
        equation_group = VGroup(acubed_copy, plus3, a2b_group, plus4, ab2_group, plus5, bcubed_copy)
        equation_group.arrange(UP, buff=0.3)
        equation_group.move_to([0, 3, 1])
        self.play(Create(equation_group))
        
        # So, we get this equation:
        aplusbcubed = MathTex(
                     r"=", 
                     r"a", r"^3",
                     r"+", 
                     r"3", r"a", r"^2", r"b",
                     r"+",
                     r"3", r"a", r"b", r"^2", 
                     r"+",
                     r"b", r"^3"
                    )
        aplusbcubed.set_color_by_tex("a",RED_C)
        aplusbcubed.set_color_by_tex("b",BLUE_C)
        aplusbcubed.next_to(plus4, IN, buff=1)
        aplusbcubed.rotate(90*DEGREES, UP)
        aplusbcubed.rotate(90*DEGREES, RIGHT)
        self.play(Write(aplusbcubed))
        
        aplusbcubedfull = MathTex(
            r"\therefore",
            r"(", r"a", r"+", r"b", r")", r"^", r"3",
            r"=",
            r"a", r"^", r"3",
            r"+", 
            r"3", r"a", r"^", r"2", r"b",
            r"+",
            r"3", r"a", r"b", r"^", r"2", 
            r"+",
            r"b", r"^", r"3"
        )
        aplusbcubedfull.next_to(aplusbcubed, IN, buff=2)
        aplusbcubedfull.rotate(90*DEGREES, UP)
        aplusbcubedfull.rotate(90*DEGREES, RIGHT)
        self.play(Write(aplusbcubedfull))
        
        
        # These are the binomial expansions for (a+b)2 and (a+b)3. They are quite neat, and relatively easy to visualise. 
        self.play(FadeOut(cuaxes), FadeOut(labels2), FadeOut(y5a), FadeOut(y6b), FadeOut(z5a), FadeOut(z6b),  FadeOut(x5a), FadeOut(x6b), FadeOut(acubed), FadeOut(bcubed), FadeOut(aba), FadeOut(aab), FadeOut(baa), FadeOut(bba), FadeOut(bab), FadeOut(abb))
        
        x7grp_copy = x7grp.copy()
        y7grp_copy = y7grp.copy()
        times3 = MathTex(r"\times")
        times3.rotate(-90*DEGREES, UP)
        equals3 = MathTex("=")
        equals3.rotate(-90*DEGREES, UP)
        equals3.rotate(90*DEGREES, RIGHT)
        rhsfinaleq = MathTex(r"(", r"a", r"+", r"b", r")", r"^", r"2")
        rhsfinaleq.set_color_by_tex("a", RED_C)
        rhsfinaleq.set_color_by_tex("b", BLUE_C)
        rhsfinaleq.rotate(90*DEGREES, UP)
        rhsfinaleq.rotate(90*DEGREES, RIGHT)
        
        x7grp_copy.scale(0.5)
        y7grp_copy.scale(0.5)
        
        aplusbsq = VGroup(x7grp_copy, times3, y7grp_copy, equals3, rhsfinaleq)
        aplusbsq.arrange(UP, buff=0.4)
        aplusbsq.move_to([0, -4, 3])
        self.play(Create(aplusbsq))
       
        
        a2_newcopy = square.copy()
        a2_newcopy.rotate(90*DEGREES, UP)
        b2_newcopy = b2_square.copy()
        b2_newcopy.rotate(90*DEGREES, UP)
        ab_1_newcopy = ab_rect_2.copy()
        ab_1_newcopy.rotate(90*DEGREES, UP)
        ab_2_newcopy = ab_rect_2.copy()
        ab_2_newcopy.rotate(90*DEGREES, UP)
        a2_newcopy.scale(0.3)
        b2_newcopy.scale(0.3)
        ab_1_newcopy.scale(0.3)
        ab_2_newcopy.scale(0.3)
        
        ab_grp = VGroup(ab_1_newcopy, ab_2_newcopy)
        ab_grp.arrange(UP, buff=-0.2)
        
        plus6 = MathTex("+")
        plus6.rotate(-90*DEGREES, UP)
        plus7 = MathTex("+")
        plus7.rotate(-90*DEGREES, UP)
    
        
        twoD_eq = VGroup(a2_newcopy, plus6, ab_grp, plus7, b2_newcopy)
        twoD_eq.arrange(UP, buff=0.4)
        twoD_eq.move_to([0, -3, 1])
        
        rhsfinaleq4 = MathTex(r"=",
            r"a", r"^", r"2",
            r"+", 
            r"2", r"a", r"b",
            r"+",
            r"b", r"^", r"2")
        rhsfinaleq4.set_color_by_tex("a", RED_C)
        rhsfinaleq4.set_color_by_tex("b", BLUE_C)
        rhsfinaleq4.next_to(a2_newcopy, IN, buff=1)
        rhsfinaleq4.rotate(90*DEGREES, UP)
        rhsfinaleq4.rotate(90*DEGREES, RIGHT)
        
        self.play(Create(twoD_eq), Write(rhsfinaleq4))
        
        aplusbsquaredfull = MathTex(
            r"\therefore",
            r"(", r"a", r"+", r"b", r")", r"^", r"2",
            r"=",
            r"a", r"^", r"2",
            r"+", 
            r"2", r"a", r"b",
            r"+",
            r"b", r"^", r"2"
        )
        aplusbsquaredfull.set_color_by_tex("a", RED_C)
        aplusbsquaredfull.set_color_by_tex("b", BLUE_C)
        aplusbsquaredfull.next_to(rhsfinaleq4, IN, buff=2)
        aplusbsquaredfull.rotate(90*DEGREES, UP)
        aplusbsquaredfull.rotate(90*DEGREES, RIGHT)
        self.play(Write(aplusbsquaredfull))
        
        self.wait(5)
        
        # But what about the expansion for (a+b)4? We’d have to visualise it using the 4-dimensional equivalent of a cube: a 4-dimensional hypercube, or, a tesseract. But it’s not so easy to visualise and split up a tesseract, because we live in a 3 dimensional world. 
        # And it’s even harder to visualise 5 or 6 dimensional spaces, which we would need to visualise these expressions. 
        # So, let’s examine the geometry of 1, 2 and 3 dimensions more deeply, and search for patterns there that we can generalise to higher powers.
 

    
        

        
        
        
        
        
            
            
        
        
        
        
        
   
# manim -pql Binomial\ Theorem\ SoME\ Animations.py Basic  
'''
The z plane isn't in and out of the screen, i think. It's placed in the same way that the 3D coordinate system is placed. LIke with the x in and out, and the z up and down. 
'''