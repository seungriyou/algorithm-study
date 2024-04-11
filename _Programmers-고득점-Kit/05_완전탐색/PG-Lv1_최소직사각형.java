class Solution {
    public int solution(int[][] sizes) {
        int longer = 0;
        int shorter = 0;
        
        for (int[] size : sizes) {
            if (size[0] < size[1]) {
                shorter = Math.max(shorter, size[0]);
                longer = Math.max(longer, size[1]);
            } else {
                shorter = Math.max(shorter, size[1]);
                longer = Math.max(longer, size[0]);
            }
        }
        
        return longer * shorter;
    }
}
