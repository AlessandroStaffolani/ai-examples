
import MCProblem as myProblem
from MCProblem import MCProblem
from Solver import Solver
import core.search as search
import time

problem = MCProblem()
solver = Solver(problem)
solver.execute_breadth_first_tree_search()
print(solver)

solver.execute_breadth_first_graph_search()
print(solver)

solver.execute_astar_search()
print(solver)


# def printPath(path):
#     print("Path size = " + str(len(path)))
#     for node in path:
#         print(node)
#
#
# problem = myProblem.MCProblem()
#
# startTime = time.time()
# agent = search.breadth_first_tree_search(problem)
# solution = agent.solution()
# path = agent.path()
# endTime = time.time() - startTime
# print("\n\nBREADTH FIRST TREE EXECUTION")
# print("Solution for problem in %s seconds" %endTime)
# print("Solution = " + str(solution))
# printPath(path)
#
# startTime = time.time()
# agent = search.breadth_first_graph_search(problem)
# solution = agent.solution()
# path = agent.path()
# endTime = time.time() - startTime
# print("\n\nBREADTH FIRST GRAPH EXECUTION")
# print("Solution for problem in %s seconds" %endTime)
# print("Solution = " + str(solution))
# printPath(path)
#
# startTime = time.time()
# agent = search.depth_first_graph_search(problem)
# solution = agent.solution()
# path = agent.path()
# endTime = time.time() - startTime
# print("\n\nDEPTH LIMITED SEARCH EXECUTION")
# print("Solution for problem in %s seconds" %endTime)
# print("Solution = " + str(solution))
# printPath(path)
#
# startTime = time.time()
# agent = search.astar_search(problem)
# solution = agent.solution()
# path = agent.path()
# endTime = time.time() - startTime
# print("\n\nA* EXECUTION")
# print("Solution for problem in %s seconds" %endTime)
# print("Solution = " + str(solution))
# printPath(path)




