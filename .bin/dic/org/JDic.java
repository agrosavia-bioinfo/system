import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.lang.*;
import java.io.*;

// Controller for JDic class
interface JDicCtrl {
		public void newGameMSG ();
		public void randomWordsMSG ();
		public void matchMSG (String first, String second);
}

////////////////////////////////////////////////////////////////
public class JDic extends JFrame implements JDicCtrl {
	JDicCtrl controller = this;
	Words words = new Words ();
	PanelCommands commands = new PanelCommands (controller);
	PanelGrid grid = new PanelGrid (controller, words);
	PanelWords wordsPanel = new PanelWords ();

	public void newGameMSG () {
		remove (grid);
		wordsPanel.remove ();
		grid = new PanelGrid (controller, words);
		add (grid, "Center");
		setVisible (true);
	}

	public void randomWordsMSG () {
		remove (grid);
		wordsPanel.remove ();
		words.loadRandomWords ();
		grid = new PanelGrid (controller, words);
		add (grid, "Center");
		setVisible (true);
	}

	public void matchMSG (String first, String second) {
		String s1s2 = first + " : " + second;
		wordsPanel.add (s1s2);
		setVisible (true);
		System.out.println (first + " : " + second);
	}

	public JDic () {
		super ("LG Dictionary");
		add (commands, "North");
		add (grid, "Center");
		add (wordsPanel, "South");
		setSize (800,400);
		setLocation (1,1);
		setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
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
			controller.newGameMSG ();
		if (e.getSource () == randomButton)
			controller.randomWordsMSG ();
	}
}
		
////////////////////////////////////////////////////////////////
class Words {
	HashMap <String, String> wordsMap = new HashMap < String, String>();

	public Words () {
		loadWords ();
	}

	public String get (String word) {
		return wordsMap.get (word);
	}

	public ArrayList <String> getString () {
		return new ArrayList (wordsMap.keySet ());
	}

	public void loadWords () {
		try {
			BufferedReader bf = new BufferedReader (new FileReader ("words.txt"));

			String text = null;
			int k = 0;
			for (int i=0; i < 10; i++) {
				text = bf.readLine();
				String english = text.split(":")[0];	
				String spanish = text.split(":")[1];	
				wordsMap.put (english, spanish);
				wordsMap.put (spanish, english);
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
			for (int i=0; i < 10; i++) {
				text = wordList.get (i);
				String english = text.split(":")[0];	
				String spanish = text.split(":")[1];	
				wordsMap.put (english, spanish);
				wordsMap.put (spanish, english);
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
		int rows = 4;
		int files = 5;

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
				}
			}
		}
	}

	public class Check extends Thread {
		Square first, second;
		public Check (Square first, Square second) {
			super();
			this.first = first;
			this.second = second;
		}
		public void run () {
			String firstWord = firstButton.getWord();
			String secondWord = secondButton.getWord();
			if (firstWord.equals (words.get (secondWord))) {
				firstButton.setEnabled (false);
				secondButton.setEnabled (false);
				nextButton = null;
				controller.matchMSG (firstWord, secondWord);
			} else {
				while (flagNewButton == false)
					try {
						Thread.sleep (100);
					} catch (Exception ex) {ex.printStackTrace();}
				
				firstButton.change (false);
				secondButton.change (false);
			}
			firstButton = nextButton;
			secondButton = null;
		}
	}
}

////////////////////////////////////////////////////////////////
class Square extends JButton {
	String word;
	
	public Square (String word) {
		super (".");
		this.word = word;
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


