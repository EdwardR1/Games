package hangman;
import java.util.ArrayList;
public class Word {
	private String words;
	private char[] spaces;
	private char[] shown;
	private ArrayList<Character> failed;
	public static final int GUESSES = 15;
 
	public Word(String words){
		this.words = words.toLowerCase();
		this.spaces = words.toCharArray();
		this.setShown();
		this.failed = new ArrayList<>();
	}

	private boolean isChar(char chr){
		return Character.isLetter(chr);
	}

	private void setShown(){
		this.shown = new char[spaces.length];
		for(int i=0; i<shown.length; i++){
			if(isChar(spaces[i])){
				shown[i] = '*';
			} else {
				shown[i] = spaces[i];
			}
		}
	}

	private boolean inWords(char check){
		return words.contains("" + check);
	}

	private ArrayList<Integer> locations(char check){
		ArrayList<Integer> indexes = new ArrayList<>();
		for(int i=0; i<spaces.length; i++){
			if(spaces[i] == check){
				indexes.add(i);
			}
		}
		return indexes;	
	}

	public void guess(char guess){
		if(inWords(guess)){
			for(var i : locations(guess)){
				shown[i] = guess;
			}
		} else {
			addFailed(guess);
		}
	}

	private void addFailed(char guess){
		if(!failed.contains(guess))
			failed.add(guess);
	}

	public void printCurrent(){
		System.out.print("Word: ");
		for(char chr : shown){
			System.out.print(chr);
		}
		System.out.println();
	}

	public void printFailed(){
		System.out.print("Failed: ");
		for(Character chr : failed){
			System.out.print(chr + " ");
		}
		System.out.println();
	}

	public int getGuessesUsed(){
		return failed.size();
	}

	public int getGuessesLeft(){
		return GUESSES - getGuessesUsed();
	}

	public boolean guessed(){
		for(int i=0; i<shown.length; i++){
			if(shown[i] != spaces[i]){
				return false;
			}
		}
		return true;
	}

	
}