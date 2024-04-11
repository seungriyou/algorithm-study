import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        
        int[] answer = new int[commands.length];
        
        
        for (int l = 0; l < commands.length; l++) {
            int[] command = commands[l];
            int i = command[0];
            int j = command[1];
            int k = command[2];
            
            // slicing
            int[] sub = Arrays.copyOfRange(array, i - 1, j);
            
            // sort
            Arrays.sort(sub);
            
            // index get
            answer[l] = sub[k - 1];
        }
        
        return answer;
    }
}
