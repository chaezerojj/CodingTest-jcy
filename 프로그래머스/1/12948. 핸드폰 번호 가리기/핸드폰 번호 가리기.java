class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String[] nums = phone_number.split("");
        for (int i = 0; i < nums.length; i++) {
            if (i < nums.length - 4) {
                answer += "*";
            } else {
                answer += nums[i];
            }
        }
        
        return answer;
    }
}