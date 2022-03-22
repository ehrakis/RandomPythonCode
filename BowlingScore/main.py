def compute_bowling_score(falling_skittles: list[int]):
    multiplicator = [1] * (len(falling_skittles)+2)
    result = 0
    is_first_throw = True
    previous_throw = None

    for index, skittle in enumerate(falling_skittles):

        if skittle == 10 or not is_first_throw and skittle + previous_throw == 10:
            multiplicator[index+1] += 1

            if is_first_throw:
                multiplicator[index+2] += 1
                is_first_throw = False

        result += skittle * multiplicator[index]
        is_first_throw = not is_first_throw
        previous_throw = skittle

    return result
