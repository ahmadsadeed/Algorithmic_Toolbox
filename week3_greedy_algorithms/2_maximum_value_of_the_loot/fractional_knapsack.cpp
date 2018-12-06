#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::pair;

bool sortVectors(std::pair<int, int> &a, pair<int, int> &b) {
    return ( (double) a.first/a.second) > ((double) b.first/b.second);
}

double get_optimal_value(int capacity, vector<pair<int, int>> data) {
    sort(data.begin(), data.end(), sortVectors);
    double value = 0.0;

    for (int i = 0; i < data.size(); i++) {
        if ( capacity >= data[i].second) {
            capacity -= data[i].second;
            value += data[i].first;
        } else {
            value += (data[i].first *  ((double) capacity / data[i].second));
            capacity = 0;
        }
        if (capacity <= 0) {
            break;
        }
    }

    return value;
}

int main() {
    int n;
    int capacity;
    std::cin >> n >> capacity;

    vector<pair<int, int>> data(n);
    for (int i = 0; i < n; i++) {
        std::cin >> data[i].first >> data[i].second;
    }

    double optimal_value = get_optimal_value(capacity, data);

    std::cout.precision(10);
    std::cout << optimal_value << std::endl;
    return 0;
}


