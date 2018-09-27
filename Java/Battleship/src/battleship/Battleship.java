package battleship;

public class Battleship extends Ship{
	
	// default, {false, false, false, false}
	boolean [] hit = new boolean[4];
	
	// Initialize from the abstract ship.
	Battleship(){
		super.length = 4;
		super.hit = hit;
	}

	@Override
	int getLength() {
		// TODO Auto-generated method stub
		return 4;
	}

	@Override
	String getShipType() {
		// TODO Auto-generated method stub
		return "battleship";
	}
}
