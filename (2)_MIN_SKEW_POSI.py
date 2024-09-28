def minimum_skew(genome):
    skew_values = [0]  # skew value at position 0 is 0
    min_skew = 0

    # Calculate the skew at each position
    for i in range(len(genome)):
        if genome[i] == 'G':
            skew_values.append(skew_values[i] + 1)
        elif genome[i] == 'C':
            skew_values.append(skew_values[i] - 1)
        else:
            skew_values.append(skew_values[i])

        min_skew = min(min_skew, skew_values[i + 1])

    # Find positions with the minimum skew value
    min_skew_positions = [i for i, skew in enumerate(skew_values) if skew == min_skew]
    return min_skew_positions

ANS = minimum_skew("GATACACTTCCCGAGTAGGTACTG")
print(ANS)