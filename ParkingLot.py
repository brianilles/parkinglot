from nodes import Road, ParkingSpot, Entrance, Car, Undefined


class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.layer1_nodes = {}
        self.layer2_nodes = {}

    def add_layer1_node(self, object, node_id):
        if isinstance(object, (Road, ParkingSpot, Entrance, Undefined)):
            self.layer1_nodes[node_id] = object
        else:
            raise TypeError(f"{object} not valid.")

    def layer_1_node_get_neighbors(self, node_id):
        return self.layer1_nodes[node_id].connections

    def add_layer1_connection(self, node_a, node_b):
        if node_a in self.layer1_nodes and node_b in self.layer1_nodes:
            self.layer1_nodes[node_a].connections.add(node_b)
        elif node_a not in self.layer1_nodes and node_b not in self.layer1_nodes:
            raise KeyError(f"{node_a} and {node_b} do not exist.")
        elif node_a not in self.layer1_nodes:
            raise KeyError(f"{node_a} does not exist.")
        else:
            raise KeyError(f"{node_b} does not exist.")

    def add_layer2_node(self, object, layer1_node_id):
        if isinstance(object, (Car)):
            if layer1_node_id in self.layer1_nodes:
                if isinstance(self.layer1_nodes[layer1_node_id], (Road, ParkingSpot)):
                    self.layer2_nodes[layer1_node_id] = object
                else:
                    raise TypeError(
                        f"{object} cannot reside on {type(self.layer1_nodes[layer1_node_id])}")
            else:
                raise KeyError(f"{node_b} does not exist.")
        else:
            raise TypeError(f"{object} not valid.")

    def get_path_to_parking_spot(self, starting_node, target_parking_spot):
        visited = set()
        queue = []
        queue.append([starting_node])

        while len(queue) > 0:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                if node == target_parking_spot:
                    return path
                visited.add(node)
                for next_node in self.layer_1_node_get_neighbors(node):
                    new_path = list(path)
                    new_path.append(next_node)
                    queue.append(new_path)
        return "No path"
