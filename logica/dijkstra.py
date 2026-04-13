def get_min_distance_node(distances, unvisited):
    # varre as distâncias dos nós ainda não visitados
    min_dist = float('infinity')
    min_node = None
    
    # Compara a distância salva pra descobrir qual tem o passe mais "rápido" até agora
    for no in unvisited:
        if distances[no] < min_dist:
            min_dist = distances[no]
            min_node = no
            
    return min_node

def dijkstra(graph, start_name, end_name):
    # logica principal de achar o caminho
    distancias = {v.id: float('infinity') for v in graph}
    distancias[start_name] = 0
    predecessores = {v.id: None for v in graph}
    
    nao_visitados = [v.id for v in graph]
    
    while nao_visitados:
        # Chama a função que tem no passo 3
        no_atual = get_min_distance_node(distancias, nao_visitados)
        
        if no_atual is None or distancias[no_atual] == float('infinity'):
            break # Não tem mais como avançar
            
        vertice_atual = graph.vertices[no_atual] # Puxando da estrutura da Marys
        
        # Simulação do relaxamento de arestas
        for vizinho_id, peso in vertice_atual.vizinhos.items():
            if vizinho_id in nao_visitados:
                nova_dist = distancias[no_atual] + peso
                if nova_dist < distancias[vizinho_id]:
                    distancias[vizinho_id] = nova_dist
                    predecessores[vizinho_id] = no_atual
                    
        nao_visitados.remove(no_atual)
        
        # Otimização: Se já chegou no destino, pode parar
        if no_atual == end_name:
            break
            
    return predecessores

def reconstruct_path(predecessors, start_name, end_name):
    # reconstrução do caminho ótimo
    caminho_tracado = []
    no_atual = end_name
    
    # Voltamos a lista de trás pra frente (do destino para a origem)
    while no_atual is not None:
        caminho_tracado.insert(0, no_atual)
        if no_atual == start_name:
            break
        no_atual = predecessors.get(no_atual)
        
    # Validando se ele de fato conseguiu achar um caminho que conecte a origem e o fim
    if caminho_tracado[0] == start_name:
        return caminho_tracado
    else:
        return []
