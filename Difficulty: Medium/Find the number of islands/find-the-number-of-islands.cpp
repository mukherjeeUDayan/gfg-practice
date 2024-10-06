//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
      int n,m, answ=0, dxy[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
      bool valid(int x, int y){
          return x >= 0 && x < n && y >= 0 && y < m;
      };
        // Function to find the number of islands.
    int numIslands(vector<vector<char>>& grid) {
        // Code here
        n=grid.size();
        m= grid[0].size();
        answ=0;
        bool v[n+1][m+1];
        memset(v,false, sizeof(v));
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j] == '1' && !v[i][j]){
                    queue<pair<int,int>> q;
                    answ++;
                    q.push({i,j});
                    v[i][j] = true;
                    while(!q.empty()){
                        int k= q.size();
                        while(k--){
                            pair<int,int> p= q.front();
                            q.pop();
                            int a= p.first, b=p.second;
                            for(int k=0; k<8; k++){
                                int x= a + dxy[k][0], y= b+dxy[k][1];
                                if(valid(x,y) && grid[x][y]== '1' && !v[x][y]){
                                    q.push({x,y});
                                    v[x][y]= true;
                                }
                            }
                        }
                    }
                }
            }
        }
        return answ;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends