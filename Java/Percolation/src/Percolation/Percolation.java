/**
 * Name: Zhengchao Ni
 * Penn ID: 73173892
 */
package Percolation;

public class Percolation{
	/**
	 * int [][] ground(int n, double p): generate a new board, with 0 and 1.
	 * void seep (int [][] ground, int row): operation, simulate the flowing process.
	 * boolean percolate (int [][] ground): test if the water flows to bottom.
	 * double findProbability(int n): calculate the probability of flowing to the bottom of different arrays.
	 * 
	 */
	
	int [][] ground (int n, double p){
		
		/**
		 * Use the encoding 0 = empty space, 1 = sand grain, 2 = water. 
		 * @param n:  each array is of length n
		 * @param p:  each integer has probability p of being a sand grain,(1-p) of being empty (and dry).
		 * @return:   an array of n arrays of integers.
		 */
		
		// set up a new board.
		int [][] board = new int [n][n];
		
		// initialize every element of board[][]
		// if random number is greater than p, then set 1, else, set 0.
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				double random = Math.random();
				if (random < p)
					board[i][j] = 1;
				else
					board[i][j] = 0;
			}
		}
		return board;
	}
	
	void seep (int [][] ground, int row) {
		
		/**
		 * Simulates water to flow from row into row + 1, modifying the array.
		 * @param ground: the board, a two-dimensional array.
		 * @param row :   row index of the array.
		 * Just a operation, no return.
		 */
		
		// For the first row, if there is a 0, set it to 2.
		for (int i = 0; i < ground.length; i++) {
			if (ground[0][i] == 0) {
				ground [0][i] = 2;
			}
		}
		
		// find a 2 in ground[row], determine whether it could flow down.
		for (int i = 0; i < ground.length; i++) {
			if (ground[row][i] == 2) {
				if (ground[row + 1][i] == 0) {
					ground[row + 1][i] = 2;
					
					// pervade in the ground[row + 1], both directions.
					int j = 1, k = 1; // two indexes, right and left from ground[row + 1][i]
					
					// pervade rightward
					while (j <= ground.length - 1 - i) {
						if (ground[row + 1][i + j] == 0) 
							ground[row + 1][i + j] = 2;
						if (ground[row + 1][i + j] == 1) 
							break;
						j++;
					}
					
					// pervade leftward
					while (k <= i) {
						if (ground[row + 1][i - k] == 0)
							ground[row + 1][i - k] = 2;
						if (ground[row + 1][i - k] == 1)
							break;
						k++;
					}
				}
			}	
		}
	}
	
	boolean percolate (int [][] ground) {
		
		/**
		 * Returns true if, after water has "seeped" as far as it can, water has reached the bottom row,
		 * and false otherwise.
		 */
		
		// once there is a 2 in the bottom, flag = true.
		boolean flag = false;
		for (int i = 0; i < ground.length; i++) {
			if (ground[ground.length - 1][i] == 2) {
				flag = true;
				break;
			}
		}
		return flag;
	}
	
	
	
	double findProbability(int n) {
		
		/**
		 * For an n by n array, determines the packing probability p that causes the array 
		 * to have a 50% probability of water seeping all the way to the bottom.
		 * 
		 * n is the dimension of the array.
		 * 
		 * returns a double p representing the probability.
		 * 
		 * NumOfTrue (Number of times when boolean percolate function returns true).
		 * 
		 * (1) when NumOfTrue oscillate from the half of total_iteration
		 * (i.e. this turn, NumOfTrue > half of total_iteration; next turn, delta decreases, then NumOfTrue < half of total_iteration)
		 * delta begins to change.
		 * 
		 * (2) when delta needs to be changed, it will become 90% of its original value (personal set, other value maybe okay). 
		 * 
		 * (3) after many times of iteration, when delta is proper and NumOfTrue equals to the exact half of total_iteration, end loop.
		 */

		// iteration represents the iteration index, total_ideration represents the total times of iteration.
		// NumOfTrue_last is the value of NumOfTrue in last iteration.
		int  iteration = 1, NumOfTrue = 0, NumOfTrue_last = 0, total_iteration = 30;
		double p = 0.5, delta = 0.05;
		
		while (NumOfTrue != total_iteration/2) {
			NumOfTrue_last = NumOfTrue; // store the NumOfTrue value of last time.	
			
			// reset
			NumOfTrue = 0; 
			iteration = 1;
			
			// iterate for some times, to get NumOfTrue (Number of times when boolean percolate is true).
			while (iteration <= total_iteration) {
				int [][] NewGround = ground(n, p);
				for (int m = 0; m < NewGround.length - 1; m++) {
					seep(NewGround, m);
				}
				if (percolate(NewGround) == true)
					NumOfTrue++;
				iteration++;
			}
			
			// when NumOfTrue is less than half, that means p is large (too much sand). 
			if (NumOfTrue < total_iteration/2) {
				p -= delta;
			}
			
			// when NumOfTrue more than half, that means p is small (too much empty). 
			else if (NumOfTrue > total_iteration/2) {
				p += delta;
			}
			
			// when previous and current NumOfTrue oscillate 
			if ((NumOfTrue_last < total_iteration/2 && NumOfTrue > total_iteration/2) || 
					(NumOfTrue_last > total_iteration/2 && NumOfTrue < total_iteration/2)) {
				delta *= 0.9;
			}
		}
		return p;
	}

	
	public int arraySum(int [][] a) {
		
		/**
		 * This function is used for JUnit Test.
		 * Returns the sum of a given two-dimensional array.
		 * Used for finding the total number of 1 in the generated ground.
		 * Then calculate the probability.
		 */
		
		int sum = 0;
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a.length; j++) {
				sum += a[i][j];
			}
		}
		return sum;
	}
	
	public static void main(String[] args) {
		// Use these methods will somewhat slow down the program (like p.findProbability).
		// if I define those 4 methods as static methods, and use directly in the main function, it will be faster.
		
		int n1 = 50, n2 = 100, n3 = 200;
		double d1, d2, d3;
		Percolation p = new Percolation();
		
		//long startTime = System.currentTimeMillis(); // This 3-line commented code is timing.
		d1 = p.findProbability(n1); // 
		d2 = p.findProbability(n2);
		d3 = p.findProbability(n3);
		//long endTime = System.currentTimeMillis();
		//System.out.println("Operation Time: " + endTime - startTime);
		
		// output format, convert double number into 2-decimal.
		System.out.println("Result: ");
		System.out.println("The Probability of 50*50 : " + String.format("%.2f", d1));
		System.out.println("The Probability of 100*100 : " + String.format("%.2f", d2));
		System.out.println("The Probability of 200*200 : " + String.format("%.2f", d3));
	}
}