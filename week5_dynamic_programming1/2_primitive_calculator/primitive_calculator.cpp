#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using std::vector;

vector<int> optimal_sequence(int n) {
    std::vector<int> vecNumOfOperations;
    std::vector<int> sequence;

    vecNumOfOperations.push_back(0);
    vecNumOfOperations.push_back(1);
    for (int x = 2; x <= n; x++) {
        int prev = vecNumOfOperations[x - 1];
        vector<int> mins;
        mins.push_back(prev);
        int min1 = std::numeric_limits<int>::max();
        int min2 = std::numeric_limits<int>::max();
        if (x % 2 == 0) {
            int remain = (x/2);
            min1 = vecNumOfOperations[remain];
            mins.push_back(min1);
        } if (x % 3 == 0) {
            int remain = (x/3);
            min2 = vecNumOfOperations[remain];
            mins.push_back(min2);
        }
        int z = *min_element(mins.begin(), mins.end());
        vecNumOfOperations.push_back(z + 1);
    }

    while (n > 0) {
        sequence.push_back(n);
        if (n%2 != 0 && n%3 != 0) {
            n -= 1;
        } else if (n%2 == 0 && n%3 == 0) {
            n /= 3;
        } else if (n%2 == 0) {
            if (vecNumOfOperations[n - 1] < vecNumOfOperations[n/2]) {
                n -= 1;
            } else {
                n /= 2;
            }
        } else if (n%3 == 0) {
            if (vecNumOfOperations[n - 1] < vecNumOfOperations[n/3]) {
                n -= 1;
            } else {
                n /= 3;
            }
        }
    }
    reverse(sequence.begin(), sequence.end());
    return sequence;
}

int main() {
    int n;
    std::cin >> n;
    vector<int> sequence = optimal_sequence(n);
    std::cout << sequence.size() - 1 << std::endl;
    for (size_t i = 0; i < sequence.size(); ++i) {
        std::cout << sequence[i] << " ";
    }
}


