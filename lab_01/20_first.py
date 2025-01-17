# Constructing nested dictionary
Graph_of_A = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": []

}
print(Graph_of_A)

graph_of_B = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25, "Biratchowk": 30},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 11, "Dharan": 20},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Biratchowk": 30, "Itahari": 11, "Kanepokhari": 10},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25, "Urlabari": 40},
    "Kanepokhari": {"Biratchowk": 10, "Rangeli": 25, "Urlabari": 12},
    "Urlabari": {"Kanepokhari": 12, "Rangeli": 40, "Damak": 6},
    "Damak": {"Urlabari": 6}
}

print(graph_of_B)
