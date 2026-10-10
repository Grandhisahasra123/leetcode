int gcd(int a, int b){
    if(b==0) return a;
    else return gcd(b,a%b);
}
int countFactors(int n) {
    int cnt = 0;
    for(int i = 1; i * i <= n; i++) {
        if(n % i == 0) {
            if(i == n / i) {
                cnt++;
            }
            else {
                cnt += 2;
            }
        }
    }
    return cnt;
}
class Solution {
public:
    int commonFactors(int a, int b) {
        int x=gcd(a,b);
        return countFactors(x);
    }
};