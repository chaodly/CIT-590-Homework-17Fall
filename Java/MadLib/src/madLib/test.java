package madLib;
import java.util.Random;

public class test{
	public int reverse(int x) {
        int temp, y = 0;
        
        while (x != 0){
            temp = x % 10;
            x = x / 10;
            y = y * 10 + temp;
        }
        return y;
    }

	public static void main(String[] args) {
		String s1 = "Zhengchao";
		String s2 = "Ni";
		System.out.println(s1.hashCode());
		System.out.println(s2.hashCode() - s1.hashCode());
		
	}
}