import random
import pandas as pd

def generate_full_names(first_names, last_names, count):
    full_names = set()
    while len(full_names) < count:
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        full_names.add(name)
    return list(full_names)

def generate_edges(users, num_edges):
    edges = set()
    while len(edges) < num_edges:
        u, v = random.sample(users, 2)
        edge = tuple(sorted((u, v)))
        edges.add(edge)
    return list(edges)

first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace",
               "Hank", "Ivy", "Jack", "Karen", "Leo", "Mona", "Nate", "Olive",
               "Paul", "Quinn", "Rita", "Steve", "Tina"]

last_names = ["Anderson", "Brown", "Clark", "Davis", "Evans", "Franklin",
              "Garcia", "Hill", "Irwin", "Johnson", "Klein", "Lewis", "Moore",
              "Nelson", "Owens", "Parker", "Quinn", "Reed", "Smith", "Turner"]

full_names = generate_full_names(first_names, last_names, 100)

name_edges = generate_edges(full_names, 300)

print("Head (n=10):")
print(name_edges[:10])

# Convert the list of edges to a DataFrame
df_edges = pd.DataFrame(name_edges)

# Save as TSV
tsv_path = "social_network_edges.tsv"
df_edges.to_csv(tsv_path, sep="\t", index=False, header=False)

print(f"Data stored at: {tsv_path}")
