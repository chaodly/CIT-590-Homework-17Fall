package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class OceanTest {
	Ocean oceantest;

	@BeforeEach
	void setUp() throws Exception {
		oceantest = new Ocean();
		oceantest.ocean = new Ocean();
	}

	@Test
	void testOcean() {
		for (int i = 0; i <10; i++) {
			for (int j = 0; j < 10; j++) {
				assertEquals(oceantest.ships[i][j].toString(), "-");
			}
		}
	}

	@Test
	void testPlaceAllShipsRandomly() {
		oceantest.placeAllShipsRandomly();
		int sum = 0;
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (oceantest.ocean.ships[i][j].toString().equals("-") == false) {
					sum += 1;
				}
			}
		}
		assertEquals(sum, 20);
	}

	@Test
	void testIsOccupied() {
		Ship ship = new Battleship();
		ship.placeShipAt(0, 0, true, oceantest.ocean);
		assertTrue(oceantest.isOccupied(0, 0));
		assertFalse(oceantest.isOccupied(0, 5));
	}

	@Test
	void testShootAt() {
		Ship ship = new Battleship();
		ship.placeShipAt(0, 0, true, oceantest);
		oceantest.ocean.ships = oceantest.ships;
		oceantest.shootAt(0, 0);
		assertTrue(oceantest.getHitCount() == 1);
	}

	@Test
	void testGetShotsFired() {
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				oceantest.shootAt(i, j);
			}
		}
		assertEquals(oceantest.getShotsFired(), 25);
	}

	@Test
	void testGetHitCount() {
		Ship ship = new Battleship();
		ship.placeShipAt(0, 0, true, oceantest.ocean);
		for(int j = 0; j < 10; j++) {
			oceantest.shootAt(0, j);
			}
		assertEquals(oceantest.getHitCount(),4);
		assertTrue(oceantest.getShotsFired() != oceantest.getHitCount());
	}

	@Test
	void testIsGameOver() {
		oceantest.placeAllShipsRandomly();
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				oceantest.shootAt(i, j);
			}
		}
		assertTrue(oceantest.isGameOver());
	}
	

	@Test
	void testGetShipArray() {
		Ship[][] ships = new Ship[10][10];
		ships[0][0] = new Battleship();
		ships[2][2] = new Cruiser();
		ships[4][4] = new Destroyer();
		ships[6][6] = new Submarine();
		oceantest.ships = ships;
		
		assertEquals(oceantest.ships, ships);
	}

}



