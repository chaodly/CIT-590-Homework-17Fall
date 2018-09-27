package battleship;

public class Destroyer extends Ship{
	boolean [] hit = {false, false, true, true};
	
	// Initialize from the abstract ship.
	Destroyer(){
		super.length = 2;
		super.hit = hit;
	}

	@Override
	int getLength() {
		// TODO Auto-generated method stub
		return 2;
	}

	@Override
	String getShipType() {
		// TODO Auto-generated method stub
		return "destroyer";
	}

}
