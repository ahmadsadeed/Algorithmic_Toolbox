#include <iostream>

int get_change(int m) {
    int a = (m / 4) + ((m%4) / 3) + ((m%4) % 3);
    int b = ((m / 4)-1) + (m-((m / 4)-1)*4) / 3 + (m-((m / 4)-1)*4) % 3;
    return ((a>b) ? b : a);
}

int main() {
    int m;
    std::cin >> m;
    std::cout << get_change(m) << '\n';
}


