// Zhengchao Ni, 73173892
package Fraction;
import java.util.Scanner;

public class FractionCalculator {
	public static void main(String[] args) {
		Fraction f = new Fraction (0, 1);
		while (true) {
			System.out.println(f + "\nPlease input your command!\n");
			
			// use the below two lines to get input in Java.
			Scanner scanner = new Scanner(System.in);
			String operation = scanner.nextLine();
			
			if (operation.equals("a")) {
				f.abs();
			}
			
			else if (operation.equals("c")) {
				f = new Fraction (0, 1);
			}
			
			else if (operation.equals("i")) {
				// use try-catch to avoid exception
				try{
					 f.inverse();
				}
				catch(Exception e) {
					System.out.println("Error! Please think twice before inputting...");
					continue;
				}
			}
			
			else if(operation.startsWith("s")) {
				String sub = operation.substring(2, operation.length());
				int numerator, denominator;
				try{
					// if sub.length() is 1, then it must be a positive integer;
					// if sub.length() is 2, then we should decide whether it begins with a '-';
					if ((sub.length() == 1) || (sub.length() == 2 && sub.startsWith("-"))){
						numerator = Integer.parseInt(sub);
						denominator = 1;
					}
					else {
						String[] sub_result = sub.split("/");
						numerator = Integer.parseInt(sub_result[0].trim());
						denominator = Integer.parseInt(sub_result[1].trim());
					}
				}
				catch(Exception e) {
					System.err.println("Error! Please think twice before inputting...");
					continue;
				}
				
				// use the new fraction to replace
				f = new Fraction(numerator,denominator);
			}
			
			else if (operation.equals("q")) {
				System.out.println("Program ends...\nBye~!");
				break;
			}
			
			else if (operation.startsWith("+")) {
				// allow "27 / 99", use substring(beginIndex, endIndex)
				String add = operation.substring(2, operation.length());
				int numerator, denominator;
				try{
					if ((add.length() == 1) || (add.length() == 2 && add.startsWith("-"))){
						numerator = Integer.parseInt(add);
						denominator = 1;
					}
					else {
						String[] add_result = add.split("/");
						numerator = Integer.parseInt(add_result[0].trim());
						denominator = Integer.parseInt(add_result[1].trim());
					}
				}
				catch(Exception e) {
					System.err.println("Error! Please think twice before inputting...");
					continue;
				}
				Fraction result = new Fraction(numerator,denominator);
				
				// here! must use the new value to replace f!!
				f = f.add(result);
			}
			
			else if (operation.startsWith("-")) {
				String subtract = operation.substring(2, operation.length());
				int numerator, denominator;
				try{
					if ((subtract.length() == 1) || (subtract.length() == 2 && subtract.startsWith("-"))){
						numerator = Integer.parseInt(subtract);
						denominator = 1;
					}
					else {
						String[] subtract_result = subtract.split("/");
						numerator = Integer.parseInt(subtract_result[0].trim());
						denominator = Integer.parseInt(subtract_result[1].trim());
					}
				}
				catch(Exception e) {
					System.err.println("Error! Please think twice before inputting...");
					continue;
				}
				Fraction result = new Fraction(numerator,denominator);
				f = f.subtract(result);
			}
			
			else if (operation.startsWith("*")) {
				String multiply = operation.substring(2, operation.length());
				int numerator, denominator;
				try{
					if ((multiply.length() == 1) || (multiply.length() == 2 && multiply.startsWith("-"))){
						numerator = Integer.parseInt(multiply);
						denominator = 1;
					}
					else {
						String[] multiply_result = multiply.split("/");
						numerator = Integer.parseInt(multiply_result[0].trim());
						denominator = Integer.parseInt(multiply_result[1].trim());
					}
				}
				catch(Exception e) {
					System.err.println("Error! Please think twice before inputting...");
					continue;
				}
				Fraction result = new Fraction(numerator,denominator);
				f = f.multiply(result);
			}
			
			else if (operation.startsWith("/")) {
				String divide = operation.substring(2, operation.length());
				int numerator, denominator;
				try{
					if ((divide.length() == 1) || (divide.length() == 2 && divide.startsWith("-"))){
						numerator = Integer.parseInt(divide);
						denominator = 1;
					}
					else {
						String[] divide_result = divide.split("/");
						numerator = Integer.parseInt(divide_result[0].trim());
						denominator = Integer.parseInt(divide_result[1].trim());
					}
				}
				catch(Exception e) {
					System.err.println("Error! Please think twice before inputting...");
					continue;
				}
				Fraction result = new Fraction(numerator,denominator);
				f = f.divide(result);
			}		
			else {
				continue;
			}
		}
	}
}