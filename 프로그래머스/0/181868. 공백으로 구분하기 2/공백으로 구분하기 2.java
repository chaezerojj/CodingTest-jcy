class Solution {
    public String[] solution(String my_string) {
        String[] answer = my_string.trim().split("\\s+");
        // \\s+ -> 하나 이상의 공백
        return answer;
    }
}