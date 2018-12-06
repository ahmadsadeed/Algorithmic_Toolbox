#include <iostream>

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int fibonacci_last_digit_fast(int n) {
    // write your code here
    if (n <= 1)
        return n;
    int array[n];
    array[0] = 0;
    array[1] = 1;

    for (int i = 2; i <= n; i++) {
        array[i] = (array[i - 1] + array[i - 2]) % 10;
    }

    return array[n];
}

int main() {
    int n;
    std::cin >> n;
    int c = fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
}

