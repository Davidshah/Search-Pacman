# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  # Initiate frontier as a stack
  frontier = util.Stack()
  # Push starting state to stack
  frontier.push((problem.getStartState(), [], []))
  # Check that frontier isn't empty and proceed
  while not frontier.isEmpty():
      # Pull variables from frontier
      current_state, actions, visited = frontier.pop()
      
      # Iterate through successors at current_state
      for coord, direction, steps in problem.getSuccessors(current_state):
          # Check if already visited
          if not coord in visited:
              # Check if found goal, return actions
              if problem.isGoalState(coord):
                  return actions + [direction]
              # If goal not found, push successor onto frontier
              frontier.push((coord, actions + [direction], visited + [current_state]))

  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  # Initiate frontier as a queue
  frontier = util.Queue()
  # Push starting state to queue
  frontier.push((problem.getStartState(), []))
  # Initialize visited variable
  visited = []
  # Check that frontier isn't empty and proceed
  while not frontier.isEmpty():
      # Pull variables from frontier
      current_state, actions = frontier.pop()
      
      # Iterate through successors at current_state
      for coord, direction, steps in problem.getSuccessors(current_state):
          # Check if already visited
          if not coord in visited:
              # Check if found goal, return actions
              if problem.isGoalState(coord):
                  return actions + [direction]
              # If goal not found, push successor onto frontier and mark visited
              frontier.push((coord, actions + [direction]))
              visited.append(coord)

  return []
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  # Initiate frontier as a priority queue
  frontier = util.PriorityQueue()
  # Push starting state to queue
  frontier.push((problem.getStartState(), []), 0)
  # Initialize visited variable
  visited = []
  # Check that frontier isn't empty and proceed
  while not frontier.isEmpty():
      # Pull variables from frontier
      current_state, actions = frontier.pop()
      
      # Early termination if at goal
      if problem.isGoalState(current_state):
          return actions
          
      # Add to visited
      visited.append(current_state)
      
      # Iterate through successors at current_state
      for coord, direction, steps in problem.getSuccessors(current_state):
          # Check if already visited
          if not coord in visited:
              # Get actions and push to frontier
              n_actions = actions + [direction]
              frontier.push((coord, n_actions), problem.getCostOfActions(n_actions))      

  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  # Initiate frontier as a priority queue
  frontier = util.PriorityQueue()
  start = problem.getStartState()
  # Push starting state to queue
  frontier.push((start, []), heuristic(start, problem))
  # Initialize visited variable
  visited = []
  # Check that frontier isn't empty and proceed
  while not frontier.isEmpty():
      # Pull variables from frontier
      current_state, actions = frontier.pop()
      
      # Early termination if at goal
      if problem.isGoalState(current_state):
          return actions
          
      # Add to visited
      visited.append(current_state)
      
      # Iterate through successors at current_state
      for coord, direction, cost in problem.getSuccessors(current_state):
          # Check if already visited
          if not coord in visited:
              # Get actions/score and push to frontier
              n_actions = actions + [direction]
              score = problem.getCostOfActions(n_actions) + heuristic(coord, problem)
              frontier.push((coord, n_actions), score)  
              
  return []  
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
