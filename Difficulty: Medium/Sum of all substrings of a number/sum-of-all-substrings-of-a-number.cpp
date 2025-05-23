class Solution {
  public:
    int sumSubstrings(string &s) {
        // code here
        long long int answ=0;
        int n=s.size();
        for(int i=0; i<n; i++){
            int x=s[i]-'0';
            answ+=x;
            for(int j=i+1; j<n; j++){
                x= x*10+ (s[j]-'0');
                answ+=x;
            }
        }
        return answ;
    }
};