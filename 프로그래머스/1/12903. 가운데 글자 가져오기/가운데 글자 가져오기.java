class Solution {
    public String solution(String s) {
        String answer = "";
        int index = s.length() / 2;
        answer = s.length() % 2 == 0 ?
            s.substring(index - 1, index + 1) : s. substring(index, index + 1);
        return answer;
    }
}