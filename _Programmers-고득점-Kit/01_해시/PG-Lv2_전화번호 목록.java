import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> _set = new HashSet<>();
        for (String p : phone_book) {
            _set.add(p);
        }
        
        for (String p : phone_book) {
            StringBuilder prefix = new StringBuilder();
            
            for (char n : p.toCharArray()) {
                prefix.append(n);
                
                if (_set.contains(prefix.toString()) && !p.equals(prefix.toString())) {
                    return false;
                }
            }
        }
        
        return true;
    }
}

class Solution1 {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        
        for (int i = 0; i < phone_book.length - 1; i++) {
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }
        return true;
    }
}
