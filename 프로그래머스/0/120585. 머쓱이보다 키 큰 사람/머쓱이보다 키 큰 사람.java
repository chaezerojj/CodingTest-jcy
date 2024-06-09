class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        if ((height >= 1 && height <= 200) && (array.length >= 1 && array.length <= 100)) {
            for (int i = 0; i < array.length; i++) {
                if(height < array[i]) {
                    answer++;
                }
            }
        }
        return answer;
    }
}