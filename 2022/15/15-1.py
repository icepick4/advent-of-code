import sys


def read_file(filename):
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


def sensor_area(x, y, distance, beacons, y_pos):
    current_pos = [x, y]
    no_beacon = []
    if current_pos[1] > y_pos:
        dist = current_pos[1] - y_pos
    elif current_pos[1] < y_pos:
        dist = y_pos - current_pos[1]
    else:
        dist = 0
    # print(dist, distance)
    if dist >= distance:
        return no_beacon
    current_pos[1] = y_pos
    current_pos[0] = current_pos[0] - distance + dist
    for _ in range(distance*2 - dist * 2 + 1):
        if not_beacon(current_pos[0], current_pos[1], beacons):
            no_beacon.append([current_pos[0], current_pos[1]])
        current_pos[0] += 1
    return no_beacon


def check_line(no_beacon):
    for i, beacon in enumerate(no_beacon):
        if beacon[0] > 0 and beacon[1] < 20:
            if beacon[0] - 1 != no_beacon[i-1][0] and beacon[1] == no_beacon[i-1][1]:
                print(beacon[0] - 1, beacon[1])
                print((beacon[0]-1) * 4000000 + beacon[1])
                sys.exit()


if __name__ == '__main__':
    sensors, beacons = read_file('input.txt')
    COUNTER = 1
    y_pos = 10
    while True:
        print(COUNTER)
        no_beacon = []
        for sensor in sensors:
            temp_no_beacon = sensor_area(
                sensor[0][0], sensor[0][1], sensor[1], beacons, y_pos + COUNTER)
            no_beacon += temp_no_beacon

        no_beacon.sort()
        # remove duplicates
        no_beacon = [no_beacon[i] for i in range(
            len(no_beacon)) if i == 0 or no_beacon[i] != no_beacon[i-1]]
        check_line(no_beacon)
        no_beacon = []
        for sensor in sensors:
            temp_no_beacon = sensor_area(
                sensor[0][0], sensor[0][1], sensor[1], beacons, y_pos - COUNTER)
            no_beacon += temp_no_beacon

        no_beacon.sort()
        # remove duplicates
        no_beacon = [no_beacon[i] for i in range(
            len(no_beacon)) if i == 0 or no_beacon[i] != no_beacon[i-1]]
        check_line(no_beacon)
        COUNTER += 1
