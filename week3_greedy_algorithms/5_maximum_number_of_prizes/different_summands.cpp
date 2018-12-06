#include <iostream>
#include <vector>

using std::vector;

vector<int> optimal_summands(int n) {
    vector<int> summands;
    int remaining = n;

    for (int x = 1; x <= n; x++) {
        if (remaining >= x) {
            if ((remaining - x) > x ) {
                summands.push_back(x);
                remaining -= x;
            } else {
                summands.push_back(remaining);
                remaining = 0;
            }
        } else {
            break;
        }
    }
    return summands;
}

int main() {
    int n;
    std::cin >> n;
    vector<int> summands = optimal_summands(n);
    std::cout << summands.size() << '\n';
    for (size_t i = 0; i < summands.size(); ++i) {
        std::cout << summands[i] << ' ';
    }

}



