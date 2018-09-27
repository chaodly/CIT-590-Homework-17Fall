// Zhengchao Ni, 73173892
package Fraction;

public class Fraction{
	// attributes
	private int numerator;
	private int denominator;
	
	// gcd function, which will be used for normalization
	public int gcd(int a, int b) {
		//Compute greatest common divisor of a and b.
		int r;
		while (b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
	
	//constructors
	public Fraction(int numerator, int denominator) {
		if (denominator == 0) {
			throw new IllegalArgumentException("Error: Denominator cannot be zero!!");
		}
		int gcd_number;
		gcd_number = gcd(numerator, denominator);
		numerator = numerator / gcd_number;
		denominator = denominator / gcd_number;
		//normalization
		if (denominator < 0) {
			// whether numerator is positive or negative, 
			// when denominator < 0, they both need to change.
			numerator = -numerator; denominator = -denominator;
		}
		this.numerator = numerator;
		this.denominator = denominator;
	}
	
	public Fraction(int wholeNumber) {
		// set the default denominator = 1.
		this.numerator = wholeNumber;
		this.denominator = 1;
	}
	
	public Fraction(String fraction) {
		// first of all, split the string into two integers.
		String[] fraction_parts = fraction.split("/");
		String part1 = fraction_parts[0].trim(); 
		String part2 = fraction_parts[1].trim(); 
		int numerator =Integer.parseInt(part1);
		int denominator =Integer.parseInt(part2);
		
		// normalization
		if (denominator < 0) {
			// whether numerator is positive or negative, 
			// when denominator < 0, they both need to change.
			numerator = -numerator; denominator = -denominator;
		}
		int gcd_number;
		gcd_number = gcd(numerator, denominator);
		numerator = numerator / gcd_number;
		denominator = denominator / gcd_number;
		this.numerator = numerator;
		this.denominator = denominator;
	}
	
	public Fraction add(Fraction f) {
		// return a new Fraction object, must pay attention in FractionCalculator!
		int numerator =  this.numerator * f.denominator + this.denominator * f.numerator;
		int denominator = this.denominator * f.denominator;
		return new Fraction(numerator, denominator);
	}
	
	public Fraction subtract(Fraction f) {
		int numerator =  this.numerator * f.denominator - this.denominator * f.numerator;
		int denominator = this.denominator * f.denominator;
		return new Fraction(numerator, denominator);
	}
	
	public Fraction multiply(Fraction f) {
		int numerator =  this.numerator * f.numerator;
		int denominator = this.denominator * f.denominator;
		return new Fraction(numerator, denominator);
	}
	
	public Fraction divide(Fraction f) {
		int numerator =  this.numerator * f.denominator ;
		int denominator = this.denominator * f.numerator;
		return new Fraction(numerator, denominator);
	}
	
	public Fraction abs() {
		if (this.numerator > 0 && this.denominator < 0)
			this.denominator = -this.denominator;
		else if (this.numerator < 0 && this.denominator > 0)
			this.numerator = -this.numerator;
		else if (this.numerator < 0 && this.denominator < 0) {
			this.numerator = -this.numerator; this.denominator = -this.denominator;
		}
		return new Fraction(this.numerator, this.denominator);
	}
	
	public Fraction negate() {
		// if denominator is negative, then change the denominator first
		if (this.denominator < 0){
			this.denominator = -this.denominator;
		}
		if (this.denominator > 0) {
			this.numerator = -this.numerator;
		}
		return new Fraction(this.numerator, this.denominator);
	}
	
	public Fraction inverse() {
		//use a temporary variable to store
		int temp;
		if (this.numerator > 0) {
			temp = this.numerator;
			this.numerator = this.denominator;
			this.denominator = temp;
		}
		if (this.numerator < 0) {
			temp = this.numerator;
			this.numerator = -this.denominator;
			this.denominator = -temp;
		}
		return new Fraction(this.numerator, this.denominator);
	}
	
	public int compareTo(Fraction f) {
		// calculate 'this - f', if positive, then this > f; if negative, then this < f;
		Fraction value = new Fraction(numerator, denominator);
		value.numerator =  this.numerator * f.denominator - this.denominator * f.numerator;
		value.denominator = this.denominator * f.denominator;
		if (value.numerator > 0)
			return 1;
		else if (value.numerator < 0)
			return -1;
		return 0;
	}
	
	public String toString(){
		String out;
		if (this.denominator == 1)
			out = this.numerator + "";
		else 
			out = this.numerator + "/" + this.denominator;
		
		// when numerator is 0, output should be 0/1...
		if (this.numerator == 0)
			out ="0/1";
		return out;
	}
}