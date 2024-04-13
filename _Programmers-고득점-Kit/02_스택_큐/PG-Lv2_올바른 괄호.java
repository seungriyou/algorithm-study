import java.util.*;

class Solution {
    boolean solution(String s) {
        
        Stack<Character> stack = new Stack<>();
        for (char p : s.toCharArray()) {
            if (p == '(') {
                stack.push(p);
            } else if (!stack.empty()) {
                stack.pop();
            } else {
                return false;
            }
        }

//         if (stack.empty()) {
//             return true;
//         } else {
//             return false;
//         }
        
        return (stack.empty() ? true : false);
        
    }
}
