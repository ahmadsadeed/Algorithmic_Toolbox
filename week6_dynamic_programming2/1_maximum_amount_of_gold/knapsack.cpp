#include <iostream>
#include <vector>

using std::vector;

int optimal_weight(int capacity, const vector<int> &data) {
    size_t col = capacity + 1;
    size_t row = data.size() + 1;

    std::vector<std::vector<int>> matrix(row, std::vector<int>(col));

    for (int r = 1; r < row; r++) {
        for (int c = 1; c < col; c++) {
            matrix[r][c] = matrix[r-1][c];
            if (data[r-1] <= c) {
                int val = ( matrix[r-1][c - data[r-1]] ) + data[r-1];
                if (matrix[r][c] < val) {
                    matrix[r][c] = val;
                }
            }
        }
    }

    //    for(auto& row: matrix) {for(auto& val: row) std::cout << val << ' ';std::cout << '\n';}

    return matrix[row-1][col-1];
}

int main() {
    int n;
    int weight;
    std::cin >> weight >> n;

    vector<int> data(n);
    for (int i = 0; i < n; i++) {
        std::cin >> data[i];
    }

    int optimal_value = optimal_weight(weight, data);
    std::cout << optimal_value << std::endl;
}


