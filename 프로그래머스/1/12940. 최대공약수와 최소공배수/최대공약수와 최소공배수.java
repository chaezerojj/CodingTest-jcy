class Solution {
    int gcd(int a, int b) {
        int k;
        while (b > 0) {
            k = a % b;
            a = b;
            b = k;
        }
        return a;
    }
    
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        if (n < m) {
            int temp = n;
            n = m;
            m = temp;
        }
        answer[0] = gcd(n, m);
        answer[1] = n * m / answer[0];
        return answer;
    }
}