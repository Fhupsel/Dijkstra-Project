def dijkstra(graph, start):
  import heapq # filas de prioridade (menor elemento -> peso)
  distances = {node: float('infinity') for node in graph} # todos nós com distância infinita
  distances[start] = 0
  priority_queue = [(0, start)]
  while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue) # remove e retorna o menor elemento da fila
    if current_distance > distances[current_node]:
      continue
    for neighbor, weight in graph[current_node].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (distance, neighbor))
  return distances