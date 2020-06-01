import java.io.*;
import java.lang.*;
import java.util.*;

////////////////////////////////////////////////////////////////
// Handle the words of the dictionary
////////////////////////////////////////////////////////////////
public class Words {
	HashMap <String, String> wordsMap;
	HashMap <String, String> examplesMap;
	public int numberOfWords;

	public Words () {
		wordsMap = new HashMap < String, String>();
		examplesMap = new HashMap < String, String>();
		numberOfWords = 15;
	}

	public String get (String word) { return wordsMap.get (word); }

	public String getExample (String word) { return examplesMap.get (word); }

	public ArrayList <String> getString () { return new ArrayList (wordsMap.keySet ()); }

	public void loadWords () {
		try {
			BufferedReader bf = new BufferedReader (new FileReader ("words.txt"));

			String text = null;
			int i=0;
			while (i < numberOfWords) {
				text = bf.readLine();
				if (text.startsWith ("#")) // Don't load this line
					continue;
				else
					i++;

				String english = text.split(":")[0];	
				String spanish = text.split(":")[1];	
				wordsMap.put (english, spanish);
				wordsMap.put (spanish, english);

				examplesMap.put (english, "");
				examplesMap.put (spanish, "");

				if (text.split (":").length	 > 2) {
					String example = text.split(":")[2];	
					examplesMap.put (english, example);
					examplesMap.put (spanish, example);
				}
			}
		}catch (IOException e) {e.printStackTrace();}
	}

	public void loadRandomWords () {
		try {
			BufferedReader bf = new BufferedReader (new FileReader ("words.txt"));
			ArrayList <String> wordList = new ArrayList <String> ();

			String text = null;
			while ((text = bf.readLine()) != null) 
				wordList.add (text);

			Collections.shuffle (wordList);

			wordsMap.clear ();
			examplesMap.clear ();
			for (int i=0; i < numberOfWords; i++) {
				text = wordList.get (i);
				String english = text.split(":")[0];	
				String spanish = text.split(":")[1];	
				wordsMap.put (english, spanish);
				wordsMap.put (spanish, english);

				if (text.split (":").length	 > 2) {
					String example = text.split(":")[2];	
					examplesMap.put (english, example);
					examplesMap.put (spanish, example);
				}
			}
		}catch (IOException e) {e.printStackTrace();}
	}
	// Main to test the class
	public static void main (String args []) {
		StringDic s1 = new StringDic (args[0], 1);
		StringDic s2 = new StringDic (args[1], 1);
		StringDic s3 = new StringDic (args[2], 1);

		HashMap <StringDic, StringDic> wordsMap;
		wordsMap = new HashMap < StringDic, StringDic>();

		wordsMap.put (s1, s2);
		StringDic s = wordsMap.get (s3);

		System.out.println (s);
	}
}

////////////////////////////////////////////////////////////////
// String with language attribute
////////////////////////////////////////////////////////////////
class StringDic implements Comparable <StringDic> {

	String string;
	int language = -1; // 0: English, 1: Spanish

	public int compareTo (StringDic s) {
		System.out.println (string + " == " + s.string);

		if (string == s.string) 
			return 0;
		else 
			return 1;
	}

	public StringDic (String s, int l) {
		string = s;
		language = l;
	}
	public StringDic (int lang) {
		language = lang;
	}
	public String toString () {
		return string;
	}
}

////////////////////////////////////////////////////////////////
//
