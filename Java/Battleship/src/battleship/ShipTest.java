package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;


class ShipTest {
	
	Ship battleshiptest;
	Ship cruisertest;
	Ship destroyertest;
	Ship submarinetest;
	Ship emptyseatest;
	Ocean ocean1;
	Ocean ocean2;

	@BeforeEach
	void setUp() throws Exception {
		battleshiptest = new Battleship();
		cruisertest = new Cruiser();
		destroyertest = new Destroyer();
		submarinetest = new Submarine();
		emptyseatest = new EmptySea();
		ocean1 = new Ocean();
		ocean2 = new Ocean();
	}

	@Test
	void testGetLength() {
		assertEquals(battleshiptest.length, 4);
		assertEquals(cruisertest.length, 3);
		assertEquals(destroyertest.length, 2);
		assertEquals(submarinetest.length, 1);
		assertEquals(emptyseatest.length,1);
	}

	@Test
	void testGetBowRow() {
		battleshiptest.bowRow = 4;
		assertEquals(battleshiptest.getBowRow(), 4);
		cruisertest.bowRow = 5;
		assertEquals(cruisertest.getBowRow(), 5);
		destroyertest.bowRow = 6;
		assertEquals(destroyertest.getBowRow(), 6);
		submarinetest.bowRow = 7;
		assertEquals(submarinetest.getBowRow(), 7);
		emptyseatest.bowRow = 8;
		assertEquals(emptyseatest.getBowRow(), 8);
		
	}

	@Test
	void testGetBowColumn() {
		battleshiptest.bowColumn = 2;
		assertEquals(battleshiptest.getBowColumn(), 2);
		cruisertest.bowColumn = 3;
		assertEquals(cruisertest.getBowColumn(), 3);
		destroyertest.bowColumn = 8;
		assertEquals(destroyertest.getBowColumn(), 8);
		submarinetest.bowColumn = 9;
		assertEquals(submarinetest.getBowColumn(), 9);
		emptyseatest.bowColumn = 1;
		assertEquals(emptyseatest.getBowColumn(), 1);
	}

	@Test
	void testIsHorizontal() {
		battleshiptest.horizontal = true;
		assertEquals(battleshiptest.isHorizontal(), true);
		cruisertest.horizontal = false;
		assertEquals(cruisertest.isHorizontal(), false);
		destroyertest.horizontal = false;
		assertEquals(destroyertest.isHorizontal(), false);
		submarinetest.horizontal = true;
		assertEquals(submarinetest.isHorizontal(), true);
	}

	@Test
	void testSetBowRow() {
		battleshiptest.setBowRow(3);
		assertEquals(battleshiptest.bowRow, 3);
		cruisertest.setBowRow(4);
		assertEquals(cruisertest.bowRow, 4);
		destroyertest.setBowRow(5);
		assertEquals(destroyertest.bowRow, 5);
		submarinetest.setBowRow(6);
		assertEquals(submarinetest.bowRow, 6);
		
	}

	@Test
	void testSetBowColumn() {
		battleshiptest.setBowColumn(9);
		assertEquals(battleshiptest.bowColumn, 9);
		cruisertest.setBowColumn(8);
		assertEquals(cruisertest.bowColumn, 8);
		destroyertest.setBowColumn(7);
		assertEquals(destroyertest.bowColumn, 7);
		submarinetest.setBowColumn(1);
		assertEquals(submarinetest.bowColumn, 1);
	}

	@Test
	void testSetHorizontal() {
		battleshiptest.setHorizontal(false);
		assertEquals(battleshiptest.horizontal, false);
		cruisertest.setHorizontal(true);
		assertEquals(cruisertest.horizontal, true);
		destroyertest.setHorizontal(true);
		assertEquals(destroyertest.horizontal, true);
		submarinetest.setHorizontal(false);
		assertEquals(submarinetest.horizontal, false);
	}

	@Test
	void testGetShipType() {
		assertEquals(battleshiptest.getShipType(), "battleship");
		assertEquals(cruisertest.getShipType(), "cruiser");
		assertEquals(destroyertest.getShipType(), "destroyer");
		assertEquals(submarinetest.getShipType(), "submarine");
		assertEquals(emptyseatest.getShipType(), "");
	}

	@Test
	void testOkToPlaceShipAt() {
		
		// There's nothing in current ocean, so must okay to place ship.
		assertTrue(battleshiptest.okToPlaceShipAt(0, 0, true, ocean1));
		
		// Fill the second row with submarines.
		for (int i = 0; i < 10; i++) {
			ocean1.ships[2][i] = submarinetest;
		}
		
		// So we cannot place battleshiptest in the first or third row, but it's okay to place in the forth row. (All horizontal direction)
		assertFalse(battleshiptest.okToPlaceShipAt(1, 0, true, ocean1));
		assertFalse(battleshiptest.okToPlaceShipAt(3, 0, true, ocean1));
		assertTrue(battleshiptest.okToPlaceShipAt(4, 0, true, ocean1));
		
		// Fill the eighth row with submarines.
		for (int i = 0; i < 10; i++) {
			ocean1.ships[8][i] = submarinetest;
		}
		
		// So, cannot place battleship vertically.
		assertTrue(!battleshiptest.okToPlaceShipAt(3, 0, false, ocean1));
		
		assertTrue(cruisertest.okToPlaceShipAt(4, 0, true, ocean1));
		assertTrue(cruisertest.okToPlaceShipAt(4, 0, false, ocean1));
		assertFalse(cruisertest.okToPlaceShipAt(6, 0, false, ocean1));
		assertFalse(cruisertest.okToPlaceShipAt(7, 0, true, ocean1));
		
		
		assertTrue(destroyertest.okToPlaceShipAt(5, 5, false, ocean1));
		assertTrue(destroyertest.okToPlaceShipAt(4, 8, true, ocean1));
		assertFalse(destroyertest.okToPlaceShipAt(6, 3, false, ocean1));
		assertFalse(destroyertest.okToPlaceShipAt(7, 7, true, ocean1));
		
		assertTrue(submarinetest.okToPlaceShipAt(5, 5, true, ocean1));
		assertTrue(submarinetest.okToPlaceShipAt(6, 9, false, ocean1));
		assertFalse(submarinetest.okToPlaceShipAt(2, 4, true, ocean1));
		assertFalse(submarinetest.okToPlaceShipAt(8, 7, false, ocean1));
		
	}

	@Test
	void testPlaceShipAt() {
		// operating in ocean2
		
		// (0, 0), (0, 1), (0, 2), (0, 3)
		battleshiptest.placeShipAt(0, 0, true, ocean2);
		assertEquals(ocean2.ships[0][0].getShipType(), "battleship");
		assertEquals(ocean2.ships[0][3].getShipType(), "battleship");
		assertFalse(ocean2.ships[1][3].getShipType().equals("battleship"));
		
		// (2, 0), (2, 1), (2, 2)
		cruisertest.placeShipAt(2, 0, true, ocean2);
		assertEquals(ocean2.ships[2][0].getShipType(), "cruiser");
		assertEquals(ocean2.ships[2][2].getShipType(), "cruiser");
		assertFalse(ocean2.ships[3][2].getShipType().equals("cruiser"));
		
		// (5, 5), (6, 5)
		destroyertest.placeShipAt(5, 5, false, ocean2);
		assertEquals(ocean2.ships[5][5].getShipType(), "destroyer");
		assertEquals(ocean2.ships[6][5].getShipType(), "destroyer");
		assertFalse(ocean2.ships[7][5].getShipType().equals("destroyer"));
		
		// (7, 7)
		submarinetest.placeShipAt(7, 7, false, ocean2);
		assertEquals(ocean2.ships[7][7].getShipType(), "submarine");
		assertFalse(ocean2.ships[8][8].getShipType().equals("submarine"));
	}

	@Test
	void testShootAt() {
		
		battleshiptest = new Battleship();
		
		// (0, 0), (0, 1), (0, 2), (0, 3)
		battleshiptest.setBowRow(0);
		battleshiptest.setBowColumn(0);
		battleshiptest.setHorizontal(true);
		battleshiptest.shootAt(0, 1);
		assertEquals(battleshiptest.hit[1], true);
		assertEquals(battleshiptest.hit[0], false);
		
		cruisertest = new Cruiser();
		
		// (2, 0), (2, 1), (2, 2)
		cruisertest.setBowRow(2);
		cruisertest.setBowColumn(0);
		cruisertest.setHorizontal(true);
		cruisertest.shootAt(2, 1);
		assertEquals(cruisertest.hit[1], true);
		assertEquals(cruisertest.hit[0], false);
		
		destroyertest = new Destroyer();
		
		// (4, 4), (5, 4)
		destroyertest.setBowRow(4);
		destroyertest.setBowColumn(4);
		destroyertest.setHorizontal(false);
		destroyertest.shootAt(5, 4);
		assertEquals(destroyertest.hit[1], true);
		assertEquals(destroyertest.hit[0], false);
		
		submarinetest = new Submarine();
		
		// (7, 7)
		submarinetest.setBowRow(7);
		submarinetest.setBowColumn(7);
		submarinetest.setHorizontal(false);
		submarinetest.shootAt(7, 7);
		assertEquals(submarinetest.hit[0], true);
	}

	@Test
	void testIsSunk() {
		
		battleshiptest = new Battleship();
		cruisertest = new Cruiser();
		destroyertest = new Destroyer();
		submarinetest = new Submarine();
		
		assertFalse(battleshiptest.isSunk());
		assertFalse(cruisertest.isSunk());
		assertFalse(destroyertest.isSunk());
		assertFalse(submarinetest.isSunk());
		
		battleshiptest.placeShipAt(0, 0, true, ocean2);
		battleshiptest = ocean2.ships[0][0];
		battleshiptest.shootAt(0, 0);
		battleshiptest.shootAt(0, 1);
		battleshiptest.shootAt(0, 2);
		battleshiptest.shootAt(0, 3);
		assertTrue(battleshiptest.isSunk());
		
		
		cruisertest.placeShipAt(2, 0, true, ocean2);
		cruisertest = ocean2.ships[2][0];
		cruisertest.shootAt(2, 0);
		cruisertest.shootAt(2, 1);
		cruisertest.shootAt(2, 2);
		assertTrue(cruisertest.isSunk());
		
		destroyertest.placeShipAt(4, 5, false, ocean2);
		destroyertest = ocean2.ships[4][5];
		destroyertest.shootAt(4, 5);
		destroyertest.shootAt(5, 5);
		assertTrue(destroyertest.isSunk());
		
		submarinetest.placeShipAt(7, 7, false, ocean2);
		submarinetest = ocean2.ships[7][7];
		submarinetest.shootAt(7, 7);
		assertTrue(submarinetest.isSunk());

	}

	@Test
	void testToString() {
		boolean[] sunk = {true, true, true, true};
		assertEquals(battleshiptest.toString(), "S");
		assertEquals(cruisertest.toString(), "S");
		assertEquals(destroyertest.toString(), "S");
		assertEquals(submarinetest.toString(), "S");
		assertEquals(emptyseatest.toString(), "-");
		
		
		battleshiptest.hit = sunk;
		cruisertest.hit = sunk;
		destroyertest.hit = sunk;
		submarinetest.hit = sunk;
		
		assertEquals(battleshiptest.toString(), "x");
		assertEquals(cruisertest.toString(), "x");
		assertEquals(destroyertest.toString(), "x");
		assertEquals(submarinetest.toString(), "x");
		assertEquals(emptyseatest.toString(), "-");
		
	}

}
