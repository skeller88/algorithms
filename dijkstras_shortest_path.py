import sys

graph = {
    's': {
        'neighbors': {'a': 1, 'b': 2},
    },
    'a': {
        'neighbors': {'s': 1, 'd': 7},
    },
    'b': {
        'neighbors': {'s': 2, 'd': 2},
    },
    'd': {
        'neighbors': {'a': 7, 'b': 2}
    },
}

class HeapDict(dict):
    def __init__(self, **kwargs):
        pass

    def get_min(self):
        min_item = min_priority = None

        for item, priority in self.iteritems():
            if ((min_priority != 0 and not min_priority)
                or priority < min_priority):
                min_item = item
                min_priority = priority

        del self[min_item]

        return min_item, min_priority

def dijkstras(graph, source):
    unvisited = HeapDict()

    for node in graph.keys():
        unvisited[node] = sys.maxint if node != source else 0

    visited = {}
    current = None

    while unvisited:
        current, current_distance = unvisited.get_min()
        # print '******', current, current_distance

        visited[current] = {
            'distance': current_distance,
            'previous': graph[current].get('previous')
        }

        neighbors = graph[current]['neighbors']

        for neighbor, edge in neighbors.iteritems():
            partial_path_distance = current_distance + edge

            if (unvisited.get(neighbor) and partial_path_distance <
                    unvisited[neighbor]):
                # decrease the key of the node
                # if unvisited were a classic heap, you would have some
                # "decrease_key" method that reassigns priority
                unvisited[neighbor] = partial_path_distance
                graph[neighbor]['previous'] = current

    return visited

print dijkstras(graph, 's')