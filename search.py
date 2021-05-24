# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def InQueue(item, queue):
    for queue_item in queue.list:
        if queue_item[0] == item:
            return True
    return False

def generalGraphSearch(problem, data_structure):
    from util import Stack
    node_point = problem.getStartState()  # initialize the first node
    if problem.isGoalState(node_point):
        return []
    node_path = []
    data_structure.push([node_point, node_path])  # push to the structure the first node with an empty path
    explored_list = []
    while not data_structure.isEmpty():  # as long as the structure is not empty
        node, path = data_structure.pop()  # we pop a nude and a path
        if problem.isGoalState(node):  # check the node
            return path  # return the path if needed
        explored_list.append(node)  # else we mark it as visited
        successor = problem.getSuccessors(node)  # then we add all of is successor to the stack
        if successor:  # if there is a successor
            for successor_node in successor:  # loop on all of the successors
                if successor_node[0] not in explored_list:  # consider only the unvisited nodes
                    if isinstance(data_structure, Stack) or not InQueue(successor_node[0], data_structure):  # if stack we can just scan
                        data_structure.push((successor_node[0], path + [successor_node[1]]))  # add to the stack
    return []  # if the func reaches here it means no path was found therefore we return an empty list

def depthFirstSearch(problem):  # page 85
    return generalGraphSearch(problem, util.Stack())

def breadthFirstSearch(problem):  # page 82
    return generalGraphSearch(problem, util.Queue())

def inPriorityQueue(item, queue):
    for queue_item in queue.heap:
        if queue_item[2][0] == item:  #check if queue item at [2] place whice is 'item' = item
            return True
    return False

def uniformCostSearch(problem):  # page84
    node_point = problem.getStartState()  # initialize the first node
    if problem.isGoalState(node_point):
        return []
    p_queue = util.PriorityQueue()
    node_path = []
    p_queue.push((node_point, node_path), 0)
    explored_list = []
    while not p_queue.isEmpty():
        node, path = p_queue.pop()
        if problem.isGoalState(node):
            return path
        explored_list.append(node)
        successor = problem.getSuccessors(node)
        if successor:
            for successor_node in successor:
                if successor_node[0] not in explored_list:
                    if not inPriorityQueue(successor_node[0], p_queue):
                        newPath = path + [successor_node[1]]
                        priority = problem.getCostOfActions(newPath)
                        p_queue.push((successor_node[0], newPath), priority)
                    else:
                        for node in p_queue.heap:
                            if node[2][0] == successor_node[0]:
                                #node[2] = item, item[0] = node_point-->node[2][0] = the node point of a given
                                # successor_node, node[2][1] = the path of a given successor_node
                                oldPri = problem.getCostOfActions(node[2][1])  #get the cost of this node path
                        newPri = problem.getCostOfActions(path + [successor_node[1]])
                        if newPri < oldPri :
                            p_queue.update((successor_node[0], path + [successor_node[1]]), newPri)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):  # page 95
    node_point = problem.getStartState()  # initialize the first node
    if problem.isGoalState(node_point):
        return []
    p_queue = util.PriorityQueue()
    node_path = []
    p_queue.push((node_point, node_path), 0)
    explored_list = []
    while not p_queue.isEmpty():
        node, path = p_queue.pop()
        if problem.isGoalState(node):
            return path
        explored_list.append(node)
        successor = problem.getSuccessors(node)
        if successor:
            for successor_node in successor:
                if successor_node[0] not in explored_list:
                    if not inPriorityQueue(successor_node[0], p_queue):
                        newPath = path + [successor_node[1]]
                        newCostToNode = problem.getCostOfActions(newPath)
                        Cost = newCostToNode + heuristic(successor_node[0], problem)
                        p_queue.push((successor_node[0], newPath), Cost)
                    else:
                        for node in p_queue.heap:
                            if node[2][0] == successor_node[0]:
                                #node[2] = item, item[0] = node_point-->node[2][0] = the node point of a given
                                # successor_node, node[2][1] = the path of a given successor_node
                                oldcost = problem.getCostOfActions(node[2][1])  #get the cost of this node path
                        newcost = problem.getCostOfActions(path + [successor_node[1]])
                        if newcost < oldcost:
                            p_queue.update((successor_node[0], path + [successor_node[1]]), newcost)
    return []










# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
