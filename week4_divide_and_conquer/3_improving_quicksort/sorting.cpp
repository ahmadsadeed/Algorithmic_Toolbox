#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;

std::pair<int, int> partition3(vector<int> &a, int l, int r) {
    int x = a[l];
    int second = l, first = l + 1;
    for (int i = l + 1; i <= r; i++) {
        if (a[i] <= x) {
            second++;
            swap(a[i], a[second]);
            if (a[second] < x) {
                swap(a[first], a[second]);
                first++;
            }
        }
    }
    swap(a[l], a[first-1]);
    return {first, second};
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
    if (l >= r) { return; }

    int k = l + rand() % (r - l + 1);
    swap(a[l], a[k]);
    std::pair<int, int> pairReturn = partition3(a, l, r);

    randomized_quick_sort(a, l, pairReturn.first - 1);
    randomized_quick_sort(a, pairReturn.second + 1, r);
}

int main() {
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); ++i) {
        std::cin >> a[i];
    }


    randomized_quick_sort(a, 0, (int)a.size() - 1);
    for (size_t i = 0; i < a.size(); ++i) {
        std::cout << a[i] << ' ';
    }
}



