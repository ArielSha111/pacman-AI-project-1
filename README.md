# pacman-AI-project-1
In this project i have used common AI algorithms for a version of Pacman, including ghosts. using the base of AI algoritems.
Most of the code was written by the University of Berkeley except for the various search algorithms.

* the original source is: [pacman project 1](https://inst.eecs.berkeley.edu/~cs188/fa20/project1/)

# Introduction
In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently using general search algorithms and using them on verius Pacman scenarios.

# Download
1. Make sure to have any version of python 3.
1. Download the full repository.
1. In order to view the code - open the files on your python ide of choice.
1. Go over to cmd where the downloaded files are located.
1. Type the following commend to see it all works: python pacman.py


# How to play
1. Open the CMD on the path of the downloaded files
1. Type: python pacman.py
1. Use your keyboard to move the Pacman.
1. Make sure to not let pacman lose many points since the game will be over.


# AI algorithms and commands

**Open the CMD on the path of the downloaded files and then type any of commends that will be presented.**

**At any point if Pacman gets stuck, you can exit the game by type CTRL-c .**


> Note that pacman.py supports a number of options that can each be expressed in a long way (e.g. , --layout) or a short way (e.g., -l). You can see the list of all options and their default values via the next commend:
python pacman.py -h
---
## self moving agents that always go west.
1. To test test regular maze type : python pacman.py --layout testMaze --pacman GoWestAgent 
1. To test tiny maze type : python pacman.py --layout tinyMaze --pacman GoWestAgent

## Depth First Search algorithm.
1. To test the tiny maze with tinyMazeSearch function type : python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
1. To test the tiny maze with default function type : python pacman.py -l tinyMaze -p SearchAgent
1. To test the medium maze with default function type  : python pacman.py -l mediumMaze -p SearchAgent
1. To test the big maze with default function type  : python pacman.py -l bigMaze -z .5 -p SearchAgent

## Breadth First Search algorithm.
1. To test the medium maze with bfs function type : python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
1. To test the big maze with bfs function type : python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
1. To test type eightpuzzle game with bfs function type : python eightpuzzle.py

> By changing the cost function, we can encourage Pacman to find different paths. For example, we can charge more for dangerous steps in ghost-ridden areas or less for steps in food-rich areas, and a rational Pacman agent should adjust its behavior in response.

## Varying the Cost Function
1. To test the medium maze with ucs function type : python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
1. To test the medium dotted maze with ucs function type : python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
1. To test the medium scary maze with ucs function type : python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

## A* search
1. To test the big maze with a* and manhattan Heuristic function type : python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

## Finding All the Corners 
1. To test Corners Problem on tiny maze with bfs type : python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
1. To test Corners Problem on big maze with bfs type : python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

## Finding All the Corners using A* with a certin huristic
1. To test A* with medium maze and corners Heuristic type : python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
1. To test A* with corners Heuristic in general type : -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic

## Eating All The Dots
1. To eat all the dots with generic A* type : python pacman.py -l testSearch -p AStarFoodSearchAgent
1. To eat all the dots with A* and food Heuristic type : -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
1. To eat all the dots with A* on trickySearch type : python pacman.py -l trickySearch -p AStarFoodSearchAgent

## Suboptimal Search
1. To test Suboptimal Search type : python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

# Viewing the code
## The main code that was not given and needed to be written by me located in the next filles:
1. search.py
1. searchAgent.py

## Files you might want to look at:
1. pacman.py
1. game.py
1. util.py
