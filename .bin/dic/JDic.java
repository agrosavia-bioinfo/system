import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.lang.*;
import java.io.*;

// Controller for JDic class
interface JDicCtrl {
		public void newGameEvent (String typeOfGame);
		public void wordsMatchedEvent (String first, String second, String example);
}

////////////////////////////////////////////////////////////////
public class JDic extends JFrame implements JDicCtrl {
	JDicCtrl controller = this;
	Words words;
	int numberOfWordsNotMatched;
	PanelCommands commands;
	PanelGrid grid;
	PanelWords wordsPanel;
	ArrayList <String> arrayOfWords; 

	public JDic () {
		super ("LG Dictionary");

		words = new Words ();
		words.loadWords ();
		commands = new PanelCommands (controller);
		grid = new PanelGrid (controller, words);
		wordsPanel = new PanelWords ();

		add (commands, "North");
		add (grid, "Center");
		add (wordsPanel, "South");
		setSize (1020,500);
		setLocation (0,0);
		setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);

		newGameEvent ("new");
	}

	public void newGameEvent (String typeOfGame) {
		if (typeOfGame == "random")
			words.loadRandomWords ();

		arrayOfWords = new ArrayList();
		numberOfWordsNotMatched = words.numberOfWords;
		remove (grid);
		wordsPanel.remove ();
		grid = new PanelGrid (controller, words);
		add (grid, "Center");
		setVisible (true);
	}

	public void wordsMatchedEvent (String first, String second, String example) {
		String allWordsString = first + " : " + second + " : " + example;
		wordsPanel.add (allWordsString);
		arrayOfWords.add (first);
		arrayOfWords.add (second);
		setVisible (true);
		numberOfWordsNotMatched--;
		if (numberOfWordsNotMatched == 0) 
			Speak.speakAllWords (arrayOfWords);
	}

	public static void main (String args[]) {
		JDic jdic = new JDic ();
		jdic.setVisible (true);
	}
}

////////////////////////////////////////////////////////////////
class PanelWords extends JPanel {
	Vector wordsList = new Vector ();
	JList wordsArea = new JList (wordsList);

	public PanelWords () {
		wordsArea.setBackground (Color.BLACK); 
		wordsArea.setForeground (Color.CYAN); 
		add (wordsArea);
	}
	public void add (String words) {
		wordsList.add (words);
		remove (wordsArea);
		wordsArea = new JList (wordsList);
		add (wordsArea);
	}
	public void remove () {
		wordsList.clear ();
		remove (wordsArea);
		wordsArea = new JList (wordsList);
		add (wordsArea);
	}
}
////////////////////////////////////////////////////////////////
class PanelCommands extends JPanel implements ActionListener {
	JDicCtrl controller;
	JButton newButton;
	JButton randomButton;

	public PanelCommands (JDicCtrl controller) {
		this.controller = controller;
		newButton = new JButton("New");
		randomButton = new JButton("Random");
		newButton.addActionListener (this);
		randomButton.addActionListener (this);
		add (newButton);
		add (randomButton);
	}

	public void actionPerformed (ActionEvent e) {
		if (e.getSource () == newButton)
			controller.newGameEvent ("new");
		if (e.getSource () == randomButton)
			controller.newGameEvent ("random");
	}
}
		
////////////////////////////////////////////////////////////////
// String with language attribute
////////////////////////////////////////////////////////////////
class StringDic {
	String word; 
	String language; // english, spanish

	public StringDic (String word, String language) {
		this.word = word;
		this.language = language;
	}
}


////////////////////////////////////////////////////////////////
// Handle the words of the dictionary
////////////////////////////////////////////////////////////////
class Words {
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
}

////////////////////////////////////////////////////////////////

class PanelGrid extends JPanel {
	JDicCtrl controller;
	Words words;

	Square firstButton, secondButton, nextButton;
	boolean flagNewButton = false;
	
	public PanelGrid (JDicCtrl controller, Words words) {
		super();
		this.controller = controller;
		this.words = words;
		setLayout (new BorderLayout());
		putWords ();
	}

	public void putWords () {
		int rows = 5;
		int files = 6;

		setLayout (new GridLayout (rows, files));

		ArrayList <String>  arrayWords = words.getString ();
		Collections.shuffle (arrayWords);

		Controller controller = new Controller ();
		int k = 0;
		for (int i=0; i < files; i++)
			for (int j=0; j < rows; j++) {
				Square button = new Square ((String) arrayWords.get (k++));
				button.addActionListener (controller);
				add (button);
			}
	}

	public class Controller implements ActionListener {
		public void actionPerformed (ActionEvent e) {
			if (firstButton == null) {
				firstButton = (Square)e.getSource();
				firstButton.change (true);
				Speak.speak (firstButton.getWord());
			}
			else {
				if (secondButton == null) {
					flagNewButton = false;
					secondButton = (Square) e.getSource();
					secondButton.change (true);
					Check check = new Check (firstButton, secondButton);
					check.start();
					check = null;
				} else {
					flagNewButton = true;
					nextButton = (Square) e.getSource();
					nextButton.change (true);
					Speak.speak (nextButton.getWord());
				}
			}
		}
	}
	///////////////////////////////////////////////////////////////////
	// Class to check if there is match
	///////////////////////////////////////////////////////////////////
	public class Check extends Thread {
		Square first, second;
		public Check (Square first, Square second) {
			super();
			this.first = first;
			this.second = second;
		}
		public void run () {
		  try {
			String firstWord = firstButton.getWord();
			String secondWord = secondButton.getWord();
			if (firstWord.equals (words.get (secondWord))) {
				firstButton.setEnabled (false);
				secondButton.setEnabled (false);
				nextButton = null;
				String example = words.getExample (secondWord);
				controller.wordsMatchedEvent (firstWord, secondWord, example);
			} else {
				Speak.speak (second.getWord());
				while (flagNewButton == false)
					Thread.sleep (100);

				firstButton.change (false);
				secondButton.change (false);
			}
			firstButton = nextButton;
			secondButton = null;
		  } catch (java.lang.InterruptedException e) {e.printStackTrace();}
		}
	}
}

////////////////////////////////////////////////////////////////
// Speak a string
class Speak {
	public static void speak (String word) {
		Runtime run = Runtime.getRuntime (); 
		try {
			String[] cmd = {"espeak", "-g", "10",  word};
			run.exec (cmd);
		} catch (Exception e) {e.printStackTrace (); }
	}
	public static void speakAllWords (ArrayList <String> arrayOfWords) {
	  try {
		int i=0;
		while (i < arrayOfWords.size() ) {
			String word = arrayOfWords.get (i++);
			System.out.println (word);
			speak (word);
			Thread.sleep (1500);
		}
	  } catch (Exception ex) {ex.printStackTrace();}
	}
}

////////////////////////////////////////////////////////////////
// Class representing the buttons of the square game
////////////////////////////////////////////////////////////////
class Square extends JButton {
	String word;
	String languajeOfWord;
	
	public Square (String word) {
		super (".");
		this.word = word;
		setBackground (Color.BLACK); 
		setForeground (Color.CYAN); 
	}

	public String getWord () {
		return word;
	}

	public void change (boolean value) {
		if (value) {
			setText (word);
			repaint();
		}
		else 
			setText (".");
	}
}


