package battleship;

import java.util.Scanner;


public class BattleshipGame {
	
	/**
	 * Function of the whole game.
	 * Get input from the user, display the shotsFired and hitCount number in each step,
	 * hit or miss information, specific ship-type which has been sunk,
	 * along with the current ocean.
	 */
	public void game(){
		Ocean ocean = new Ocean();
		System.out.println("");
		System.out.println("********************************");
		System.out.println("* Welcome to Battleship Game!! *");
		System.out.println("********************************");
		System.out.println("");
		ocean.placeAllShipsRandomly();
		
		// Print the original ocean.
		System.out.println("");
		System.out.println("--$ Original Ocean $--");
		System.out.println("");
		ocean.print();
		
		/* Ship Distribution Map
		System.out.println("  0 1 2 3 4 5 6 7 8 9");
		for (int i = 0; i < 10; i++) {
			System.out.print(i + " ");
			for (int j = 0; j < 10; j++) {
				System.out.print(ocean.ocean.ships[i][j] + " ");
			}
			System.out.println("");
		}*/
		
		Scanner scanner = new Scanner(System.in);
		
		while (ocean.ocean.isGameOver() == false) {
			
			int m = 0, n = 0;
			boolean flag1 = true;
			
			// Insist on getting a proper row number input from the user. 
			while (flag1) {
				try {
					System.out.println("Please input a row number...");
					m = Integer.parseInt(scanner.nextLine());
					if (m < 0 || m > 9) {
						System.out.println("Warning!! Please input a number between 0 and 9...");
						continue;
					}
					flag1 = false;
				}
				catch(Exception e) {
					System.out.println("Wrong Input!! Please try again!");
				}
			}
			
			boolean flag2 = true;
			
			// Insist on getting a proper column number input from the user.
			while (flag2) {
				try {
					System.out.println("Please input a column number...");
					n = Integer.parseInt(scanner.nextLine());
					if (n < 0 || n > 9) {
						System.out.println("Warning!! Please input a number between 0 and 9...");
						continue;
						
					}
					flag2 = false;
				}
				catch(Exception e) {
					System.out.println("Wrong Input!! Please try again!");
				}
			}
		
			// If the user just hit somewhere that is already hit (does no good), then output nothing
			if (ocean.ocean.ships[m][n].isSunk()) {
				
				// Real Shoot!
				ocean.ocean.ships[m][n].shootAt(m, n);
				
				// Counting, shotsFired and hitCount.
				ocean.shootAt(m, n);
			}
			else {
				ocean.ocean.ships[m][n].shootAt(m, n);
				ocean.shootAt(m, n);
				if (ocean.ocean.ships[m][n].isSunk()) {
					System.out.println("==============================");
					System.out.println("You just sank a " + ocean.ocean.ships[m][n].getShipType() + "!!!");
					System.out.println("==============================");
				}
			}
			
			// hit or miss.
			if (ocean.isOccupied(m, n)) System.out.println("\n---# hit #---\n");
			else System.out.println("\n~~~miss~~~\n");
			
			// Display the scores.
			System.out.println("ShotsFired: " + ocean.getShotsFired());
			System.out.println("HitCount: " + ocean.getHitCount());
			
			// Display current ocean.
			System.out.println("");
			System.out.println("--$ Current Ocean $--");
			System.out.println("");
			ocean.ocean.print();
		}
		
		System.out.println("");
		System.out.println("***************");
		System.out.println("* Game Over!! *");
		System.out.println("***************");
		System.out.println("");
		
		System.out.println("============================");
		System.out.println("Your final score is " + ocean.shotsFired + ".");
		System.out.println("============================");
		System.out.println("");
	}
	
	public static void main(String[] args) {
		
		BattleshipGame battleshipgame = new BattleshipGame();
		battleshipgame.game();
		Scanner scanner = new Scanner(System.in);
		
		boolean input = true;
		// Insist on getting an proper input from the user.
		while(input) {
			System.out.println("Do you want to play again?...");
			System.out.println("Press Y to continue, press Q to exit.");
			String user_input = scanner.nextLine(); 
			if (user_input.equals("Y") || user_input.equals("y")) {
				battleshipgame.game();
				continue;
			}
			else if (user_input.equals("Q") || user_input.equals("q")){
				input = false;
				break;
			}
			else {
				continue;
			}
		}
		scanner.close();
	}
}

