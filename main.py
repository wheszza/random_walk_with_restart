import graph
import parse
import calculator
import sys
import numpy as np



#parser = parse.Parser(sys.argv[1])
parser = parse.Parser("./data/input.txt")
graph = parser.get_graph()
#graph.print_graph(sys.argv[2])
calculator = calculator.Calculator(graph)
edge = [7, 2]

calculator.unit_insert(edge)
#calculator.save_P(sys.argv[2])
calculator.save_P("./data/output.txt")