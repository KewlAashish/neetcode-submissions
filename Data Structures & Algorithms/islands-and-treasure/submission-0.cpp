class Solution {
public:
    int INF = 2147483647;
    vector<pair<int, int>> moves = {{1,0}, {0,1}, {-1,0}, {0,-1}};

    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        queue<pair<int, int>> bfs;

        // Step 1: Push all gates (0s) into queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    bfs.push({i, j});
                }
            }
        }

        // Step 2: Multi-source BFS from all gates
        while (!bfs.empty()) {
            auto [x, y] = bfs.front(); bfs.pop();

            for (auto [dx, dy] : moves) {
                int nx = x + dx, ny = y + dy;
                if (nx >= 0 && ny >= 0 && nx < m && ny < n && grid[nx][ny] == INF) {
                    grid[nx][ny] = grid[x][y] + 1;
                    bfs.push({nx, ny});
                }
            }
        }
    }
};
