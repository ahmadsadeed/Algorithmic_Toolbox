#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <limits>

using std::vector;
using std::string;
using std::max;
using std::min;
using std::pair;

long long eval(long long a, long long b, char op) {
    if (op == '*') {
        return a * b;
    } else if (op == '+') {
        return a + b;
    } else if (op == '-') {
        return a - b;
    } else {
        assert(0);
    }
}

pair<long long, long long> MinAndMax(int i, int j, std::vector<char> &opK, const std::vector<std::vector<long long>> &minMatrix, const std::vector<std::vector<long long>> &maxMatrix)
{
    pair<long long, long long> p;
    p.first = std::numeric_limits<int>::max();
    p.second = std::numeric_limits<int>::min();

    for (int k = i; k <= j-1; k++) {
        /*
         cout<<"\ni: "<<i<<", j: "<<j<<", k: "<<k<<endl;
         cout << "\nMat: "<<maxMatrix[i][k]<<", op: "<<char(opK[k])<<", and: "<<maxMatrix[k+1][j]<< endl;
         cout << "Mat: "<<maxMatrix[i][k]<<", op: "<<char(opK[k])<<", and: "<<minMatrix[k+1][j]<< endl;
         cout << "Mat: "<<minMatrix[i][k]<<", op: "<<char(opK[k])<<", and: "<<maxMatrix[k+1][j]<< endl;
         cout << "Mat: "<<minMatrix[i][k]<<", op: "<<char(opK[k])<<", and: "<<minMatrix[k+1][j]<< endl;*/

        long long a = eval(maxMatrix[i][k], maxMatrix[k+1][j], opK[k]);
        long long b = eval(maxMatrix[i][k], minMatrix[k+1][j], opK[k]);
        long long c = eval(minMatrix[i][k], maxMatrix[k+1][j], opK[k]);
        long long d = eval(minMatrix[i][k], minMatrix[k+1][j], opK[k]);
        p.first = std::min(p.first, std::min(a, std::min(b, std::min(c ,d))));
        p.second = std::max(p.second, std::max(a, std::max(b, std::max(c ,d))));
        /*
         cout<< "First: "<<p.first<<", Second: "<<p.second<<endl;
         cout<<"\ni: "<<i<<", j: "<<j<<", k: "<<k<<", a: "<<a<<", b: "<<b<<", c: "<<c<<", d: "<<d<<endl;*/
    }
    return p;
}

long long get_maximum_value(const string &exp) {
    // string s = "5-8+7*4-8+9";
    // 200 = (5 − ((8 + 7) × (4 − (8 + 9))))

    // add operators to vector
    vector<char> opK;
    for (int op = 1; op < exp.size(); op+=2) {
        opK.push_back(exp[op]);
    }

    size_t rowCol = (exp.size() + 1) / 2;
    // create the matrix
    std::vector<std::vector<long long>> minMatrix(rowCol, std::vector<long long>(rowCol));
    std::vector<std::vector<long long>> maxMatrix(rowCol, std::vector<long long>(rowCol));
    for (int i = 0, x = 0; i < rowCol; i++) {
        minMatrix[i][i] = (exp[x] - '0');
        maxMatrix[i][i] = (exp[x] - '0');
        x += 2;
    }

    for (int s = 1; s <= (rowCol - 1); s++) {
        for (int i = 0; i < (rowCol - s); i++) {
            int j = i + s;
            pair<long long, long long> pMinMax = MinAndMax(i, j, opK, minMatrix, maxMatrix);
            minMatrix[i][j] = pMinMax.first;
            maxMatrix[i][j] = pMinMax.second;
        }
    }

    /*cout << "\nMin Matrix: " << endl;
     for(auto& row: minMatrix) {for(auto& val: row) std::cout << val << ' ';std::cout << '\n';}
     cout << "\nMax Matrix: " << endl;
     for(auto& row: maxMatrix) {for(auto& val: row) std::cout << val << ' ';std::cout << '\n';}*/

    return maxMatrix[0][rowCol-1];
}

int main() {
    string s;
    std::cin >> s;
    std::cout << get_maximum_value(s) << '\n';
}



