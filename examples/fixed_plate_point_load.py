#!/usr/bin/env python3

from topopt.topopt import StructuralOptim, Visualizer
from topopt.physical import PhysicalModel, Material
from topopt.mesh import Displacement, Load, Mesh
import matplotlib.pyplot as plt

volfrac = 0.5
ndiv = 20

mesh = Mesh()
mesh.rect_mesh(ndiv)

loads = Load(mesh)
loads.add_by_coord((1,0),(0,-1))

support = Displacement()
support.add_by_edge("left","all")

mat = Material()
mat.set_structural_params(2.1e5,.3)

pmodel = PhysicalModel(mesh,mat,support,loads)

optimizer = StructuralOptim(pmodel,volfrac,5)
optimizer.run()

visu = Visualizer(pmodel)
visu.write_result()

visu.plot_result()
plt.show()