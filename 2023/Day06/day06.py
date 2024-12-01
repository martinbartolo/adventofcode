file = open("input.txt", "r")
text = file.read().strip()


def num_ways_to_beat_record(text: str):
    lines = text.splitlines()
    race_times = [int(num) for num in lines[0].split(":")[1].strip().split()]
    records = [int(num) for num in lines[1].split(":")[1].strip().split()]

    result = 1
    for race_time, record in zip(race_times, records):
        ways_to_beat_record = 0
        for speed in range(1, race_time + 1):
            distance = speed * (race_time - speed)
            if distance > record:
                ways_to_beat_record += 1
        result *= ways_to_beat_record

    return result


print("Solution 1: ", num_ways_to_beat_record(text))


def num_ways_to_beat_record_2(text: str):
    lines = text.splitlines()
    race_time = int(lines[0].split(":")[1].strip().replace(" ", ""))
    record = int(lines[1].split(":")[1].strip().replace(" ", ""))

    ways_not_to_beat_record = 0

    # Run from 1 until we beat the record
    for speed in range(1, race_time + 1):
        distance = speed * (race_time - speed)
        if distance <= record:
            ways_not_to_beat_record += 1
        else:
            break

    # Run from race_time backwards until we beat the record
    for speed in range(race_time, 1, -1):
        distance = speed * (race_time - speed)
        if distance <= record:
            ways_not_to_beat_record += 1
        else:
            break

    return race_time - ways_not_to_beat_record


print("Solution 2: ", num_ways_to_beat_record_2(text))
