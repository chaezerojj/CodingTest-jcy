import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int s = sc.nextInt();
        
        if (s == 0 && t >= 12 && t <= 16) {
            System.out.println(320);
        } else {
            System.out.println(280);
        }
    }
}