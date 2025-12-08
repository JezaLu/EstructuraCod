grafo={
    "A":["B","C"],
    "B":["A","C"],
    "C":["A"],
    "D":["B"],
}
for Nodo in grafo:
    print (f"{Nodo} el nodo establecido es:{grafo[Nodo]}")