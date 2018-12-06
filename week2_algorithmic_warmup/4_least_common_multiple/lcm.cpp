#include <iostream>

using namespace std;

//long long lcm_naive(int a, int b) {
//    for (long l = 1; l <= (long long) a * b; ++l)
//        if (l % a == 0 && l % b == 0)
//            return l;
//
//    return (long long) a * b;
//}
int gcd_fast(int a, int b) {
    int iBig = max(a, b);
    int iSmall = min(a, b);

    int iSmallCopy = iBig % iSmall;

    while (iSmallCopy != 0) {
        iBig = iSmall;
        iSmall = iSmallCopy;
        iSmallCopy = iBig % iSmall;
    }
    return iSmall;
}

long long lcm_fast(int a, int b) {
    int gcd = gcd_fast(a, b);

    return ((long long) a * b)/gcd;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << lcm_fast(a, b) << std::endl;
    return 0;
}


