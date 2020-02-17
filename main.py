from ParkingLot import ParkingLot
from nodes import Road, ParkingSpot, Entrance, Car, Undefined


def buildBasicParkingLot():
    pl = ParkingLot("World")

    # build road
    for i in range(10):
        pl.add_layer1_node(Road(), i)
        # add road connections
        if (i > 0):
            pl.add_layer1_connection(i-1, i)

    # build parkingspot and entrance
    pl.add_layer1_node(ParkingSpot(), 10)
    pl.add_layer1_node(Entrance(), 11)
    pl.add_layer1_connection(9, 10)
    pl.add_layer1_connection(10, 11)

    # build alternate (farther route)
    for i in range(12, 19):
        pl.add_layer1_node(Road(), i)
        if i == 12:
            pl.add_layer1_connection(6, 12)
        if i > 12:
            pl.add_layer1_connection(i-1, i)
    pl.add_layer1_connection(18, 10)
    pl.add_layer2_node(Car(), 0)

    print(pl.layer1_nodes)
    print(pl.layer2_nodes)
    print()
    print("Path to parking spot:")
    print(pl.get_path_to_parking_spot(0, 10))


if __name__ == '__main__':
    buildBasicParkingLot()
