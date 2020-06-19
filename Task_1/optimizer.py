import ast
import operator


class NodeOptimizationTransformer(ast.NodeTransformer):
    """
    A :class:'ast.NodeTransformer' subclass that walks the abstract syntax tree
    and allows modification of nodes.

    The NodeOptimisationTransformer will walk the AST and calculate binary
    operators for literals using DFS traversal order.
    """

    def __init__(self):
        self.binop_dict = {
            ast.Sub:        operator.sub,
            ast.Add:        operator.add,
            ast.Mult:       operator.mul,
            ast.Div:        operator.truediv,
            ast.MatMult:    operator.matmul,
            ast.Pow:        operator.pow,
            ast.Mod:        operator.mod,
            ast.LShift:     operator.lshift,
            ast.RShift:     operator.rshift,
            ast.BitOr:      operator.or_,
            ast.BitAnd:     operator.and_,
            ast.BitXor:     operator.xor,
            ast.FloorDiv:   operator.floordiv
        }

    def visit_BinOp(self, node: ast.BinOp):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)

        if not isinstance(node.left, ast.Num) or not isinstance(node.right, ast.Num):
            return node

        result = node
        try:
            op_type = type(node.op)
            result = ast.Num(n=self.binop_dict[op_type](node.left.n, node.right.n))
        except:
            print("Error: undefined type")

        return ast.copy_location(result, node)
