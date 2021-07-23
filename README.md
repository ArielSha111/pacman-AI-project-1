
# pacman-AI-project-1
in this project i have used common AI algorithems for a version of Pacman, including ghosts. using the base of AI algoritems.
Most of the code was written by the University of Berkeley except for the various search algorithms.

* the original source is: [pacman project 1](https://inst.eecs.berkeley.edu/~cs188/fa20/project1/)

# Introduction
In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently using general search algorithms and using them on verius Pacman scenarios.

# Download and play
1. make sure to have any version of python 3.
1. download the full repository.
1. open the filles on your python ide of choice.
1. go over to cmd where the downloaded filles are located.
1. type the following commend to see it all works.
    * python pacman.py


# How to play
1. use your keyboard to move the Pacman.
1. make sure to not let pacman lose many points since the game will be over.

# AI algorithms and commands

**go over to cmd where the downloaded filles are located to type any of following commends the will be presented.**

**at any point if Pacman gets stuck, you can exit the game by typing CTRL-c into your terminal.**

Soon, your agent will solve not only tinyMaze, but any maze you want.

> Note that pacman.py supports a number of options that can each be expressed in a long way (e.g. , --layout) or a short way (e.g., -l). You can see the list of all options and their default values via the next commend:
python pacman.py -h
---
## self moving agents that always go west.
1. typing into your terminal: python pacman.py --layout testMaze --pacman GoWestAgent 
1. typing into your terminal: python pacman.py --layout tinyMaze --pacman GoWestAgent

## Depth First Search algorithm.
1. typing into your terminal: python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
1. typing into your terminal: python pacman.py -l tinyMaze -p SearchAgent
1. typing into your terminal: python pacman.py -l mediumMaze -p SearchAgent
1. typing into your terminal: python pacman.py -l bigMaze -z .5 -p SearchAgent

## Breadth First Search algorithm.
1. typing into your terminal: python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
1. typing into your terminal: python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
1. typing into your terminal: python eightpuzzle.py

> By changing the cost function, we can encourage Pacman to find different paths. For example, we can charge more for dangerous steps in ghost-ridden areas or less for steps in food-rich areas, and a rational Pacman agent should adjust its behavior in response.
## Varying the Cost Function
1. typing into your terminal: python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
1. typing into your terminal: python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
1. typing into your terminal: python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

## A* search
1. typing into your terminal: python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

## Finding All the Corners 
1. typing into your terminal: python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
1. typing into your terminal: python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

## Finding All the Corners using A* with a certin huristic
1. typing into your terminal: python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
1. typing into your terminal: -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic

## Eating All The Dots
1. typing into your terminal: python pacman.py -l testSearch -p AStarFoodSearchAgent
1. typing into your terminal: -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
1. typing into your terminal: python pacman.py -l trickySearch -p AStarFoodSearchAgent

## Suboptimal Search
1. typing into your terminal: python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

# viewing the code
## the main code that was not given and need to be written by me is in the next filles:
1. search.py
1. searchAgent.py

## Files you might want to look at:
1. pacman.py
1. game.py
1. util.py
