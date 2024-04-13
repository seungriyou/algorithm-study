import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        // days 모으기
        int[] days = new int[progresses.length];
        
        for (int i = 0; i < progresses.length; i++) {
            days[i] = (int) Math.ceil((float)(100 - progresses[i]) / (float)speeds[i]);
        }
        
        // stack 사용
        Stack<Integer> stack = new Stack<>();
        for (int day : days) {
            if (stack.empty() || stack.peek() < day) {
                stack.add(day);
                answer.add(1);
            } else {
                int idx = answer.size() - 1;
                answer.set(idx, answer.get(idx) + 1);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
