package battleship;

public class Cruiser extends Ship {
	
	boolean [] hit = {false, false, false, true};
	
	// Initialize from the abstract ship.
	Cruiser(){
		super.length = 3;
		super.hit = hit;
	}

	@Override
	int getLength() {
		// TODO Auto-generated method stub
		return 3;
	}

	@Override
	String getShipType() {
		// TODO Auto-generated method stub
		return "cruiser";
	}
	
}
