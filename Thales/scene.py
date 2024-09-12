from manim import *
import numpy as np

class Thales(Scene):
    def construct(self):
        theorem_tex = Tex(r"\textit{Thales' Theorem} - if $A,B$, and $C$ lie on \\a circle,"
                          r" with line $\overline{AC}$ as the diameter,\\ then $\angle ABC$"
                           r" is a right-angle.")
        self.add(theorem_tex)
        self.wait(4)
        self.play(Write(theorem_tex), rate_func=lambda t: smooth(1-t))
        circle = Circle(2.5).rotate_about_origin(PI/2).flip(UP).set_color(GREY)
        
        A = Dot(LEFT*2.5).set_color(BLUE).set_z_index(1)
        B = Dot(RIGHT*2.5).set_color(BLUE).set_z_index(1)
        A_tex = MathTex("A").next_to(A,LEFT)
        B_tex = MathTex("C").next_to(B,RIGHT)
        AB = Line(A.get_center(), B.get_center())
        d_label = MathTex("d").move_to(DOWN*0.5)
        self.play(Create(circle))
        self.play(GrowFromCenter(A),GrowFromCenter(B))
        self.play(Create(AB), FadeIn(A_tex,B_tex))
        self.play(FadeIn(d_label))
        self.wait(0.5)
        self.play(FadeOut(d_label))
        AB.add_updater(lambda x: x.become(Line(A.get_center(), B.get_center())))
        #self.add(AB,A_tex,B_tex)


        self.next_section()


        C = Dot(UP*2.5).set_color(BLUE).set_z_index(1)
        
        C_tex = MathTex("B").next_to(C,UP)
        AC = Line(A.get_center(), C.get_center())
        BC = Line(B.get_center(), C.get_center())
        triangle = Polygon(A.get_center(),
                           B.get_center(),
                           C.get_center())
        triangle.set_fill(BLUE,opacity=0.4).set_z_index(-1)
        triangle.set_sheen(0.4)
        
        self.play(GrowFromCenter(C))
        self.play(Create(AC),Create(BC), FadeIn(C_tex))
        self.play(FadeIn(triangle))

        AC.add_updater(lambda x: x.become(Line(A.get_center(), C.get_center())))
        BC.add_updater(lambda x: x.become(Line(B.get_center(), C.get_center())))
        C_tex.add_updater(lambda x: x.become(MathTex("B").next_to(C,UP)))
        triangle.add_updater(lambda x: x.become(Polygon(A.get_center(),
                           B.get_center(),
                           C.get_center()).set_fill(BLUE,opacity=0.4).set_z_index(-1).set_sheen(0.4)))
        self.add(triangle, AC, BC)
        #self.add(C_tex)
        ABC = Angle(line1=BC, line2=AB, radius=0.5, quadrant=(1,-1))
        BCA = Angle(line1=AC, line2=BC, radius=0.5, quadrant=(-1,-1))
        CAB = Angle(line1=AB, line2=AC, radius=0.5, quadrant=(1,1))
       

        self.next_section()
        
        self.play(Create(ABC), Create(BCA), Create(CAB))
        
        ABC.add_updater(lambda x: x.become(Angle(line1=BC,
                                                  line2=AB,
                                                    radius=0.5,
                                                      quadrant=(1,-1))))
        BCA.add_updater(lambda x: x.become(Angle(line1=AC,
                                                  line2=BC,
                                                    radius=0.5,
                                                      quadrant=(-1,-1))))
        CAB.add_updater(lambda x: x.become(Angle(line1=AB,
                                                  line2=AC,
                                                    radius=0.5,
                                                      quadrant=(1,1))))

        self.add(ABC,BCA,CAB)

        self.next_section()
        self.play(MoveAlongPath(C,
                                path=Arc(radius=2.5,
                                         start_angle=PI/2,
                                         angle=-PI/5)),
                                         run_time=2,
                                         rate_func=smooth)
        self.play(MoveAlongPath(C,
                                path=Arc(radius=2.5,
                                         start_angle=3*PI/10,
                                         angle=11*PI/30)),
                                         run_time=2,
                                         rate_func=smooth)
        self.wait()

        self.next_section()

        
        ABC.clear_updaters()
        BCA.clear_updaters()
        CAB.clear_updaters()
        

        q = MathTex(r"?").move_to(DOWN)
        attempt = Tex(r"Pause to try for yourself").to_edge(DOWN)
        sum_tex_r = MathTex("1","8",r"0^\circ").move_to(triangle.get_center_of_mass())
        sum_tex_l = MathTex(r"2",r"\alpha","+","2",r"\beta"," = ")
        temp_angle = BCA.copy()
        O = Dot(ORIGIN).set_color(BLUE).set_z_index(1)

        AO_y = Line(A,ORIGIN).set_color(YELLOW)
        BO_y = Line(B,ORIGIN).set_color(YELLOW)
        CO_y = Line(C, ORIGIN).set_color(YELLOW)

        copy1 = CO_y.copy()
        copy2 = CO_y.copy()
        copy3 = AO_y.copy()
        copy4 = BO_y.copy()

        CO = Line(C, ORIGIN)

        Ar_label = MathTex("r").next_to(AO_y,DOWN)
        Br_label = MathTex("r").next_to(BO_y,DOWN)
        Cr_label = MathTex("r").next_to(CO_y.get_center(),LEFT)

        OCA = Angle(line1=AC,
                    line2=CO,
                    quadrant=(-1,1),
                    radius=0.5)
        OCB = Angle(line1=CO, 
                    line2=BC, 
                    quadrant=(1,-1),
                    radius=0.5)


        avgr = VGroup(CAB.copy(),BCA.copy(),ABC.copy())
        avgr2 = VGroup(copy1,copy2,copy3,copy4)

        self.play(temp_angle.animate.become(q)) 
        self.wait()
        self.play(FadeOut(temp_angle))
        self.play(Write(attempt), rate_func=smooth)
        self.wait()
        self.play(Write(attempt), rate_func=lambda t: smooth(1-t))
        self.play(Transform(avgr, sum_tex_r))
        self.wait(0.5)
        self.play(avgr.animate.move_to(ORIGIN).to_edge(DOWN))
        self.wait()
        self.play(Create(CO),GrowFromCenter(O))
        self.wait()
        self.play(FadeIn(AO_y,BO_y,CO_y,Ar_label,Br_label,Cr_label))
        self.wait()


        self.next_section()


        alpha1 = MathTex(r"\alpha").move_to(
            Angle(line1=AC,
                    line2=CO,
                    quadrant=(-1,1),
                    radius=0.5+3*SMALL_BUFF).point_from_proportion(0.5)
        )
        alpha2 = MathTex(r"\alpha").move_to(
            Angle(line1=AB, 
                  line2=AC, 
                  radius=0.5+3*SMALL_BUFF, 
                  quadrant=(1,1)).point_from_proportion(0.5)
        )
        beta1 = MathTex(r"\beta").move_to(
            Angle(line1=CO,
                    line2=BC,
                    quadrant=(1,-1),
                    radius=0.5+8*SMALL_BUFF).point_from_proportion(0.5)
        )
        beta2 = MathTex(r"\beta").move_to(
            Angle(line1=BC, 
                        line2=AB, 
                        radius=0.5+8*SMALL_BUFF, 
                        quadrant=(1,-1)).point_from_proportion(0.5)
        )
        self.play(copy1.animate.become(beta1),
                  copy2.animate.become(alpha1),
                  copy3.animate.become(alpha2),
                  copy4.animate.become(beta2))
        self.wait()
        self.play(FadeOut(AO_y,BO_y,CO_y,Ar_label,Br_label,Cr_label))
        self.wait()

        tex_vgr = VGroup(sum_tex_l,
                         sum_tex_r).arrange(RIGHT).move_to(ORIGIN).to_edge(DOWN)
        
        self.play(ReplacementTransform(avgr2.copy(), sum_tex_l), avgr.animate.move_to(sum_tex_r.get_center()))
        self.wait(2)

        final_tex_l = MathTex(r"\alpha","+",r"\beta","=").next_to(sum_tex_r,LEFT)
        final_tex_r = MathTex("9",r"0^\circ").next_to(sum_tex_l,RIGHT)
        BCA_y = Angle(line1=AC, line2=BC, radius=0.5, quadrant=(-1,-1)).set_color(YELLOW).set_z_index(2)


        self.remove(avgr)
        self.play(TransformMatchingTex(sum_tex_l,final_tex_l),
                    TransformMatchingTex(sum_tex_r,final_tex_r))
        
        self.wait()


        self.next_section()
        

        self.play(Circumscribe(final_tex_l[:-1],run_time=2.5),Create(BCA_y,run_time=2))
        self.play(FadeOut(BCA_y,CO,BCA,O,avgr2,final_tex_r,final_tex_l))

        BCA = RightAngle(line1=AC, line2=BC, length=0.4,quadrant=(-1,-1))
        self.play(Create(BCA))
        self.wait()

        ABC.add_updater(lambda x: x.become(Angle(line1=BC,
                                                  line2=AB,
                                                    radius=0.5,
                                                      quadrant=(1,-1))))
        BCA.add_updater(lambda x: x.become(RightAngle(line1=AC,
                                                       line2=BC, 
                                                       length=0.4,
                                                       quadrant=(-1,-1))))
        CAB.add_updater(lambda x: x.become(Angle(line1=AB,
                                                  line2=AC,
                                                    radius=0.5,
                                                      quadrant=(1,1))))
        self.play(MoveAlongPath(C,
                                path=Arc(radius=2.5,
                                         start_angle=2*PI/3,
                                         angle=-11*PI/30)),
                                         run_time=2,
                                         rate_func=smooth)
        self.play(MoveAlongPath(C,
                                path=Arc(radius=2.5,
                                         start_angle=3*PI/10,
                                         angle=PI/5)),
                                         run_time=2,
                                         rate_func=smooth)
        self.wait()
        for mob in self.mobjects:
            mob.clear_updaters()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        theorem_tex = Tex(r"\textit{Thales' Theorem} - if $A,B$, and $C$ lie on \\a circle,"
                          r" with line $\overline{AC}$ as the diameter,\\ then $\angle ABC$"
                           r" is a right-angle.")
        self.play(Write(theorem_tex),rate_func=smooth)