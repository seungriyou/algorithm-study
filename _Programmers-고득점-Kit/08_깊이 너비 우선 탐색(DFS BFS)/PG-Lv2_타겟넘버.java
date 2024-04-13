class Solution {
    int dfs(int idx, int val, int[] numbers, int target) {
        // base condition
        if (idx == numbers.length) {
            if (target == val) {
                return 1;
            }
            return 0;
        }

        // recur
        return dfs(idx + 1, val + numbers[idx], numbers, target) + dfs(idx + 1, val - numbers[idx], numbers, target);
    }

    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        answer = dfs(0, 0, numbers, target);
        
        return answer;
    }
}
