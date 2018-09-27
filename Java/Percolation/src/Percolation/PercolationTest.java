/**
 * Name: Zhengchao Ni
 * Penn ID: 73173892
 */
package Percolation;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.*;

class PercolationTest {
	
	// Create a new object.
	Percolation p;
	
	@BeforeEach
	public void setUp(){
		p = new Percolation();
	}

	@Test
	void testGround() {
		
		/**
		 * Use the arraySum method in Percolation.java to compute the sum of the two-dimension array.
		 * Use the result to further compute the probability. 
		 */
		
		int [][] ground_test1;
		int num1; // compute the sum.
		int n1 = 50; 
		double p1 = 0.5;
		ground_test1 = p.ground(n1, p1);
		num1 = p.arraySum(ground_test1);
		assertTrue((Math.abs((double) num1/(n1 * n1) - p1)) <= 0.03); 
		// Here, if I change 0.03 to 0.02, among about 30 tests will exist one failure.
		// I tested 30 times when 0.02, encountered 1 failure.
		// Then I changed to 0.25, more than 50 tests existing a failure.
		// So, I finally set 0.03, I tested over 100 tests, no failure.
		
		int [][] ground_test2;
		int num2;
		int n2 = 100; 
		double p2 = 0.4;
		ground_test2 = p.ground(n2, p2);
		num2 = p.arraySum(ground_test2);
		assertTrue((Math.abs((double) num2/(n2 * n2) - p2)) <= 0.03);
	}

	@Test
	void testSeep() {
		
		/**
		 * test each step, test whether 2 is correctly flowed. 
		 */
		
		// Just use a 4 dimensional array to test.
		int [][] ground_test1 = {{1,0,0,1},{0,0,1,1},{0,1,0,0},{0,0,1,1}}; // original.
		
		// seep row 0. The water (2) must flow to row + 1, that is the first 2 row must be filled with water.
		p.seep(ground_test1, 0);
		int [][] ground_test2 = {{1,2,2,1},{2,2,1,1},{0,1,0,0},{0,0,1,1}};
		for (int i = 0; i < ground_test1.length; i++ ) {
			for (int j = 0; j < ground_test1.length; j++) {
				assertEquals(ground_test1[i][j], ground_test2[i][j]);
			}
		}
		
		// continue to flow, the first 3 lines must be full of water.
		p.seep(ground_test1, 1);
		int [][] ground_test3 = {{1,2,2,1},{2,2,1,1},{2,1,0,0},{0,0,1,1}};
		for (int i = 0; i < ground_test1.length; i++ ) {
			for (int j = 0; j < ground_test1.length; j++) {
				assertEquals(ground_test1[i][j], ground_test3[i][j]);
			}
		}
		
		p.seep(ground_test1, 2);
		int [][] ground_test4 = {{1,2,2,1},{2,2,1,1},{2,1,0,0},{2,2,1,1}};
		for (int i = 0; i < ground_test1.length; i++ ) {
			for (int j = 0; j < ground_test1.length; j++) {
				assertEquals(ground_test1[i][j], ground_test4[i][j]);
			}
		}
	}

	@Test
	void testPercolate() {
		
		/*
		 * Just test if there is a 2 in the bottom. 
		 */
		
		int [][] ground_test1 = {{1,2,2,1},{2,2,1,1},{2,1,0,0},{0,0,1,1}};
		int [][] ground_test2 = {{1,2,2,1},{2,2,1,1},{2,1,0,0},{2,2,1,1}};
		assertTrue(p.percolate(ground_test1) == false); // It seems there is no assertFalse statement in Java.
		assertTrue(p.percolate(ground_test2));
	}

}
