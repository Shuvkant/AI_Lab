
from queue import PriorityQueue
import math

graph = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25, "Biratchowk": 30},
    "Itahari": {"Biratnagar": 22, "Dharan": 20, "Biratchowk": 11},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Biratnagar": 30, "Itahari": 11, "Kanepokhari": 10},
    "Kanepokhari": {"Biratchowk": 10, "Rangeli": 25, "Urlabari": 12},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25, "Urlabari": 40},
    "Urlabari": {"Kanepokhari": 12, "Rangeli": 40, "Damak": 6},
    "Damak": {"Urlabari": 6},
}

h = {
    "Biratnagar": 46,
    "Itahari": 39,
    "Dharan": 41,
    "Rangeli": 28,
    "Biratchowk": 29,
    "Kanepokhari": 17,
    "Urlabari": 6,
    "Damak": 0,
}


def astar(G, h, start, goal):
    PQ = PriorityQueue()
    prev = dict()
    visited = set()

    # PQ.put((0+h[start], (start, 0)))
    # outStateFScore, (outState, outStateGScore) = PQ.get()
    # print(f"outState={outState}\n outStateGScore={
    #       outStateGScore}\n outStateFScore={outStateFScore}")

    PQ.put((0+h[start], (start, 0)))
    prev[start] = " "
    while (not PQ.empty()):
        outStateFScore, (outState, outStateGScore) = PQ.get()
        print(f"outState={outState}\n outStateGScore={
            outStateGScore}\n outStateFScore={outStateFScore}")

        print(f"Size of elements in queue: {PQ.qsize()}")
        visited.add(outState)
        print(f"visited_elements:{visited}")
        if (outState == goal):
            return True, prev, outStateGScore
        for chimeki in G[outState]:
            if chimeki not in visited:
                chimekiGScore = outStateGScore + G[outState][chimeki]
                chimekiFScore = h[chimeki] + chimekiGScore
                print(chimeki)
                print(f"chimekiGScore={chimekiGScore}")
                print(f"chimekiFScore={chimekiFScore}\n")
                PQ.put((chimekiFScore, (chimeki, chimekiGScore)))
                prev[chimeki] = outState
    return False, prev, math.inf


def reconstruct_path(prev, goal):
    path = goal
    while prev[goal] != " ":
        path = prev[goal]+"->"+path
        goal = prev[goal]
    return f"Path is: {path}"


start = 'Biratnagar'
goal = "Damak"
goalFound, prev, cost = astar(graph, h, start, goal)
if (goalFound):
    print(reconstruct_path(prev, goal))
    print("Cost: ", cost)
else:
    print("No path found")
