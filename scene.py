from manim import *

temp = TexTemplate()
temp.add_to_preamble(r"""
\renewcommand{\vec}[1]{\boldsymbol{\mathbf{#1}}}
\newcommand{\cross}{\times}
\newcommand{\grad}{\nabla}
\newcommand{\dive}{\grad\cdot}
\newcommand{\curl}{\grad\cross}
\newcommand{\hodge}{{\star}}
""")

epigraph = TexTemplate()
epigraph.add_to_preamble(r"\usepackage{epigraph}")

class Maff(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(
                tex_template=temp, 
                tex_to_color_map={
                    r"0": GRAY,

                    r"_t": YELLOW,
                    r"_x": YELLOW,
                    r"_y": YELLOW,
                    r"_z": YELLOW,
                    r"^t": YELLOW,
                    r"^x": YELLOW,
                    r"^y": YELLOW,
                    r"^z": YELLOW,
                    r"\,t": YELLOW,
                    r"\,x": YELLOW,
                    r"\,y": YELLOW,
                    r"\,z": YELLOW,
                    r"^{tt}": YELLOW,
                    r"^{tx}": YELLOW,
                    r"^{ty}": YELLOW,
                    r"^{tz}": YELLOW,
                    r"^{xt}": YELLOW,
                    r"^{xx}": YELLOW,
                    r"^{xy}": YELLOW,
                    r"^{xz}": YELLOW,
                    r"^{yt}": YELLOW,
                    r"^{yx}": YELLOW,
                    r"^{yy}": YELLOW,
                    r"^{yz}": YELLOW,
                    r"^{zt}": YELLOW,
                    r"^{zx}": YELLOW,
                    r"^{zy}": YELLOW,
                    r"^{zz}": YELLOW,

                    r"\mu": GOLD,
                    r"\nu": GOLD,
                    r"\rho": GOLD,
                    r"\sigma": GOLD,

                    r"\phi": GREEN,
                    r"\lambda": GREEN,
                    r"F": GREEN,
                    r"\vec A": GREEN,
                    r"A": GREEN,
                    r"\vec J": GREEN,
                    r"J": GREEN,

                    r"G": PURPLE,

                    r"\vec E": BLUE,
                    r"\vec B": PINK,
                },
                *args, **kwargs)

class Trix(Matrix):
    def __init__(self, *args, **kwargs):
        super().__init__(
                left_bracket="(", 
                right_bracket=")", 
                element_to_mobject=Maff, 
                *args, **kwargs)

class S00_Title(Scene):
    def construct(self):
        quote = Tex(r"""
\setlength\epigraphwidth{.3\textwidth}
\epigraph{
Gauge symmetry is, in many ways, an odd foundation on which
to build our best theories of physics. It is not a property
of Nature, but rather a property of how we choose to describe
Nature. Gauge symmetry is, at heart, a redundancy in our
description of the world. Yet it is a redundancy that has
enormous utility, and brings a subtlety and richness
to those theories that enjoy it.
}{}
                """, color=PURPLE, font_size=24, tex_template=epigraph).shift(RIGHT*4 + UP)
        tong = Tex(r"\textit{David Tong}", color=PURPLE, font_size=18).next_to(quote, DOWN).shift(UP*0.2)

        title = Tex(r"A Sketch of Gauge Theory", font_size=80, tex_template=temp)
        subtitle = Tex(r"From Maxwell's Equations to Modern Particle Physics", color=PURPLE, font_size=42, tex_template=temp).next_to(title, DOWN)

        self.play(FadeIn(quote, run_time = 3))
        self.wait(4)
        self.play(FadeIn(tong, run_time = 0.5))
        self.wait(3)
        self.play(FadeOut(quote, run_time = 1), FadeOut(tong, run_time=2), Write(title))
        self.wait()
        self.play(Write(subtitle))
        self.wait()

        self.next_section()
        self.clear()

class S01_Notation(Scene):
    def construct(self):
        notation_h = Tex(r"Notation", color=PURPLE).shift(UP+UP+UP)

        scalars = VGroup(
                Tex("Scalar fields: "), 
                Maff(r"\phi, \lambda"),
        ).arrange(RIGHT)
        vectors = VGroup(
                Tex("3-vector fields: "),
                Maff(r"\vec E, \vec B, \vec A \equiv"),
                Trix([[r"\vec A_x"], [r"\vec A_y"], [r"\vec A_z"]])
        ).arrange(RIGHT)
        VGroup(scalars, vectors).arrange(direction=DOWN, buff=0.2)

        partials = VGroup(
                Tex("Partial derivatives: "),
                Maff(r"\partial_t \equiv \frac{\partial}{\partial t}")
        ).arrange(RIGHT)
        gradient = VGroup(
                Tex("Gradient: "),
                Maff(r"\grad \equiv"), 
                Trix([[r"\partial_x"], [r"\partial_y"], [r"\partial_z"]])
        ).arrange(RIGHT)
        VGroup(partials, gradient).arrange(direction=DOWN, buff=0.2)

        fourvectors = VGroup(
                Tex("4-vector fields: "),
                Maff(r"J^\mu, A^\nu \equiv"), 
                Trix([[r"A^t"], [r"A^x"], [r"A^y"], [r"A^z"]])
        ).arrange(RIGHT)
        covariant = VGroup(
                Tex("Spacetime derivative: "),
                Maff(r"\partial_\mu \equiv"), 
                Trix([[r"\partial_t"], [r"\partial_x"], [r"\partial_y"], [r"\partial_z"]])
        ).arrange(RIGHT)
        VGroup(fourvectors, covariant).arrange(direction=DOWN, buff=0.2)

        tensors = VGroup(Tex("Tensor fields: "), Trix([
            ["G^{tt}", "G^{tx}", "G^{ty}", "G^{tz}"],
            ["G^{xt}", "G^{xx}", "G^{xy}", "G^{xz}"],
            ["G^{yt}", "G^{yx}", "G^{yy}", "G^{yz}"],
            ["G^{zt}", "G^{zx}", "G^{zy}", "G^{zz}"],
            ])).arrange(RIGHT)
        self.play(Write(notation_h))
        self.wait()

        self.play(Write(scalars))
        self.wait()
        self.play(Write(vectors))
        self.wait()

        self.clear()
        self.add(notation_h)

        self.play(Write(partials))
        self.wait()
        self.play(Write(gradient))
        self.wait()

        self.clear()
        self.add(notation_h)

        self.play(Write(fourvectors))
        self.wait()
        self.play(Write(covariant))
        self.wait()

        self.clear()
        self.add(notation_h)

        self.play(Write(tensors))
        self.wait()

class S02_Maxwells(Scene):
    def construct(self):
        maxwells = Maff(r"""
            \dive\vec E &= \rho \\ 
            \curl\vec B - \partial_t\vec E &= \vec J \\
            \dive\vec B &= 0 \\
            \curl\vec E + \partial_t\vec B &= 0 \\
        """)
        maxwells_h = Tex(r"Maxwell's equations of electrodynamics", color=PURPLE).next_to(maxwells, UP)
        simplify_h = Tex(r"We can simplify this!", color=PURPLE).next_to(maxwells, DOWN)
        self.play(Write(maxwells_h))
        self.wait()
        self.play(Write(maxwells))
        self.wait()
        self.play(Write(simplify_h))
        self.wait()

class S03_Simplify(Scene):
    def construct(self):
        identity_h = VGroup(Tex(r"For any", color=PURPLE), Maff(r"\phi, \vec A")).arrange(RIGHT)
        identity = Maff(r"""
            \curl(\grad\phi) &= 0\\
            \dive(\curl\vec A) &= 0
        """)
        electrostat_h = Tex(r"In electrostatics", color=PURPLE)
        electrostat = Maff(r"""
            \curl\vec E &= 0\\
            \implies \vec E &\equiv -\grad\phi\\
        """)
        question = Tex(r"Is there something similar for electrodynamics?", color=PURPLE)
        VGroup(identity_h, identity, electrostat_h, electrostat, question).arrange(DOWN)

        self.play(Write(identity_h))
        self.wait()
        self.play(Write(identity))
        self.wait()
        self.play(Write(electrostat_h))
        self.wait()
        self.play(Write(electrostat))
        self.wait()
        self.play(Write(question))
        self.wait()
        self.wait()

class S04_Potentials(Scene):
    def construct(self):
        phi = Maff(r"""
            \dive\vec B &= 0\\
            \vec B &\equiv \curl\vec A
        """)
        a = Maff(r"""
            \curl\vec E &= -\partial_t\vec B = -\partial_t\curl\vec A\\
            \vec E &\equiv -\grad\phi - \partial_t\vec A\\
        """)
        potentials = VGroup(phi, a).arrange(RIGHT, buff=2)
        potentials_h = Tex(r"In electrodynamics", color=PURPLE).next_to(potentials, UP)
        self.play(Write(potentials_h))
        self.wait()
        self.play(Write(phi))
        self.wait()
        self.play(Write(a))
        self.wait()

        self.play(FadeOut(potentials_h), potentials.animate.shift(UP+UP+UP).scale(0.8))

        maxwells_h = Tex(r"Maxwell's equations in potential form")
        maxwells = [
            (
                Maff(r"\dive\vec E = \rho"),
                Maff(r"\curl\vec B - \partial_t\vec E = \vec J"),
                Maff(r"\dive\vec B = 0"),
                Maff(r"\curl\vec E + \partial_t\vec B = 0"),
            ),
            (
                Maff(r"\dive(-\grad\phi - \partial_t\vec A) = \rho"),
                Maff(r"\curl(\curl\vec A) - \partial_t(-\grad\phi - \partial_t\vec A) = \vec J"),
                Maff(r"\dive(\curl\vec A) = 0"),
                Maff(r"\curl(-\grad\phi - \partial_t\vec A) + \partial_t(\curl\vec A) = 0"),
            ),
            (
                Maff(r"-\dive(\grad\phi) - \dive(\partial_t\vec A) = \rho"),
                Maff(r"\curl(\curl\vec A) + \partial_t(\grad\phi) + \partial_t^2\vec A = \vec J"),
                Maff(r"0 = 0"),
                Maff(r"0 = 0")
            ),
            (
                Maff(r"-\Delta\phi - \partial_t(\dive\vec A) = \rho"),
                Maff(r"\grad(\dive\vec A) - \Delta\vec A + \partial_t(\grad\phi) - \partial_t^2\vec A = \vec J"),
                Maff(r"0 = 0"),
                Maff(r"0 = 0")
            ),
        ]

        maxwells_h.shift(UP)
        self.play(Write(maxwells_h))
        self.wait()

        for (i, el) in enumerate(maxwells):
            VGroup(*el).arrange(DOWN).shift(RIGHT+RIGHT).shift(DOWN)
            for (j, eq) in enumerate(el):
                eq.align_to(maxwells[0][0], RIGHT)
                if i == 0:
                    self.play(Write(eq))
                else: 
                    eq.align_to(maxwells[0][j], UP)
                    self.play(TransformMatchingShapes(maxwells[i-1][j], eq))
            self.wait()

class S05_4Potential(Scene):
    def construct(self):
        fourpotential = VGroup(Maff(r"A^\mu\equiv"), Trix([ [r"\phi"], [], [r"\vec A"], [] ])).arrange(RIGHT)
        fourpotentialexpanded = VGroup(Maff(r"A^\mu\equiv"), Trix([ [r"\phi"], [r"\vec A_x"], [r"\vec A_y"], [r"\vec A_z"] ])).arrange(RIGHT)
        fourpotential_h = Tex(r"Scalar + vector = 4-vector?", color=PURPLE).next_to(fourpotentialexpanded, UP)
        self.play(Write(fourpotential_h))
        self.wait()
        self.play(Write(fourpotential))
        self.wait()
        self.play(ReplacementTransform(fourpotential, fourpotentialexpanded))
        self.wait()

class S06_Tensor(Scene):
    def construct(self):
        emtensor = Maff(r"F^{\mu\nu}\equiv\partial^u A^\nu - \partial^\nu A^\mu")
        emtensor_h = Tex(r"Electromagnetic field tensor", color=PURPLE)
        emeq = Maff(r"=")
        em = [
            (
                Trix([
                    [ r"\cdot" , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\cdot" , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\cdot" , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\cdot" , r"\cdot" , r"\cdot" , r"\cdot" ],
                ]),
                Tex("")
            ),
            (
                Trix([
                    [ 0 , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\cdot" , 0 , r"\cdot" , r"\cdot" ],
                    [ r"\cdot" , r"\cdot" , 0 , r"\cdot" ],
                    [ r"\cdot" , r"\cdot" , r"\cdot", 0 ],
                ]),
                Tex(r"Diagonal entries cancel")
            ),
            (
                Trix([
                    [ 0 , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"-\partial_t \vec A_x - \partial_x\phi" , 0, r"\cdot" , r"\cdot" ],
                    [ r"-\partial_t \vec A_y - \partial_y\phi" , r"\cdot" , 0 , r"\cdot" ],
                    [ r"-\partial_t \vec A_z - \partial_z\phi" , r"\cdot" , r"\cdot" , 0 ],
                ], h_buff = 2),
                Maff(r"A^t = \phi")
            ),
            (
                Trix([
                    [ 0 , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\vec E_x" , 0, r"\cdot" , r"\cdot" ],
                    [ r"\vec E_y" , r"\cdot" , 0 , r"\cdot" ],
                    [ r"\vec E_z" , r"\cdot" , r"\cdot" , 0 ],
                ]),
                Maff(r"\vec E = -\partial_t\vec A - \grad\phi")
            ),
            (
                Trix([
                    [ 0 , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\vec E_x" , 0, r"\cdot" , r"\cdot" ],
                    [ r"\vec E_y" , r"\partial_x \vec A_y - \partial_y \vec A_x" , 0 , r"\cdot" ],
                    [ r"\vec E_z" , r"\partial_x \vec A_z - \partial_z \vec A_x" , r"\partial_y \vec A_z - \partial_z \vec A_y" , 0 ],
                ], h_buff = 4),
                Maff(r"A^x = \vec A_x,\, A^y = \vec A_y, A^z = \vec A_z")
            ),
            (
                Trix([
                    [ 0 , r"\cdot" , r"\cdot" , r"\cdot" ],
                    [ r"\vec E_x" , 0, r"\cdot" , r"\cdot" ],
                    [ r"\vec E_y" , r"\vec B_z" , 0 , r"\cdot" ],
                    [ r"\vec E_z" , r"-\vec B_y" , r"\vec B_x" , 0 ],
                ]),
                Maff(r"\vec B = \grad\cross\vec A")
            ),
            (
                Trix([
                    [ 0 , r"-\vec E_x" , r"-\vec E_y" , r"-\vec E_z" ],
                    [ r"\vec E_x" , 0, r"-\vec B_z" , r"\vec B_y" ],
                    [ r"\vec E_y" , r"\vec B_z" , 0 , r"-\vec B_x" ],
                    [ r"\vec E_z" , r"-\vec B_y" , r"\vec B_x" , 0 ],
                ]),
                Maff(r"(F^T)^{\mu\nu} = F^{\nu\mu} = \partial_\nu A^\mu - \partial_\mu A^\nu = -F^{\mu\nu}")
            )
        ]
        emtensor.next_to(em[0][0], UP)
        emeq.next_to(em[0][0], LEFT)
        emtensor_h.next_to(emtensor, UP)
        em[0][1].next_to(em[0][0], DOWN)
        self.play(Write(emtensor_h))
        self.wait()
        self.play(Write(emtensor))
        self.wait()
        self.play(Write(emeq))
        self.play(Write(em[0][0]))
        self.play(Write(em[0][1]))

        for (i, el) in enumerate(em[1:]):
            el[1].next_to(em[0][0], DOWN)
            self.play(FadeOut(em[i][1]))
            self.play(FadeIn(el[1]))
            self.wait()
            self.play(
                emeq.animate.next_to(el[0], LEFT),
                ReplacementTransform(em[i][0], el[0])
            )
            self.wait()

class S08_Deriv(Scene):
    def construct(self):
        dem1 = Trix([
            [ r"\partial_\mu F^{\mu\,t}"],
            [ r"\partial_\mu F^{\mu\,x}"],
            [ r"\partial_\mu F^{\mu\,y}"],
            [ r"\partial_\mu F^{\mu\,z}"],
        ])
        demeq = Maff(r"=").next_to(dem1, LEFT)
        demtensor = Maff(r"\partial_\mu F^{\mu\nu}").next_to(demeq, LEFT)
        dem2 = Trix([
            [ r"0 + \partial_x \vec E_x + \partial_y \vec E_y + \partial_z \vec E_z" ],
            [ r"-\partial_t \vec E_x + 0 - \partial_y \vec B_z + \partial_z \vec B_y" ],
            [ r"-\partial_t \vec E_y + \partial_x \vec B_z + 0 - \partial_z \vec B_x" ],
            [ r"-\partial_t \vec E_z - \partial_x \vec B_y + \partial_y \vec B_x + 0" ],
        ]).next_to(demeq, RIGHT)
        dem3 = Trix([
            [ r"\dive\vec E" ],
            [],
            [ r"-\partial_t\vec E + \grad\cross\vec B" ],
            [],
        ]).next_to(demeq, RIGHT).next_to(demeq, RIGHT)
        current1 = Trix([
            [ r"\rho" ],
            [],
            [ r"\vec J" ],
            [],
        ]).next_to(demeq, LEFT)
        current2 = Maff(r"J^\mu").next_to(demeq, LEFT)
        demtensor_h = Tex(r"Maxwell's equation in covariant form", color=PURPLE).next_to(dem1, UP)
        whatabout = VGroup(
                Tex(r"What about ", color=PURPLE),
                Maff(r"\dive\vec B = 0"),
                Tex(r" and ", color=PURPLE),
                Maff(r"\curl\vec E + \partial_t\vec B = 0"),
                Tex(r"?")
        ).arrange(RIGHT).next_to(dem1, DOWN)
        self.play(Write(demtensor_h))
        self.wait()
        self.play(Write(demtensor))
        self.play(Write(demeq))
        self.play(Write(dem1))
        self.wait()
        self.play(TransformMatchingShapes(dem1, dem2))
        self.wait()
        self.play(TransformMatchingShapes(dem2, dem3))
        self.wait()
        self.play(TransformMatchingShapes(demtensor, current1))
        self.wait()
        self.play(ReplacementTransform(current1, current2))
        self.wait()
        self.play(Write(whatabout))
        self.wait()
        self.wait()


class S09_Hodge(Scene):
    def construct(self):
        hodge_h = Tex(r"Hodge dual", color=PURPLE)
        hodge_phi = Maff(r"\hodge\phi = \vec A,\,\,")
        hodge_a = Maff(r"\hodge\vec A = \phi")
        hem_tensor = Maff(r"\hodge F^{\mu\nu}")
        hem_partial = Maff(r"\partial_\mu")
        hem_equiv = Maff(r"\equiv \hodge")
        hem_equal = Maff(r"=")
        hem_em = Trix([
            [ 0 , r"-\vec E_x" , r"-\vec E_y" , r"-\vec E_z" ],
            [ r"\vec E_x" , 0, r"-\vec B_z" , r"\vec B_y" ],
            [ r"\vec E_y" , r"\vec B_z" , 0 , r"-\vec B_x" ],
            [ r"\vec E_z" , r"-\vec B_y" , r"\vec B_x" , 0 ],
        ])
        hem_hem = Trix([
            [ 0 , r"-\vec B_x" , r"-\vec B_y" , r"-\vec B_z" ],
            [ r"\vec B_x" , 0, r"\vec E_z" , r"-\vec E_y" ],
            [ r"\vec B_y" , r"-\vec E_z" , 0 , r"\vec E_x" ],
            [ r"\vec B_z" , r"\vec E_y" , r"-\vec E_x" , 0 ],
        ])
        hem_dem = Trix([
            [ r"0 + \partial_x \vec B_x + \partial_y \vec B_y + \partial_z \vec B_z" ],
            [ r"\partial_t \vec B_x + 0 + \partial_y \vec E_z - \partial_z \vec E_y" ],
            [ r"\partial_t \vec B_y - \partial_x \vec E_z + 0 + \partial_z \vec E_x" ],
            [ r"\partial_t \vec B_z + \partial_x \vec E_y - \partial_y \vec E_x + 0" ],
        ])
        hem_dem_done = Trix([
            [ r"\dive\vec B" ],
            [ ],
            [ r"\partial_t \vec B_t +\curl\vec E" ],
            [ ]
        ])
        hem_zero = Maff("0")

        hem_equal.next_to(hem_dem_done, LEFT)
        hem_equiv.align_to(hem_equal, LEFT)
        hem_tensor.next_to(hem_equiv, LEFT)
        hem_zero.next_to(hem_equiv, LEFT)
        hem_partial.next_to(hem_tensor, LEFT).shift(RIGHT*0.2 + DOWN*0.1)
        hem_em.next_to(hem_equiv, RIGHT)
        hem_hem.next_to(hem_equal, RIGHT)
        hem_dem.next_to(hem_equal, RIGHT)
        hem_dem_done.next_to(hem_equal, RIGHT)

        hodge_phi.next_to(hem_dem_done, UP).shift(UP)
        hodge_h.next_to(hodge_phi, UP)
        hodge_phi.shift(LEFT)
        hodge_a.next_to(hodge_phi, RIGHT)

        self.play(Write(hodge_h))
        self.wait()
        self.play(Write(hodge_phi))
        self.wait()
        self.play(Write(hodge_a))
        self.wait()
        self.play(Write(hem_tensor))
        self.play(Write(hem_equiv))
        self.play(Write(hem_em))
        self.wait()
        self.play(ReplacementTransform(hem_equiv, hem_equal), TransformMatchingShapes(hem_em, hem_hem))
        self.wait()
        self.play(Write(hem_partial), TransformMatchingShapes(hem_hem, hem_dem))
        self.wait()
        self.play(TransformMatchingShapes(hem_dem, hem_dem_done))
        self.wait()
        self.play(ReplacementTransform(VGroup(hem_partial, hem_tensor), hem_zero))
        self.wait()

class S10_Maxtense(Scene):
    def construct(self):
        maxwells = Tex(r"Maxwell's equation(s) in covariant form", color=PURPLE)
        equations = Maff(r"""
            \partial_\mu F^{\mu\nu} &= J^\nu\\
            \partial_\mu \hodge F^{\mu\nu} &= 0
        """)
        technicality = Maff(r"(F^{\mu\nu}\equiv\partial^u A^\nu - \partial^\nu A^\mu)")
        question = Tex(r"Is this the most concise model?")
        VGroup(maxwells, equations, technicality, question).arrange(DOWN)
        self.play(Write(maxwells))
        self.wait()
        self.play(Write(equations))
        self.wait()
        self.play(Write(technicality))
        self.wait()
        self.play(Write(question))
        self.wait()

class S11_Symmetry(Scene):
    def construct(self):
        symmetry_h = Tex(r"The potentials are not fully constrained!", color=PURPLE)
        change = Maff(r"""
            \vec A &\mapsto \vec A + \grad\lambda\\
            \phi &\mapsto \phi - \partial_t\lambda
        """)
        history = [
            (
                Maff(r"\vec B = \curl\vec A"),
                Maff(r"\vec E = -\grad\phi - \partial_t\vec A")
            ),
            (
                Maff(r"\vec B = \curl(\vec A + \grad\lambda)"),
                Maff(r"\vec E = -\grad(\phi - \partial_t\lambda) - \partial_t(\vec A + \grad\lambda)")
            ),
            (
                Maff(r"\vec B = \curl\vec A + \curl(\grad\lambda)"),
                Maff(r"\vec E = -\grad\phi - \partial_t\vec A + \grad\partial_t\lambda - \partial_t\grad\lambda")
            ),
            (
                Maff(r"\vec B = \curl\vec A + 0"),
                Maff(r"\vec E = -\grad\phi - \partial_t\vec A - 0")
            ),
            (
                Maff(r"\vec B = \curl\vec A"),
                Maff(r"\vec E = -\grad\phi - \partial_t\vec A")
            ),
        ]
        but = VGroup(
                Tex(r"Maxwell's equations are \textit{invariant} under a", color=PURPLE),
                VGroup(Tex("gauge transformation (global \textit{or} local) ", color=PURPLE), Maff(r"\lambda")).arrange(RIGHT)
            ).arrange(DOWN)
        symmetry_h.shift(UP+UP+UP)
        change.next_to(symmetry_h, DOWN)
        self.play(Write(symmetry_h))
        self.wait()
        for (i, el) in enumerate(history):
            VGroup(*el).arrange(DOWN).shift(LEFT+LEFT+LEFT)
            if i == 1:
                self.play(Write(change))
                self.wait()
            for (j, eq) in enumerate(el):
                eq.align_to(history[0][0], LEFT)
                if i == 0:
                    self.play(Write(eq))
                else: 
                    eq.align_to(history[0][j], UP)
                    self.play(TransformMatchingShapes(history[i-1][j], eq))
            self.wait()
        but.next_to(history[-1][-1], DOWN).shift(3*RIGHT)
        self.play(Write(but))
        self.wait()


class S12_Invariance(Scene):
    def construct(self):
        invariance_h = Tex("Gauge invariance remains in the covariant formulation", color=PURPLE)
        invariance = Maff(r"A^\mu \mapsto \Omega A_\mu \Omega^{-1} + i\Omega \partial_\mu \Omega^{-1}")
        question1 = Tex("Could we make a theory without this redundancy?", color=PURPLE)
        answer1 = Tex("If you try really hard")
        question2 = Tex(r"\textit{Should} we?", color=PURPLE)
        answer2 = Tex("No!")

        VGroup(invariance_h, invariance, question1, answer1, question2, answer2).arrange(DOWN)
        self.play(Write(invariance_h))
        self.wait()
        self.play(Write(invariance))
        self.wait()
        self.play(Write(question1))
        self.wait()
        self.play(Write(answer1))
        self.wait()
        self.play(Write(question2))
        self.wait()
        self.play(Write(answer2))
        self.wait()

        self.next_section()
        self.clear()

        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (1, 3), (1, 4),
                 (1, 5), (1, 6)]
        g = Graph(vertices, edges, layout="spring", layout_scale=3,
                labels={
                    1: Tex(r"\textbf{Gauge\\invariance}"),
                    2: Tex(r"Special\\relativity"),
                    3: Tex(r"General\\relativity"),
                    4: Tex(r"Behavior of\\photons"),
                    5: Tex(r"Behavior of\\electrons"),
                    6: Tex(r"\textit{Behavior of\\other fields?}"),
                }, vertex_config={
                    1: {"fill_opacity": 0.3},
                    2: {"fill_opacity": 0.1},
                    3: {"fill_opacity": 0.1},
                    4: {"fill_opacity": 0.1},
                    5: {"fill_opacity": 0.1},
                    6: {"fill_opacity": 0.1},
                    }, edge_config = {
                        edge: {"stroke_opacity": 0.3} for edge in edges
                    }
        )
        self.play(Write(g))
        self.wait()
        self.wait()
        self.wait()
        self.wait()

class S13_YM(Scene):
    def construct(self):
        ym_h = Tex("Yang--Mills theory", color=PURPLE)
        potential0 = Maff(r"A_\mu = ")
        matrix0 = Trix([ [r"A_t"], [r"A_x"], [r"A_y"], [r"A_z"]] )
        potential1 = Maff(r"A_\mu^\alpha = ")
        matrix1 = Trix([ 
            [r"A_t^0", r"A_t^1", r"A_t^2", r"A_t^3"], 
            [r"A_x^0", r"A_x^1", r"A_x^2", r"A_x^3"], 
            [r"A_y^0", r"A_y^1", r"A_y^2", r"A_y^3"], 
            [r"A_z^0", r"A_z^1", r"A_z^2", r"A_z^3"], 
        ] )
        potential2 = Maff(r"A_\mu^a = ")
        matrix2 = Trix([ 
            [r"A_t^{0(0,1,2,3)}", r"A_t^{1(0,1,2,3)}", r"A_t^{2(0,1,2,3)}", r"A_t^{3(0,1,2,3)}"], 
            [r"A_x^{0(0,1,2,3)}", r"A_x^{1(0,1,2,3)}", r"A_x^{2(0,1,2,3)}", r"A_x^{3{0,1,2,3}}"], 
            [r"A_y^{0(0,1,2,3)}", r"A_y^{1(0,1,2,3)}", r"A_y^{2(0,1,2,3)}", r"A_y^{3(0,1,2,3)}"], 
            [r"A_z^{0(0,1,2,3)}", r"A_z^{1(0,1,2,3)}", r"A_z^{2(0,1,2,3)}", r"A_z^{3(0,1,2,3)}"], 
        ] )
        emtensor = Maff(r"F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu")
        ymtensor = Maff(r"F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a - ig(A_\mu^a A_\nu^a - A_\nu^a A_\mu^a)")
        
        VGroup(ym_h, matrix2, ymtensor).arrange(DOWN)
        emtensor.align_to(ymtensor, UP)
        matrix0.align_to(matrix2, UP)
        potential0.next_to(matrix0, LEFT)
        matrix1.align_to(matrix2, UP)
        potential1.next_to(matrix1, LEFT)
        potential2.next_to(matrix2, LEFT)

        self.play(Write(ym_h))
        self.wait()
        self.play(Write(potential0), Write(matrix0))
        self.wait()
        self.play(Write(emtensor))
        self.wait()
        self.play(TransformMatchingShapes(potential0, potential1), TransformMatchingShapes(matrix0, matrix1))
        self.wait()
        self.play(TransformMatchingShapes(potential1, potential2), TransformMatchingShapes(matrix1, matrix2))
        self.wait()
        self.play(TransformMatchingShapes(emtensor, ymtensor))
        self.wait()

class S14_Bosons(Scene):
    def construct(self):
        ymtensor = Maff(r"F^{\mu\nu} = \partial^u A^\nu - \partial^\nu A^\mu - ig(A_\mu A_\nu - A_\nu A_\mu)")
        photon = Maff(r"A\mu A_\nu = A_\nu A_\mu")
        photon1 = SVGMobject("photon1.svg").scale(2)

        VGroup(ymtensor, photon1, photon).arrange(DOWN)

        gluon = Maff(r"A\mu A_\nu \ne A_\nu A_\mu").align_to(photon, UP)
        photon2 = SVGMobject("photon2.svg").scale(2).align_to(photon1, UP)
        gluon1 = SVGMobject("gluon1.svg").scale(2).align_to(photon1, UP)
        gluon2 = SVGMobject("gluon2.svg").scale(2).align_to(photon1, UP)
        gluon3 = SVGMobject("gluon3.svg").scale(2).align_to(photon1, UP)

        self.play(Write(ymtensor))
        self.wait()
        self.play(Write(photon))
        self.play(FadeIn(photon1))
        self.wait()
        self.play(ReplacementTransform(photon1, photon2))
        self.wait()
        self.play(ReplacementTransform(photon, gluon))
        self.play(ReplacementTransform(photon2, gluon1))
        self.wait()
        self.play(ReplacementTransform(gluon1, gluon2))
        self.wait()
        self.play(ReplacementTransform(gluon2, gluon3))
        self.wait()

class S15_End(Scene):
    def construct(self):
        end = Tex(r"by \textbf{Xing}\\Made with Manim\\UC Berkeley 2023", color=PURPLE, font_size=24)
        self.play(Write(end, run_time=3))
        self.wait()
        self.play(FadeOut(end))


def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    if animations: scene.play(*animations)

class Main(Scene):
    def construct(self):
        scenes = [
            S00_Title,
            S01_Notation,
            S02_Maxwells,
            S03_Simplify,
            S04_Potentials,
            S05_4Potential,
            S06_Tensor,
            S08_Deriv,
            S09_Hodge,
            S10_Maxtense,
            S11_Symmetry,
            S12_Invariance,
            S13_YM,
            S14_Bosons,
            S15_End,
                ]
        for scene in scenes:
            scene.construct(self)
            fade_out(self)

