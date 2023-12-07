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
        title = Tex(r"The Strong Force", font_size=96, tex_template=temp)
        subtitle = Tex(r"A rough sketch of the theory", color=PURPLE, font_size=64, tex_template=temp).next_to(title, DOWN)
        self.play(Write(title))
        self.wait()
        self.play(Write(subtitle))
        self.wait()

        self.next_section()
        self.clear()

class S01_Notation(Scene):
    def construct(self):
        notation_h = Tex(r"Notation", color=PURPLE).shift(UP+UP+UP)

        scalars = Group(
                Tex("Scalar fields: "), 
                Maff(r"\phi, \lambda"),
        ).arrange(RIGHT)
        vectors = Group(
                Tex("3-vector fields: "),
                Maff(r"\vec E, \vec B, \vec A \equiv"),
                Trix([[r"\vec A_x"], [r"\vec A_y"], [r"\vec A_z"]])
        ).arrange(RIGHT)
        Group(scalars, vectors).arrange(direction=DOWN, buff=0.2)

        partials = Group(
                Tex("Partial derivatives: "),
                Maff(r"\partial_t \equiv \frac{\partial}{\partial t}")
        ).arrange(RIGHT)
        gradient = Group(
                Tex("Gradient: "),
                Maff(r"\grad \equiv"), 
                Trix([[r"\partial_x"], [r"\partial_y"], [r"\partial_z"]])
        ).arrange(RIGHT)
        Group(partials, gradient).arrange(direction=DOWN, buff=0.2)

        fourvectors = Group(
                Tex("4-vector fields: "),
                Maff(r"J^\mu, A^\nu(t,x,y,z) \equiv"), 
                Trix([[r"A^t"], [r"A^x"], [r"A^y"], [r"A^z"]])
        ).arrange(RIGHT)
        covariant = Group(
                Tex("Covariant derivative: "),
                Maff(r"\partial_\mu \equiv"), 
                Trix([[r"\partial_t"], [r"\partial_x"], [r"\partial_y"], [r"\partial_z"]])
        ).arrange(RIGHT)
        Group(fourvectors, covariant).arrange(direction=DOWN, buff=0.2)

        tensors = Group(Tex("Tensor fields: "), Trix([
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
        identity_h = Group(Tex(r"For any", color=PURPLE), Maff(r"\phi, \vec A")).arrange(RIGHT)
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
        Group(identity_h, identity, electrostat_h, electrostat, question).arrange(DOWN)

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
        potentials = Maff(r"""
            \dive\vec B &= 0\\
            \implies\vec B &\equiv \curl\vec A\\
            \curl\vec E &= -\partial_t\vec B = -\partial_t\curl\vec A\\
            \implies\vec E &\equiv -\grad\phi - \partial_t\vec A\\
        """)
        potentials_h = Tex(r"In electrodynamics", color=PURPLE).next_to(potentials, UP)
        self.play(Write(potentials_h))
        self.wait()
        self.play(Write(potentials))
        self.wait()

        self.next_section()
        self.clear()

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

        maxwells_h.shift(UP+UP)
        self.play(Write(maxwells_h))
        self.wait()

        for (i, el) in enumerate(maxwells):
            Group(*el).arrange(DOWN)
            for (j, eq) in enumerate(el):
                eq.align_to(el[0], RIGHT)
                if i == 0:
                    self.play(Write(eq))
                else: 
                    eq.align_to(maxwells[0][j], UP)
                    self.play(ReplacementTransform(maxwells[i-1][j], eq))
            self.wait()

class S05_4Potential(Scene):
    def construct(self):
        fourpotential = Group(Maff(r"A^\mu\equiv"), Trix([ [r"\phi"], [], [r"\vec A"], [] ])).arrange(RIGHT)
        fourpotentialexpanded = Group(Maff(r"A^\mu\equiv"), Trix([ [r"\phi"], [r"\vec A_x"], [r"\vec A_y"], [r"\vec A_z"] ])).arrange(RIGHT)
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
        whatabout = Group(
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
        self.play(ReplacementTransform(dem1, dem2))
        self.wait()
        self.play(ReplacementTransform(dem2, dem3))
        self.wait()
        self.play(ReplacementTransform(demtensor, current1))
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

        hodge_phi.next_to(hem_dem_done, UP)
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
        self.play(ReplacementTransform(hem_equiv, hem_equal), ReplacementTransform(hem_em, hem_hem))
        self.wait()
        self.play(Write(hem_partial), ReplacementTransform(hem_hem, hem_dem))
        self.wait()
        self.play(ReplacementTransform(hem_dem, hem_dem_done))
        self.wait()
        self.play(ReplacementTransform(Group(hem_partial, hem_tensor), hem_zero))
        self.wait()

class S10_Maxtense(Scene):
    def construct(self):
        maxwells = Tex(r"Maxwell's equation(s) in covariant form", color=PURPLE)
        equations = Maff(r"""
            \partial_\mu F^{\mu\nu} &= J^\nu\\
            \partial_\mu \hodge F^{\mu\nu} &= 0
        """)
        technicality = Maff(r"(F^{\mu\nu}\equiv\partial^u A^\nu - \partial^\nu A^\mu)")
        question = Tex(r"Is this the tightest model?")
        Group(maxwells, equations, technicality, question).arrange(DOWN)
        self.play(Write(maxwells))
        self.wait()
        self.play(Write(equations))
        self.wait()
        self.play(Write(technicality))
        self.wait()
        self.play(Write(question))
        self.wait()

class Main(Scene):
    def construct(self):
        scenes = [
            S00_Title,
            S01_Notation,
            S02_Maxwells,
            S03_Simplify,
            S04_Potentials,
            S06_Tensor,
            S08_Deriv,
            S09_Hodge,
                ]
        for scene in scenes:
            scene.construct(self)
            self.next_section()
            self.clear()

