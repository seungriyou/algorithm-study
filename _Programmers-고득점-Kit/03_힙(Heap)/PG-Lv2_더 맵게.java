import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> _scoville = new PriorityQueue<>();
        for (int s : scoville) {
            _scoville.add(s);
        }
        
        if (_scoville.peek() >= K) {
            return answer;
        }
        
        while (_scoville.size() >= 2) {
            int first = _scoville.poll();
            int second = _scoville.poll();
            int new_scoville = first + (second * 2);
            
            _scoville.add(new_scoville);
            
            answer++;
            
            if (_scoville.peek() >= K) {
                return answer;
            }
        }
        
        return -1;
    }
}
