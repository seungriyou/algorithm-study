import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        
        // 1. lost와 reserve 모두 교집합을 제거 **
        Set<Integer> _lost = new HashSet<>();
        for (int l : lost) {
            _lost.add(l);
        }
        
        Set<Integer> _reserve = new HashSet<>();
        for (int r : reserve) {
            if (_lost.contains(r)) {
                _lost.remove(r);
            } else {
                _reserve.add(r);
            }
        }
        
        // 2. reserve를 기준으로, 빌려줄 수 있는 사람이 lost에 존재하는지 확인 후 있으면 제거
        for (int r : _reserve) {
            if (_lost.contains(r - 1)) {
                _lost.remove(r - 1);
            } else if (_lost.contains(r + 1)) {
                _lost.remove(r + 1);
            }
        }
        
        // 3. 전체 길이 - lost의 원소 개수 반환
        return n - _lost.size();
    }
}
