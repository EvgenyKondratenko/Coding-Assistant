import ast
import optimizer
from astmonkey import visitors

file = open("test.py").read()
tree = ast.parse(file)
optimisation = optimizer.NodeOptimizationTransformer()
tree = optimisation.visit(tree)
print(visitors.to_source(tree))
