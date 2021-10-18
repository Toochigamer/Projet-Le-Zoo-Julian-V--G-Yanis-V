# importation du module "matplotlib" pour créer des graphiques
import matplotlib.pyplot as plt
# importation du module "networkx" pour simuler un réseau social
import networkx as nx

# création d' un graphe vide non orienté appelé "monReseau"
monReseau = nx.DiGraph()
monReseau.add_node("Emma")
monReseau.add_node("Enzo")
monReseau.add_node("Jasmine")
monReseau.add_node("Théo")
monReseau.add_node("Léa")
monReseau.add_node("Mehdi")
# création des liens entre les membres du réseau
monReseau. add_edge("Emma", "Enzo")
monReseau. add_edge("Emma", "Mehdi")
monReseau. add_edge("Enzo", "Emma")
monReseau. add_edge("Jasmine", "Théo")
monReseau. add_edge("Jasmine", "Léa")
monReseau. add_edge("Théo", "Jasmine")
monReseau. add_edge("Théo", "Mehdi")
monReseau. add_edge("Léa", "Jasmine")
monReseau. add_edge("Léa", "Mehdi")
monReseau. add_edge("Mehdi", "Emma")
monReseau. add_edge("Mehdi", "Théo")
monReseau. add_edge("Mehdi", "Léa")

# dessine (draw) et affiche (show) le graphe "monReseau"
nx.draw(monReseau, with_labels=True)
plt.show()

print("Nombre de personnes =", monReseau.number_of_nodes())
print("Nombre de liens =", monReseau. number_of_edges())