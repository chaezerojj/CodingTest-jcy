import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String str = "";
        
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            
            if (Character.isLowerCase(c)){
                str += Character.toUpperCase(c);
            } else {
                str += Character.toLowerCase(c);
            }
        }
        sc.close();
        System.out.println(str);
    }
}