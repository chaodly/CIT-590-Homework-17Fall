/**
 * Name: Zhengchao Ni
 * Penn ID: 73173892
 */

package cipher;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CaesarTest {
	
	// Create a new object first of all.
	// If initiate it in the void setUp(), it will not compile!!!
	Caesar caesar;

	@BeforeEach
	public void setUp() throws Exception {
		caesar = new Caesar();
	}

	@Test
	void testEncipher() {
		
		/**
		 * Test the encipher function. 
		 */
		
		String string_original = "My name is Zhengchao Ni, a first-year master at UPenn, ESE.";
		String string_enc = "Rd sfrj nx Emjslhmft Sn, f knwxy-djfw rfxyjw fy ZUjss, JXJ.";
		assertFalse(string_original.equals(string_enc));
		assertTrue(caesar.encipher(5, string_original).equals(string_enc));
		
		// test some weird values, negative or very large.
		assertTrue(caesar.encipher(-21, string_original).equals(string_enc));
		assertTrue(caesar.encipher(265, string_original).equals(string_enc));
		assertTrue(caesar.encipher(-281, string_original).equals(string_enc));
	}

	@Test
	void testDecipher() {
		
		/**
		 * Test the decipher function. 
		 */
		
		String string_enc = "Rd sfrj nx Emjslhmft Sn, f knwxy-djfw rfxyjw fy ZUjss, JXJ.";
		String string_dec = "My name is Zhengchao Ni, a first-year master at UPenn, ESE.";
		assertFalse(string_enc.equals(string_dec));
		assertTrue(caesar.decipher(5, string_enc).equals(string_dec));
		
		assertTrue(caesar.decipher(-21, string_enc).equals(string_dec));
		assertTrue(caesar.decipher(265, string_enc).equals(string_dec));
		assertTrue(caesar.decipher(-281, string_enc).equals(string_dec));
	}

}
