/**
 * Zhengchao Ni
 * 73173892
 */

package madLib;

import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;

/**
 * 
 * General Idea of the code
 * I have to say my method is a little stupid, so my code seems a bit long.
 * 
 * Firstly, read each line from the original file into an ArrayList<String>.
 * Then, extract all the bracket words from each line and store it into another 
 * ArrayList<String>, using for interacting with user.
 * Additionally, get user input, and store.
 * Moreover, mark each line with true or false, if there exist bracket in a line, then true,
 * if not, mark false. Each true or false stored in an ArrayList<Boolean>.
 *
 * Last but not least, for the most challenging function, replacing the words.
 * Firstly, if a line is without bracket words, directly copy.
 * Then, if with brackets, decide its number.
 * if there is only one bracket, then remain the string around the brackets, and concatenate
 * user input.
 * else if there are multiple brackets, we need a iteration.
 * in each iteration, we add the string which between ']' and '[', 
 * after that, add the user input, so on and so forth.
 * after iteration, add the last piece, that is, from the last ']' to the ending of the line.
 *  
 */

public class MadLib{
	
	// if I write "List<String> line = new ArrayList<String>();", It will not compile 
	
	// stores all the lines read from the original txt file.
	ArrayList<String> line; 
	
	// stores all the (raw) missing words (including brackets).
	ArrayList<String> key_words;
	
	// stores all the standardized missing words, without those brackets.
	ArrayList<String> s_key_words;
	
	// store all the user input into a List<String>
	ArrayList<String> from_input;
	
	// flag = true if the line contains a bracket, false if the line do no contain brackets
	ArrayList<Boolean> flag;
	
	// stores the modified line, original line with replaced words.
	ArrayList<String> new_line;
	
	// count for the index of user_input List<String>.
	int count = 0;
	
	public ArrayList<String> readFile(String path) {
		
		/**
		 * Just read a file from the path, store it into an ArrayList. 
		 * return an ArrayList, called line.
		 */
		
		try {
			FileReader filereader = new FileReader(path);
			BufferedReader bufferedReader = new BufferedReader(filereader);
			String stringline = bufferedReader.readLine();
			line = new ArrayList<String>(); 
			
			while (stringline != null) {
				// add each line of the original file into the List<String> line.
				line.add(stringline);
				stringline = bufferedReader.readLine();
			}
			bufferedReader.close();
		} 
		
		catch (FileNotFoundException e) {
			e.printStackTrace();
		} 
		
		catch (IOException e) {
			e.printStackTrace();
		}
		return line;
	}
	
	
	public ArrayList<String> keyWords(ArrayList<String> line) {
		
		/**
		 * This function is use to extract those missing words with brackets.
		 * returns an ArrayList<String>, called s_key_words, containing all that words,
		 * without brackets.
		 * @param line, input a line with bracket words.
		 * @return an ArrayList<String>, containing only those plain words.
		 */
		
		//initialize
		key_words = new ArrayList<String>();
		s_key_words = new ArrayList<String>();
		flag = new ArrayList<Boolean>();
		
		for (int i = 0; i < line.size(); i++) {
			String string1 = line.get(i).toString();
			flag.add(string1.contains("["));
			
			// use "]" to split, I don't know why I cannot use "[" to split...
			String[] string2 = string1.split("]");
			
			for (int j = 0; j < string2.length; j++) {
				try {
					int index1 = string2[j].indexOf('[');
					// I used "]" to split, so "]" will disappear, I need to add it back.
					key_words.add(string2[j].substring(index1));
				}
				catch(Exception e) {
					continue;
				}
			}
		}		
		
		for (int i = 0; i < key_words.size(); i++) {
			
			// delete all that brackets, and store them into a new ArrayList<String>.
			s_key_words.add(key_words.get(i).substring(1, key_words.get(i).length()));
		}
		
		return s_key_words;
	}
	
	public String standardize(String word) {
		
		/**
		 *  if the string begins with a pron. such as my, your, his, her, its, their,
		 *  there is no need to add 'a' or 'an'.
		 */
		
		if (word.startsWith("my") || word.startsWith("your") || word.startsWith("his") || word.startsWith("her")
				|| word.startsWith("its") || word.startsWith("their")) {
			return word.substring(0, word.length());
		}
		
		else {
			// when start with an a-e-i-o-u, use "an".
			// Here, I did not take the upper case into account, followed the instruction.
			if (word.startsWith("a") || word.startsWith("e") || (word.startsWith("i") && (word.startsWith("its") == false))
					|| (word.startsWith("o") || word.startsWith("u"))) {
				return  "an " + word.substring(0, word.length());
			}
			
			else
				return  "a " + word.substring(0, word.length());
		}
	}
	
	public void play() {
		
		/**
		 * This function output a sentence interact with the user.
		 */
		
		from_input = new ArrayList<String>(); 
		for (int i = 0; i < s_key_words.size(); i++) {
			String temp = standardize(s_key_words.get(i));
			System.out.println("Enter " + temp + ":" + "\n");
			try {
				ask();
			}
			catch (Exception e){
				continue;
			}
		}
	}
	
	
	public void ask() {
		
		/**
		 * Insist on getting an proper answer from user. 
		 */
		
		Scanner user_input = new Scanner(System.in);
		String input_string =  user_input.nextLine();
		
		// for the empty string case
		while (input_string.isEmpty() == true) {
			System.out.println("Please input your answer!!!...");
			input_string =  user_input.nextLine();
		}
		
		// for the weird string case
		while (((int)input_string.toCharArray()[0] < 48) || 
				(((int)input_string.toCharArray()[0] > 57) && ((int)input_string.toCharArray()[0] < 65)) ||
				(((int)input_string.toCharArray()[0] > 90) && ((int)input_string.toCharArray()[0] < 97)) ||
				((int)input_string.toCharArray()[0] > 122)) {
					System.out.println("Please double check your input...");
					input_string =  user_input.nextLine();
					
					while (input_string.isEmpty() == true) {
						System.out.println("Please input your answer!!!...");
						input_string =  user_input.nextLine();
					}
		}	
		from_input.add(input_string);
		
		//user_input.close();
		
	}
	
	
	
	public void replace() {
		
		/**
		 * replace those missing words, from ArrayList<String> user_input 
		 */
		
		new_line = new ArrayList<String>();
		for (int i = 0; i < line.size(); i++) {
			
			// if flag.get(i) == false, that means line.get(i) do not contain brackets
			if (flag.get(i) == false) {
				
				// so copy directly.
				new_line.add(line.get(i));
			}
			
			// focus on line.get(i)
			else {
				
				/**
				 * for those lines with missing words (brackets)
				 * I split it into several pieces
				 * first of all, from line.get(i) (later convert into a charArray called line_char)
				 * from line_char[0], to the first '[',
				 * then decide if there is only one pair of brackets
				 * if so, then add the remaining part
				 * if not, enter the iteration, that add the string from indexright.get(i - 1) to indexleft.get(i)
				 * for each adding a string, add the user_input string afterwards.
				 */
				
				ArrayList<Integer> indexleft = new ArrayList<Integer>();
				ArrayList<Integer> indexright = new ArrayList<Integer>();
				
				// convert into charArray()
				char[] line_char = line.get(i).toCharArray();
				
				// store the index of '[' and ']', respectively.
				for (int x = 0; x < line.get(i).length(); x++) {
					if (line_char[x] == '[') {
						indexleft.add(x);
					}
					if (line_char[x] == ']') {
						indexright.add(x);
					}	
				}
				
				// form the new string, with replaced words. 
				// a line for new_line
				String temp = new String();
				
				// add the first piece, from line_char[0], to the beginning of the first '['
				for (int n = 0; n < indexleft.get(0); n++) {
					temp += line_char[n];
				}
				
				// add the element from the user_input string list
				temp += from_input.get(count);
				count++;
				
				// if there's only one '[]', after adding the user_input, add the remaining part
				// that is, from ']' to the end.
				if (indexleft.size() == 1) {
					for (int n = indexright.get(0) + 1; n < line.get(i).length(); n++) {
						temp += line_char[n];
					}
					new_line.add(temp.toString());
				}
				
				// if there are more than one brackets,
				// iterate
				// everytime, adding from ']' to '[', then add the user input
				// for the last time, add the remaining part,
				// that is, from the last ']' to the ending.
				else {
					for (int m = 1; m < indexleft.size(); m++) {
						for (int n = indexright.get(m - 1) + 1; n < indexleft.get(m); n++) {
							temp += line_char[n];
						}
						temp += from_input.get(count);
						count++;
					}
					for (int n = indexright.get(indexright.size() - 1) + 1; n < line.get(i).length(); n++) {
						temp += line_char[n];
					}
					new_line.add(temp); 
				}
			}
		}
	}
	
	public void putFile(ArrayList<String> nl, String save_path) {
		
		/**
		 * output function, write into a new file.
		 */
		
		FileOutputStream fos;
		
		try {
			
			// append... 
			fos = new FileOutputStream(new File(save_path));  // set up a new file, override the original.
			PrintWriter pw = new PrintWriter(fos);
			
			for (int i = 0; i < new_line.size(); i++) {
				pw.println(new_line.get(i));
			}
			pw.flush();
			pw.close(); //don't forget to close!
		} 
		
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
		
	public static void main(String[] args) {
		
		String filePath = "E:\\Java_Programs\\MadLib\\src\\madLib\\story.txt";
		
		MadLib madlib1 = new MadLib();
		
		ArrayList<String> string = madlib1.readFile(filePath);
		
		madlib1.keyWords(string);
		
		madlib1.play(); // interact with user, ask() in it.
		
		madlib1.replace();
		
		madlib1.putFile(madlib1.new_line, filePath);
	}
}