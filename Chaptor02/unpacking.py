import json

car_ages = [
    0, 9, 4, 8, 7, 20, 19, 1, 6, 15
]
car_ages_descending = sorted(car_ages, reverse=True)

oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]


def car_ages_descending():
    oldest, second_oldest, *others = car_ages_descending
    result = json.dumps({
        'count': len(car_ages_descending),
        'take': 0,
        'skip': 0,
        'data': {
            'oldest': oldest,
            'second_oldest': second_oldest,
            'others': others
        }
    })
    return result

