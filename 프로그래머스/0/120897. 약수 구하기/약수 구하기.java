import java.util.*;
class Solution {
    public int[] solution(int n) {
        int num = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                num++;
            }
        }
        int[] answer = new int[num];
        int a = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                answer[a] = i;
                a++;
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}