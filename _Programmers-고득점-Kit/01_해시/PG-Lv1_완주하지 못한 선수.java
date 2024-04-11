import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {

        // participant 로 counter 만들기
        Map<String, Integer> counter = new HashMap<>();
        for (String name : participant) {
            counter.put(name, counter.getOrDefault(name, 0) + 1);
        }
        
        // completion 돌면서 counter 값 줄이기 & 0 되면 remove
        for (String name : completion) {
            counter.put(name, counter.get(name) - 1);
        }
        
        // counter에 남아있는 entry에서 name 얻기
        String answer = "";
        for (String key : counter.keySet()) {
            if (counter.get(key) != 0) {
                answer = key;
                break;
            }
        }
        
        return answer;
    }
}
