from collections import Counter


def mode(data):
    try:
        mode_data = (Counter(data))
        mode = [k for k, v in mode_data.items() if v == mode_data.most_common(1)[0][1]]
        if len(mode) == 0:
            return None
        else:
            return mode[0]
    except ValueError:
        print("error: value is not a number")
        return None
    except IndexError:
        print("error: list is empty")
        return None
