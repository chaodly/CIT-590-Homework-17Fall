package battleship;

import java.util.Random;

public class Ocean {
	
	// Instance Variables
	Ship[][] ships = new Ship[10][10];
	
	// The total number of shots fired by the user.
	int shotsFired;
	
	// The number of times a shot hit a ship. 
	// If the user shoots the same part of a ship more than once, every hit is counted, 
	// even though the additional "hits" don't do the user any good.
	int hitCount;
	
	// Constructor
	Ocean() {
		shotsFired = 0;
		hitCount = 0;
		for (int i = 0; i < ships.length; i++) {
			for (int j = 0; j < ships.length; j++) {
				ships[i][j] = new EmptySea();
				
				// Should Set!!
				ships[i][j].setBowRow(i);
				ships[i][j].setBowColumn(j);
			}
		}
	}
	
	Ocean ocean;

	void placeAllShipsRandomly() {
		ocean = new Ocean();
		
		Battleship battleship = new Battleship();
		Cruiser cruiser = new Cruiser();
		Destroyer destroyer = new Destroyer();
		Submarine submarine = new Submarine();
		
		Random random_num = new Random();
		
		int row = random_num.nextInt(10);
		int column = random_num.nextInt(10);
		
		boolean horizontal  = random_num.nextInt(2) > 0 ? true : false;
		
		int battleship_num = 0;
		
		// if oktoPlaceShipAt, then ok, if not, while loop to find an okay place.
		while (battleship_num < 1) {
			if (battleship.okToPlaceShipAt(row, column, horizontal, ocean)) {
				battleship.placeShipAt(row, column, horizontal, ocean);

				battleship_num++;
			}
			else {
				row = random_num.nextInt(10);
				column = random_num.nextInt(10);
				continue;
			}
		}
		
		int cruiser_num = 0;
		while(cruiser_num < 2) {
			horizontal  = random_num.nextInt(2) > 0 ? true : false;
			if (cruiser.okToPlaceShipAt(row, column, horizontal, ocean)) {
				cruiser.placeShipAt(row, column, horizontal, ocean);

				cruiser_num++;
				cruiser = new Cruiser();
			}
			else {
				row = random_num.nextInt(10);
				column = random_num.nextInt(10);
				continue;
			}
		}
		
		int destroyer_num = 0;
		while(destroyer_num < 3) {
			horizontal  = random_num.nextInt(2) > 0 ? true :false;
			if (destroyer.okToPlaceShipAt(row, column, horizontal, ocean)) {
				destroyer.placeShipAt(row, column, horizontal, ocean);
				
				destroyer_num++;
				destroyer = new Destroyer();
			}
			else {
				row = random_num.nextInt(10);
				column = random_num.nextInt(10);
				continue;
			}
		}
		
		int submarine_num = 0;
		while(submarine_num < 4) {
			if (submarine.okToPlaceShipAt(row, column, horizontal, ocean)) {
				submarine.placeShipAt(row, column, horizontal, ocean);

				submarine_num++;
				submarine = new Submarine();
			}
			else {
				row = random_num.nextInt(10);
				column = random_num.nextInt(10);
				continue;
			}
		}
		
	}
	
	boolean isOccupied(int row, int column) {
		
		// once found somewhere with no "-", then occupied.
		if (ocean.ships[row][column].toString() != "-") {
			return true;
		}
		return false;
	}
	
	boolean shootAt(int row, int column) {
		
		//counting, each time calling this function, shotsFired++.
		shotsFired++;
		
		// If hit some ship, then hitCount++;
		if (ocean.ships[row][column].getShipType().equals("") == false) {
			hitCount++;
			return true;
		}
		return false;
	}
	
	int getShotsFired() {
		return shotsFired;
	}
	
	int getHitCount() {
		return hitCount;
	}
	
	boolean isGameOver() {
		// If there is an "S", that means there's still a ship not sunk, then game is not over.
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (ships[i][j].toString() == "S") {
					return false;
				}
			}
		}
		return true;
	}
	
	Ship[][] getShipArray(){
		return ships;
	}
	
	void print() {
		
		// open up a new place to store current Ocean.
		String [][] currentOcean = new String[11][11];
		int i, j;
		
		currentOcean[0][0] = " ";
		
		// column number.
		for(i = 1; i < 11; i++) {
			currentOcean[0][i] = " " + (i - 1);
		}
		
		for (i = 1; i < 11; i++) {
			
			// row number
			currentOcean[i][0] = (i - 1) + "";
			for (j = 1; j < 11; j++) {
				// decide if it is hit
				boolean isHit = ships[i - 1][j - 1].hit[i - 1 + j - 1 - (ships[i - 1][j - 1].bowRow + ships[i - 1][j - 1].bowColumn)];
				
				//if hit, then return the corresponding character
				if (isHit) currentOcean[i][j] = " " + ships[i - 1][j - 1].toString();
				else currentOcean[i][j] = " .";
			}
		}
		
		// actual print.
		for (i = 0; i < 11; i++) {
			for (j = 0; j < 11; j++){
				System.out.print(currentOcean[i][j]);
			}
			System.out.println("");
		}
	}
	
}
