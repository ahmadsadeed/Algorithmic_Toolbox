def get_optimal_value(max_weight, weight_list):
    weight_list.sort(key=lambda x: x[0] / x[1], reverse=True)
    value = 0.0

    for i in range(len(weight_list)):
        if max_weight >= weight_list[i][1]:
            max_weight -= weight_list[i][1]
            value += weight_list[i][0]
        else:
            value += (weight_list[i][0] * (max_weight / weight_list[i][1]))
            max_weight = 0
        if max_weight <= 0:
            break

    return value


if __name__ == '__main__':
    print("Main: ")
    capacity = 10
    data = [(500, 30)]  # [(60, 20), (100, 50), (120, 30)]
    optimal_value = get_optimal_value(capacity, data)
    print("Value is: ", optimal_value)
