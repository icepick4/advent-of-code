def read_file(filename):
    length_x = 0
    length_y = 0
    with open(filename, 'r') as f:
        temp_coords = []
        for line in f:
            coords = line.strip().split('=')
            for i, coord in enumerate(coords[1:]):
                if i == 0:
                    sensor_x = int(coord.split(',')[0])
                elif i == 1:
                    sensor_y = int(coord.split(':')[0])
                elif i == 2:
                    beacon_x = int(coord.split(',')[0])
                elif i == 3:
                    beacon_y = int(coord)
            temp_coords.append([sensor_x, sensor_y, beacon_x, beacon_y])
    beacons = []
    sensors = []
    for coord in temp_coords:
        beacons.append([coord[2], coord[3]])
        distance = abs(coord[0] - coord[2]) + abs(coord[1] - coord[3])
        sensors.append([[coord[0], coord[1]], distance])
    return sensors, beacons


def not_beacon(x, y, beacons):
    for beacon in beacons:
        if beacon[0] == x and beacon[1] == y:
            return False
    return True


def not_sensor(x, y, sensors):
    for sensor in sensors:
        if sensor[0][0] == x and sensor[0][1] == y:
            return False
    return True


def sensor_area(x, y, distance, beacons):
    # DIRECTIONS = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
    print('The distance from ', [x, y], 'is : ', distance)
    current_pos = [x, y]
    no_beacon = []
    if current_pos[1] > 10:
        dist = current_pos[1] - 10
    else:
        dist = 10 - current_pos[1]
    current_pos[1] = 10
    current_pos[0] = current_pos[0] - distance
    print(current_pos[0], distance * 2 - dist * 2 + 1)
    for i in range(distance * 2 - dist * 2 + 1):
        if not_beacon(current_pos[0], current_pos[1], beacons):
            no_beacon.append([current_pos[0], current_pos[1]])
        current_pos[0] += 1
    return no_beacon


if __name__ == '__main__':
    sensors, beacons = read_file('input-test.txt')
    no_beacon = []
    no_beacon = sensor_area(2, 0, 10,  beacons)
    COUNTER = 0
    for sensor in sensors:
        if sensor[0][0] == 8 and sensor[0][1] == 7:
            print(sensor[1])
        temp_no_beacon = sensor_area(
            sensor[0][0], sensor[0][1], sensor[1], beacons)
        for i in temp_no_beacon:
            if i not in no_beacon:
                no_beacon.append(i)
    no_beacon.sort()
    for i in no_beacon:
        print(i)

    print(len(no_beacon))
