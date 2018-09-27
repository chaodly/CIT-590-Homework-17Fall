package battleship;

public class Submarine extends Ship{
	boolean [] hit = {false, true, true, true};
	
	// Initialize from the abstract ship.
	Submarine(){
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
		return "submarine";
	}

}
