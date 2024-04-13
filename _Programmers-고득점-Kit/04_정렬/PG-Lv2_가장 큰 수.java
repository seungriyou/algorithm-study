import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        List<String> lst = new ArrayList<>();
        for (int num : numbers) {
            lst.add(Integer.toString(num));
        }
        
        lst.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
//                 StringBuilder t1 = new StringBuilder();
//                 StringBuilder t2 = new StringBuilder();
//                 t1.append(o1);
//                 t1.append(o2);
//                 t2.append(o2);
//                 t2.append(o1);
                
//                 int n1 = Integer.parseInt(t1.toString());
//                 int n2 = Integer.parseInt(t2.toString());
                
                int n1 = Integer.parseInt(o1 + o2);
                int n2 = Integer.parseInt(o2 + o1);
                
                if (n1 > n2) {
                    return -1;
                } else if (n1 < n2) {
                    return 1;
                } else {
                    return 0;
                }
            }
        });
        
        StringBuilder sb = new StringBuilder();
        for (String n : lst) {
            sb.append(n);
        }
        answer = sb.toString();
        
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}
