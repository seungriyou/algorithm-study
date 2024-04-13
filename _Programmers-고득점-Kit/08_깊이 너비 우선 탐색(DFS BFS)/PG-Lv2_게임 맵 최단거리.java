import java.util.*;

class Solution {
    int bfs(int n, int m, int[][] maps) {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        int[][] distance = new int[n][m];
        
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        maps[0][0] = 0; // visited
        
        while (!q.isEmpty()) {
            int[] pos = q.poll();
            int r = pos[0];
            int c = pos[1];
            
            // 도달했다면 return
            if (r == n - 1 && c == m - 1) {
                return distance[r][c] + 1;
            }
            
            // 상하좌우 진행
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && maps[nr][nc] == 1) {
                    q.offer(new int[]{nr, nc});
                    maps[nr][nc] = 0; // visited
                    distance[nr][nc] = distance[r][c] + 1; // distance
                }
            }
        }
        
        // 도달하지 못했다면 -1 return
        return -1;
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        int n = maps.length;
        int m = maps[0].length;
        
        answer = bfs(n, m, maps);
        
        return answer;
    }
}
