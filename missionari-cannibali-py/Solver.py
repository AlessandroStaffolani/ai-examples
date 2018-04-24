
from core.search import Node

from core.utils import (
    is_in, argmin, argmax, argmax_random_tie, probability, weighted_sampler,
    memoize, print_table, open_data, PriorityQueue, name,
    distance, vector_add
)

from collections import defaultdict, deque
import math
import random
import sys
import bisect
import time


class Solver:

    def __init__(self, problem=None):
        self.problem = problem
        self.node_expanded = 0
        self.execution_time = 0
        self.solution = []
        self.path = []
        self.algorithmName = ""

    def reinit(self):
        self.node_expanded = 0
        self.execution_time = 0
        self.solution = []
        self.path = []

    def __str__(self):
        string = self.algorithmName + "\n"
        string += str(self.solution) + "\n"
        string += "Solution for problem in " + str(self.execution_time) + " seconds\n"
        string += "Node expanded for problem: " + str(self.node_expanded) + "\n"
        string += self.get_path_string() + "\n"
        return string

    def get_path_string(self):
        print("Path size = " + str(len(self.path)))
        string = "Path size = " + str(len(self.path)) + "\n"
        for node in self.path:
            string += str(node) + "\n"
        return string

    def execute_breadth_first_tree_search(self):
        self.reinit()
        self.algorithmName = "BREAD FIRST TREE SEARCH"
        start_time = time.time()
        agent = self.breadth_first_tree_search(self.problem)
        self.execution_time = time.time() - start_time
        self.solution = agent.solution()
        self.path = agent.path()

    def execute_breadth_first_graph_search(self):
        self.reinit()
        self.algorithmName = "BREAD FIRST GRAPH SEARCH"
        start_time = time.time()
        agent = self.breadth_first_graph_search(self.problem)
        self.execution_time = time.time() - start_time
        self.solution = agent.solution()
        self.path = agent.path()

    def execute_astar_search(self):
        self.reinit()
        self.algorithmName = "A* SEARCH"
        start_time = time.time()
        agent = self.astar_search(self.problem)
        self.execution_time = time.time() - start_time
        self.solution = agent.solution()
        self.path = agent.path()

# ---------- ALGORITHM ----------

    def breadth_first_tree_search(self, problem):
        """Search the shallowest nodes in the search tree first.
                Search through the successors of a problem to find a goal.
                The argument frontier should be an empty queue.
                Repeats infinitely in case of loops. [Figure 3.7]"""

        frontier = deque([Node(problem.initial)])  # FIFO queue

        while frontier:
            node = frontier.popleft()
            if problem.goal_test(node.state):
                return node
            to_add_on_frontier = node.expand(problem)
            self.node_expanded += len(to_add_on_frontier)
            frontier.extend(to_add_on_frontier)
        return None

    def breadth_first_graph_search(self, problem):
        """[Figure 3.11]
        Note that this function can be implemented in a
        single line as below:
        return graph_search(problem, FIFOQueue())
        """
        node = Node(problem.initial)
        if problem.goal_test(node.state):
            return node
        frontier = deque([node])
        explored = set()
        while frontier:
            node = frontier.popleft()
            explored.add(node.state)
            to_add_on_frontier = node.expand(problem)
            self.node_expanded += len(to_add_on_frontier)
            for child in to_add_on_frontier:
                if child.state not in explored and child not in frontier:
                    if problem.goal_test(child.state):
                        return child
                    frontier.append(child)
        return None

    def best_first_graph_search(self, problem, f):
        """Search the nodes with the lowest f scores first.
        You specify the function f(node) that you want to minimize; for example,
        if f is a heuristic estimate to the goal, then we have greedy best
        first search; if f is node.depth then we have breadth-first search.
        There is a subtlety: the line "f = memoize(f, 'f')" means that the f
        values will be cached on the nodes as they are computed. So after doing
        a best first search you can examine the f values of the path returned."""
        f = memoize(f, 'f')
        node = Node(problem.initial)
        if problem.goal_test(node.state):
            return node
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            to_add_on_frontier = node.expand(problem)
            self.node_expanded += len(to_add_on_frontier)
            for child in to_add_on_frontier:
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    incumbent = frontier[child]
                    if f(child) < f(incumbent):
                        del frontier[incumbent]
                        frontier.append(child)
        return None

    def astar_search(self, problem, h=None):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or problem.h, 'h')
        return self.best_first_graph_search(problem, lambda n: n.path_cost + h(n))
