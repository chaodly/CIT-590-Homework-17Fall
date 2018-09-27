package battleship;

public abstract class Ship {
	
	// Instance Variables
	int bowRow;
	int bowColumn;
	int length;
	boolean horizontal; // true if single row
	
	// an array of booleans telling whether that part of the ship has been hit.
	// Only battleships use all four locations; cruisers use the first three; destroyers 2; submarines 1;
	// and "empty sea" either one or none.
	boolean [] hit = new boolean[4]; 
	
	// Will be initialized in battleships, cruisers, destroyers and submarines, respectively.
	abstract int getLength();
	
	// It may cause ocean.ocean.ship in the main function.
	Ocean ocean;
	
	// Getters
	int getBowRow() {
		return bowRow;
	}
	
	int getBowColumn() {
		return bowColumn;
	}
	
	boolean isHorizontal() {
		return horizontal;
	}
	
	// Setters
	void setBowRow(int row) {
		bowRow = row;
	}
	
	void setBowColumn(int column) {
		bowColumn = column;
	}
	
	void setHorizontal(boolean horizontal) {
		this.horizontal = horizontal;
	}
	
	// Will be initialized in battleships, cruisers, destroyers and submarines, respectively.
	abstract String getShipType();
	
	/**
	 * Decide whether it is okay to place at (row, column), with horizontal(if true) or vertical (if false) direction. 
	 * @param row
	 * @param column
	 * @param horizontal
	 * @param ocean
	 * @return a boolean variable indicating whether it is okay to place the ship.
	 */
	boolean okToPlaceShipAt(int row, int column, boolean horizontal, Ocean ocean) {
		
		/**
		 * In ordinary condition, (not at boundaries or corners), we have to decide from 
		 * row index : from (row - 1) to (row + 1) 
		 * column index : from (column - 1) to (column + length).
		 */
		
		int rStart = 1, cStart = 1, rEnd = 1, cEnd = 1;
		
		// boundary and corner conditions.
		if (row == 0) rStart = 0;
		if (column == 0) cStart = 0;
		if (row == 9) rEnd = 0;
		if (column == 9) cEnd = 0;
		
		// If submarine is placed at corners.
		if (length == 1) {
			if(row + length > 10 || column + length > 10) return false;
		}
		
		else{
			if (horizontal) {
				if(column + length  > 10) return false;
				
				// if at boundary, column end become (length - 1).
				if(column + length == 10) cEnd = length - 1;
				else cEnd = length;	
			}
			
			else {
				if (row + length > 10) return false;
				if (row + length == 10) rEnd = length -1;
				else rEnd = length;
			}
		}
		
		for (int i = row - rStart; i <= row + rEnd; i++) {
			for (int j = column - cStart; j <= column + cEnd; j++) {
				if(ocean.ships[i][j].toString() != "-") {
					return false;
				}
			}
		}
		return true;
		
	}
	
    /**
     * Actually place the ship in the ocean.ships array.
     * @param row
     * @param column
     * @param horizontal
     * @param ocean
     */
	void placeShipAt(int row, int column, boolean horizontal, Ocean ocean) {
    	
		Ship ship = new EmptySea();
		if (length == 4) {
			ship = new Battleship();
		}
		else if (length == 3) {
			ship = new Cruiser();
		}
		else if (length == 2) {
			ship = new Destroyer();
		}
		else if (length == 1) {
			ship = new Submarine();
		}
		
    	// Should Set!!
    	ship.setBowRow(row);
    	ship.setBowColumn(column);
    	ship.horizontal = horizontal;
    	ship.hit = hit;
		
		if (horizontal) {
			for (int i = column; i < column + length; i++) {
				// place the ship in the array.
				ocean.ships[row][i] = ship;
			}
		}
		else {
			for (int i = row; i < row + length; i++) {
				ocean.ships[i][column] = ship;
			}
		}
	}
    
    /**
     * Actually shoot at (row, column),
     * If got shot, change the value of the corresponding boolean hit list.
     * @param row
     * @param column
     * @return
     */
	boolean shootAt(int row, int column) {
    	
    	if (horizontal) {
    		// shoot at the other row...
    		if (row != bowRow) return false;
    		
    		// shoot at the exact row and within the column range.
        	if (column >= bowColumn && column < bowColumn + length) {
        		hit[column - bowColumn] = true;
        		return true;
        	}
        	else return false;
    	}
    	else {
    		if (column != bowColumn) return false;
        	if (row >= bowRow && row < bowRow + length) {
        		hit[row - bowRow] = true;
        		return true;
        	}
        	else return false;
    	}

    }
    	
    
    boolean isSunk() {
    	// if there is still a "false", that means the ship is not totally sunk.
    	for (int i = 0; i < 4; i++) {
    		if (hit[i] == false) return false;
    		
    	}
    	return true; 
    }
    
    @Override
    public String toString() {
    	// if the ship is totally sunk, output "x".
    	if(isSunk()) return "x";
    	else return "S";
    }
}
