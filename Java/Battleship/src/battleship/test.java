package battleship;
import java.util.*;
public class test {

	public static void main(String[] args) {
		
		Object[] things = new Object[100];
		things[1] = 5;
		things[2] = Character.MAX_VALUE;
		for (int i = 0; i < things.length; i++) {
			System.out.println(things[i]);
		}
		int a = ((Integer)things[2]).intValue();
		System.out.println("fuckyou");
		System.out.println(a);
	}

}
