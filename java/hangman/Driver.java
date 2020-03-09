package hangman;

import java.nio.file.Paths;
import java.util.Scanner;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class Driver {

	private static String parseFile() throws IOException {
		return Files.readString(Paths.get("./words.csv"), StandardCharsets.UTF_8);
	}
	// java/hangman/words.txt

	public static Word getRandomWord() {
		try {
			String words = parseFile();
			String[] wordsArray = words.split(",\n");
			int index = (int) (Math.random() * wordsArray.length);
			return new Word(wordsArray[index]);
		} catch (IOException e) {
			System.out.println("File not found!");
		}
		return new Word("Default");
	}

	public static boolean isNotOver(Word word) {
		return !word.guessed() && word.getGuessesLeft() != 0;
	}

	public static void main(String[] args) {
		Word word = getRandomWord();

		try (Scanner scanner = new Scanner(System.in)) {
			// while(isNotOver(word)){
			while (true) {
				word.printCurrent();
				word.printFailed();
				System.out.print("Guess a letter: ");
				char val = scanner.next().charAt(0);
				word.guess(val);
				System.out.println();
				if(word.guessed() || word.getGuessesLeft() == 0){
					break;
				}
			}
			System.out.println("You used " + word.getGuessesUsed() + " extra character(s)!");
		}

	}
}