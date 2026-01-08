from vectors import*

from manim import*
from myutils import*

class test(Scene):
    def construct(self):

        
        p = Dot().move_to([-1,0,0])
        n = Dot().move_to([1,0,0])

        
        k = 1
        
        

        

        q_p = +1
        q_n = -1
        step_size = 0.05

        def draw_field_line(start, p,n,steps):
            points = [start]

            for i in range(steps):

                r1 = dist(start[0], p.get_center()[0], start[1], p.get_center()[1])
                r2 = dist(start[0], n.get_center()[0], start[1], n.get_center()[1])

                O = mVector(*start)
                P = mVector(*p.get_center())
                N = mVector(*n.get_center())

                E1 = (O - P) * (k * q_p / r1**3)
                E2 = (O - N) * (k * q_n / r2**3)

                R = E1 + E2
                R_hat = R.normalize()

                new_p = [
                    start[0] + step_size * R_hat.x_comp,
                    start[1] + step_size * R_hat.y_comp,
                    0
                ]

                start = new_p
                points.append(new_p)

                if r2 < 0.1:
                    break

            return points

        
        starts = []
        g = VGroup()
        field_points = []

        for i in range(20):
            x = -1 + 0.01*m.cos(i*2*PI/20)
            y = 0.01*m.sin(i*2*PI/20)
            starts.append([x,y,0])
        

        
        for i in starts:
            x =draw_field_line(i,p,n,1000)
            g.add(VMobject(stroke_width=1, stroke_color=TEAL))
            field_points.append(x)
        for i in range(20):
            g[i].set_points_as_corners(field_points[i])
        
        p,n = Dot().move_to([-1,0,0]), Dot().move_to([1,0,0])
        glow1, glow2 = create_glow(p, ocity=1,color=RED),create_glow(n, ocity=1,color=BLUE)
        self.add(p,n,glow1, glow2)
        self.play(Create(g, lag_ratio=0.2), run_time=4)

        

        self.wait()

        p1 = Dot()

        
        






