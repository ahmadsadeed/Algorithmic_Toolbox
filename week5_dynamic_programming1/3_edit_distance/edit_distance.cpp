#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <string>

using std::string;

int edit_distance(const string &str1, const string &str2) {
    size_t lenStr1 = str1.size() + 1;
    size_t lenStr2 = str2.size() + 1;

    std::vector<std::vector<int>> matrix;
    for (int i = 0; i < lenStr1; i++) {
        std::vector<int> v;
        if (i == 0) {
            for (int j = 0; j < lenStr2; j++) {
                v.push_back(j);
            }
            matrix.push_back(v);
        } else {
            v.push_back(i);
            for (int j = 1; j < lenStr2; j++) {
                v.push_back(0);
            }
            matrix.push_back(v);
        }
    }


    for (int y = 1; y < lenStr2; y++) {
        for (int x = 1; x < lenStr1; x++) {
            int insertion = (matrix[x][y-1]) + 1;
            int deletion = (matrix[x-1][y]) + 1;
            int match = matrix[x-1][y-1];
            int mismatch = (matrix[x-1][y-1]) + 1;
            if (str1[x-1] == str2[y-1]) {
                matrix[x][y] = std::min(insertion, std::min(deletion, match));
            } else {
                matrix[x][y] = std::min(insertion, std::min(deletion, mismatch));
            }
        }
    }

    //    std::cout << std::endl;
    //    for (int x = 0; x < lenStr1; x++) {
    //        for (int y = 0; y < lenStr2; y++) {
    //            std::cout << matrix[x][y] << " ";
    //        }
    //        std::cout << std::endl;
    //    }
    //    std::cout << "\nInt: " << matrix[lenStr1-1][lenStr2-1] << std::endl;

    return matrix[lenStr1-1][lenStr2-1];
}

int main() {
    string str1;
    string str2;
    std::cin >> str1 >> str2;
    std::cout << edit_distance(str1, str2) << std::endl;
    return 0;
}



