import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes (tables)
tables = ["Products", "Stores", "Customers", "Sales", "Budget"]

# Define relationships (edges)
relationships = [
    ("Products", "Sales"),   # Products are referenced in Sales
    ("Stores", "Sales"),     # Stores are referenced in Sales
    ("Customers", "Sales"),  # Customers are referenced in Sales
    ("Products", "Budget")   # Products are referenced in Budget
]

# Add nodes and edges to the graph
G.add_nodes_from(tables)
G.add_edges_from(relationships)

# Draw the graph
plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)  # Positioning
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
plt.title("Database Relationships")
plt.show()
