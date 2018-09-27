/**
 * Name: Zhengchao Ni
 * Penn ID: 73173892
 */

package cipher;

import java.io.*;

public class Caesar{
	
	/**
	 * 
	 */
	
	public String encipher(int shift, String plainText) {
		
		/**
		 * This function is used for encipher a string.
		 * @param shift, the order increase in alphabet.
		 * @param plainText, string read from the txt file.
		 * @return an enciphered string.
		 */
		
		// modifying shift, calculate mod 26 (should be like 8 % 26 = 8; -8 % 26 = 18).
		// so that shift will in [0, 25]
		if (shift > 0)
			shift = shift % 26;
		else if (shift < 0)
			shift = (shift % 26) + 26;
		
		// changing a string into a charArray
		char[] line = plainText.toCharArray();
		
		//shifting operation
		for (int i = 0; i < line.length; i++) {
			
			// if line[i] is a char, then shift 
			//lowercase
			if ((int)line[i] >= 65 && (int)line[i] <= 90) {
				line[i] = (char)(line[i] + shift);
				if ((int)line[i] > 90) {
					line[i] = (char)(line[i] - 26);
				}
			}
			
			//uppercase
			if ((int)line[i] >= 97 && (int)line[i] <= 122) {
				line[i] = (char)(line[i] + shift);
				if ((int)line[i] > 122) {
					line[i] = (char)(line[i] - 26);
				}
			}
		}
		
		// convert the charArray into String.
		String enc_line = new String(line);
		return enc_line;
		
	}
	
	public String decipher(int shift, String cipheredText) {
		
		/**
		 * This function is used for decipher a encrypted string, very similar to the above.
		 * @param shift, the order decrease in alphabet.
		 * @param cipheredText, string that has been ciphered.
		 * @return a deciphered string
		 */
		
		if (shift > 0)
			shift = shift % 26;
		else if (shift < 0)
			shift = (shift % 26) + 26;
		
		// changing a string into a charArray
		char[] line = cipheredText.toCharArray();
		
		//shifting operation
		for (int i = 0; i < line.length; i++) {
			
			// if line[i] is a char, then shift 
			//lowercase
			if ((int)line[i] >= 65 && (int)line[i] <= 90) {
				line[i] = (char)(line[i] - shift);
				if ((int)line[i] < 65) {
					line[i] = (char)(line[i] + 26);
				}
			}
			
			//uppercase
			if ((int)line[i] >= 97 && (int)line[i] <= 122) {
				line[i] = (char)(line[i] - shift);
				if ((int)line[i] < 97) {
					line[i] = (char)(line[i] + 26);
				}
			}
		}
		
		// convert the charArray into String.
		String dec_line = new String(line);
		return dec_line;
		
	}
	
	public boolean diff(String originalFile, String encDecFile) {
		
		/**
		 * This function should first read from those two file path, then compare.
		 * originalFile is the original file path, 
		 * encDecFile is the targeted file path.
		 */
		
		// use for concatenate the line read from the txt file into a complete file.
		String file1 = "", file2 = "";
		
		try {
			// common file reading procedure.
			FileReader filereader1 = new FileReader(originalFile);
			BufferedReader bufferedReader1 = new BufferedReader(filereader1);
			
			FileReader filereader2 = new FileReader(encDecFile);
			BufferedReader bufferedReader2 = new BufferedReader(filereader2);
			
			String line1 = " ", line2 = " ";
			
			while (line1 != null) {
				line1 = bufferedReader1.readLine();
				file1 += line1;
			}
			
			while (line2 != null) {
				line2 = bufferedReader2.readLine();
				file2 += line2;
			}
			
			// Don't forget to close the file!!!
			bufferedReader1.close();
			bufferedReader2.close();
		}
		
		catch (FileNotFoundException e) {
			e.printStackTrace();
		} 
		
		catch (IOException e) {
			e.printStackTrace();
		}
		
		if (file1.equals(file2)) {
			return true;
		}
			
		else
			return false;
		
	}
	
	public void textWrite(String line, String path) {
		
		/**
		 * Output function
		 * @param line, the string that needs to write.
		 * @param path, the file path.
		 * @return no return, just an operation.   
		 */
		
		FileOutputStream fos;
		
		try {
			
			// append... 
			fos = new FileOutputStream(path, true); // default = false;
			PrintWriter pw = new PrintWriter(fos);
			pw.println(line);
			pw.flush();
			pw.close(); //don't forget to close!
		} 
		
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args){
		
		/**
		 * My idea is that first read a line from MyBook.txt file, 
		 * encipher it, write it into encBook.txt.
		 * and decipher it, write it into decBook.txt.
		 * And then, read another line.
		 * 
		 * I think this would allow us to read a very large file.
		 * Better than the idea that first read the whole file, then enciper and decipher...
		 * 
		 * But if we run this program for multiple times, 
		 * we should first delete the generated encBook.txt and decBook.txt. 
		 */
		
		// set file path. Here I use the absolute file path...
		String filePath = "E:\\Java_Programs\\Caesar\\src\\cipher\\MyBook.txt";
		String encFilePath = "E:\\Java_Programs\\Caesar\\src\\cipher\\encBook.txt";
		String decFilePath = "E:\\Java_Programs\\Caesar\\src\\cipher\\decBook.txt";
		
		// create a new object, because the functions in the class are not static.
		Caesar caesar = new Caesar();
		
		try {
			
			//Step 1, create the FileReader;
			FileReader filereader = new FileReader(filePath);
			
			//Step 2, using the file reader, create a BufferedReader
			BufferedReader bufferedReader = new BufferedReader(filereader);
			
			//Step 3, read the file, for example, line by line
			String line = bufferedReader.readLine();
			
			while(line != null){
				
				//readLine returns null if there are no more lines
				String string1 = caesar.encipher(5, line);
				caesar.textWrite(string1, encFilePath);
				
				String string2 = caesar.decipher(5, string1);
				caesar.textWrite(string2, decFilePath);
				
				line = bufferedReader.readLine();
			}
			
			bufferedReader.close();
		} 
		
		catch (FileNotFoundException e) {
			e.printStackTrace();
		} 
		
		catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println("The deciphered file equals to the original file?....\n" + caesar.diff(filePath, decFilePath));
	}
}