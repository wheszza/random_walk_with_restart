import graph
import parse
import calculator

import sys

if 3 != len(sys.argv) :
    print("参数错误")
    sys.exit()

parser = parse.Parser(sys.argv[1])
graph = parser.get_graph()
#graph.print_graph(sys.argv[2])
calculator = calculator.Calculator(graph)
calculator.save_P(sys.argv[2])