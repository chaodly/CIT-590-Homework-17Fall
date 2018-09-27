package battleship;

public class EmptySea extends Ship {
	
	boolean[] hit = {false, true, true, true};
 
	EmptySea(){
		super.length = 1;
		super.hit = hit;
	}
	
	@Override
	int getLength() {
		// TODO Auto-generated method stub
		return 1;
	}

	@Override
	String getShipType() {
		// TODO Auto-generated method stub
		return "";
	}
	
	@Override
	// Always return false.
	boolean shootAt(int row, int column) {
		// TODO Auto-generated method stub
		hit[0] = true;
		return false;
	}
	
	@Override
	boolean isSunk() {
		return false;
	}
	
	@Override
	public String toString() {
		return "-";
	}
}
