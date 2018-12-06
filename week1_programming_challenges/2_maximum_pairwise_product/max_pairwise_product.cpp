#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;

int64_t MaxPairwiseProductSorted(std::vector<int>& numbers) {
    sort(numbers.begin(), numbers.end());
    size_t size = numbers.size();

    int64_t first = numbers[size - 1];
    int64_t second = numbers[size - 2];

    return first * second;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    int64_t result2 = MaxPairwiseProductSorted(numbers);
    std::cout << result2 << "\n";
    return 0;
}



//#include <iostream>
//#include <vector>
//#include <algorithm>
//#include <string>
//#include <iomanip>
//#include <cctype>
//#include <cstdlib>
//#include <fstream>
//
//using namespace std;
//
//static const auto _fast=[](){ios::sync_with_stdio(0);cin.tie(0);return nullptr;}();
//
//class Solution {
//public:
//    string convert(string s, int numRows) {
//
//
//        return "s";
//    }
//};
//
//int main()
//{
//
//
//
//
//    cout << endl;
//    return 0;
//}
//
//
//

