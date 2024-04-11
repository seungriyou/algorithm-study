import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Stack<Integer> stack = new Stack<>();
        
        for (int a : arr) {
            // stack이 비어있거나, stack의 top이 a와 다르면 add
            if (stack.empty() || stack.peek() != a) {
                stack.push(a);
            }
        }
        
        int[] answer = stack.stream().mapToInt(i -> i).toArray();

        return answer;
    }
}
