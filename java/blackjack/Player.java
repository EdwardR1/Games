package blackjack;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Player {
	private String name;
	private ArrayList<Card> hand;
	private boolean keepPlaying;

	public Player(String name, ArrayList<Card> hand) {
		this.name = name;
		this.hand = hand;
		this.keepPlaying = true;
	}

	public Player(String name) {
		this(name, new ArrayList<>());
	}

	public void toggleKeepPlaying(){
		keepPlaying = !keepPlaying;
	}
	public boolean stillPlaying(){
		return this.keepPlaying;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public ArrayList<Card> getHand() {
		return hand;
	}

	public void setHand(ArrayList<Card> hand) {
		this.hand = hand;
	}

	public int handValue() {
		int sum = 0;
		for (Card card : hand) {
			sum += card.parseValue();
		}
		return sum;
	}

	public boolean hasBusted() {
		return this.handValue() > 21;
	}

	public void addCard(Card card) {
		this.hand.add(card);
	}

	private void printMenu() {
		HashMap<Integer, String> options = new HashMap<>();
		options.put(1, "Hit Me!");
		options.put(2, "Stay");
		System.out.println("Options: ");
		for (var option : options.entrySet()) {
			System.out.printf("%d: %s%n", option.getKey(), option.getValue());
		}
	}

	public int choice(Player currPlayer, Scanner userInput) {
		int value = 1;
		System.out.printf("Player: %s%n", currPlayer.getName());

		printMenu();
		System.out.print(">> ");
		try {
			if (userInput.hasNextLine())
				value = userInput.nextInt();
			else
				value = userInput.nextInt();
		} catch (InputMismatchException e) {
			System.out.println("Invalid answer! Try again");
			return choice(currPlayer, userInput);
		}
		return value;

	}

}