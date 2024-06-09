class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long p = 0;
        for (int i = 1; i <= count; i++) {
            p += price * i;
        }
        answer = (p - money) > 0 ? p - money : 0;
        return answer;
    }
}