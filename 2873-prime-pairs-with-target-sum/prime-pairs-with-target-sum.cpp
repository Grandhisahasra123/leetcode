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
    vector<vector<int>> findPrimePairs(int n) {
        vector<bool>primes=sieve(n);
        vector<vector<int>>ans;
        for(int i=2;i<=n-i;i++){
            if(primes[i] && primes[n-i]){
                ans.push_back({i,n-i});
            }
        }
        return ans;
    }
};