import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int[][] patterns = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        
        int[] lens = {
            patterns[0].length,
            patterns[1].length,
            patterns[2].length
        };
        
        int[] scores = new int[3];
        
        
        for (int i = 0; i < answers.length; i++) {
            int answer = answers[i];
            
            for (int j = 0; j < 3; j++) {
                if (answer == patterns[j][i % lens[j]]) {
                    scores[j] += 1;
                }
            }
        }
        
        int max_score = Arrays.stream(scores).max().getAsInt();
        List<Integer> res = new ArrayList<>();
        
        for (int i = 0; i < scores.length; i++) {
            if (max_score == scores[i]) {
                res.add(i + 1);
            }
        }
        
        return res.stream().mapToInt(i -> i).toArray();
    }
}
