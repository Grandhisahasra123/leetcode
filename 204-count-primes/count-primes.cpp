vector<bool>sieve(int n){
    vector<bool>primes(n+1,true);
    primes[0]=false;
    primes[1]=false;
    for(int i=2;i*i<=n;i++){
        if(primes[i]){
            for(int j=i*i;j<=n;j+=i){
                primes[j]=false;
            }
        }
    }
    return primes;
}
class Solution {
public:
    int countPrimes(int n) {
        vector<bool>primes=sieve(n);
        int c=0;
        for(int i=1;i<n;i++){
            if(primes[i]) c++;
        }
        return c;
    }
};