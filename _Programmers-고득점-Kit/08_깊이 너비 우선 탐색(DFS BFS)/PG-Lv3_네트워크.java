import java.util.*;


class Solution {
    void bfs(int i, boolean[] visited, int[][] computers, int n) {
        // queue 만들기
        Queue<Integer> q = new LinkedList<>();
        q.offer(i);
        // visited 처리
        visited[i] = true;
        
        while (!q.isEmpty()) {
            int u = q.poll();
            
            for (int v = 0; v < n; v++) {
                if (!visited[v] && computers[u][v] == 1) {
                    q.offer(v);
                    visited[v] = true;
                }
            }
        }
    }
    
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, visited, computers, n);
                answer++;
            }
        }
        
        return answer;
    }
}

class Solution_dfs {
    void dfs(int u, boolean[] visited, int[][] computers, int n) {
        visited[u] = true;
        
        for (int v = 0; v < n; v++) {
            if (!visited[v] && computers[u][v] == 1) {
                dfs(v, visited, computers, n);
            }
        }
    }
    
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, visited, computers, n);
                answer++;
            }
        }
        
        return answer;
    }
}
