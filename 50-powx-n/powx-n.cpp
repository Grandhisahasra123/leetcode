class Solution {
public:
    double findPow(double x, long long n) {
        if(n == 0) return 1.0;

        double a = findPow(x, n / 2);
        double ans = a * a;

        if(n % 2 == 1) {
            ans = ans * x;
        }

        return ans;
    }

    double myPow(double x, int n) {
        long long p = n;

        if(p < 0) {
            return 1.0 / findPow(x, -p);
        }

        return findPow(x, p);
    }
};