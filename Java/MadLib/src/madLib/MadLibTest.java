/**
 * Zhengchao Ni
 * 73173892
 */

package madLib;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class MadLibTest {
	
	MadLib madlibtest;

	@BeforeEach
	void setUp() throws Exception {
		madlibtest = new MadLib();
	}

	@Test
	void testKeyWords() {
		/**
		 * Test if those words with brackets are extracted correctly.
		 */
		
		// original list
		ArrayList<String> arraylist10 = new ArrayList<String>();
		// expected output list
		ArrayList<String> arraylist11 = new ArrayList<String>();
		// after operation
		ArrayList<String> arraylist10_modified = new ArrayList<String>();
		String string10 = "I'm Zhengchao Ni, [a first-year master at] UPenn";
		arraylist10.add(string10);
		arraylist11.add("a first-year master at");
		arraylist10_modified = madlibtest.keyWords(arraylist10);
		assertEquals(arraylist10_modified, arraylist11);
		
		// for the multiple brackets case. 
		ArrayList<String> arraylist20 = new ArrayList<String>();
		ArrayList<String> arraylist21 = new ArrayList<String>();
		ArrayList<String> arraylist20_modified = new ArrayList<String>();
		String string20 = "[Majoring in] Electrical [Engineering]";
		arraylist20.add(string20);
		arraylist21.add("Majoring in");
		arraylist21.add("Engineering");
		arraylist20_modified = madlibtest.keyWords(arraylist20);
		assertEquals(arraylist20_modified, arraylist21);
		
		// for the all brackets case. 
		ArrayList<String> arraylist30 = new ArrayList<String>();
		ArrayList<String> arraylist31 = new ArrayList<String>();
		ArrayList<String> arraylist30_modified = new ArrayList<String>();
		String string30 = "[Majoring in] [Electrical] [Engineering]";
		arraylist30.add(string30);
		arraylist31.add("Majoring in");
		arraylist31.add("Electrical");
		arraylist31.add("Engineering");
		arraylist30_modified = madlibtest.keyWords(arraylist30);
		assertEquals(arraylist30_modified, arraylist31);
		
		// for the none brackets case. 
		ArrayList<String> arraylist40 = new ArrayList<String>();
		ArrayList<String> arraylist41 = new ArrayList<String>();
		ArrayList<String> arraylist40_modified = new ArrayList<String>();
		String string40 = "Majoring in Electrical Engineering";
		arraylist40.add(string40);
		arraylist40_modified = madlibtest.keyWords(arraylist40);
		assertEquals(arraylist40_modified, arraylist41);
		
	}

	@Test
	void testStandardize() {
		
		/**
		 * just test if 'a' or "an" is added correctly.
		 * Without taking the uppercase into consideration.
		 */
		
		String string1 = "your mother"; // add nothing
		String string2 = "baby"; // add 'a';
		String string3 = "umbrella"; // add "an"
		String string4 = "its feature"; // add nothing
		String string5 = "island"; // add "an"
		
		String string6 = madlibtest.standardize(string1);
		String string7 = madlibtest.standardize(string2);
		String string8 = madlibtest.standardize(string3);
		String string9 = madlibtest.standardize(string4);
		String string0 = madlibtest.standardize(string5);
		
		assertEquals(string6, "your mother");
		assertEquals(string7, "a baby" );
		assertEquals(string8, "an umbrella");
		assertEquals(string9, "its feature");
		assertEquals(string0, "an island");
		
	}

	@Test
	void testReplace() {
		
		/**
		 * Test whether it can use the strings from ArrayList<String> from_input
		 * to replace the bracket words in the line.
		 * The result is stored in new_line.
		 * flag is an ArrayList<Boolean>, used for indicating whether there exists bracket words
		 * in the given line.
		 */
		
		// MUST INITIALIZE!!!!!
		madlibtest.line = new ArrayList<String>();
		madlibtest.from_input = new ArrayList<String>();
		madlibtest.new_line = new ArrayList<String>();
		madlibtest.flag = new ArrayList<Boolean>();
		
		madlibtest.line.add("Dear Administrator, ");
		madlibtest.line.add("My name is [my name].");
		madlibtest.line.add("[school year] graduate student majoring in [school program].");
		
		madlibtest.flag.add(false);
		madlibtest.flag.add(true);
		madlibtest.flag.add(true);
		
		madlibtest.from_input.add("Zhengchao Ni");
		madlibtest.from_input.add("a first-year");
		madlibtest.from_input.add("Electrical Engineering");
		
		ArrayList<String> newarraylist = new ArrayList<String>();
		newarraylist.add("Dear Administrator, ");
		newarraylist.add("My name is Zhengchao Ni.");
		newarraylist.add("a first-year graduate student majoring in Electrical Engineering.");
		
		madlibtest.replace();
		
		assertEquals(madlibtest.new_line, newarraylist);
		assertTrue(madlibtest.new_line != madlibtest.from_input);
		
	}

}
