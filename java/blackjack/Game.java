package blackjack;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Game {
	private ArrayList<Player> players;
	private CardGenerator cardGen;

	public Game() {
		cardGen = new CardGenerator();
		players = new ArrayList<>();
	}

	public void requestPlayers(int playerCount, Scanner input) {
		for (int i = 0; i < playerCount; i++) {
			System.out.printf("Please input the name of player %d: ", i + 1);
			String name = input.next();
			this.players.add(new Player(name));
		}
	}

	public void requestPlayers(Scanner input) {
		int playerCount = 2;
		System.out.print("How many players are there: ");
		try {
			playerCount = input.nextInt();
		} catch (InputMismatchException e) {
			System.out.println("Input wasn't a number, resorting to 2 players!");
		}
		this.requestPlayers(playerCount, input);
	}

	public ArrayList<Card> getAllCards() {
		return cardGen.generateCards();
	}

	private int getPlayerByName(String playerName) {
		for (int i = 0; i < players.size(); i++) {
			if (players.get(i).getName().equals(playerName)) {
				return i;
			}
		}
		return -1;
	}

	private boolean inPlayers(String playerName) {
		return getPlayerByName(playerName) != -1;
	}

	public void deal(String playerName) {
		if (inPlayers(playerName)) {
			int randomCardIndex = (int) (Math.random() * getAllCards().size());
			players.get(getPlayerByName(playerName)).addCard(getAllCards().get(randomCardIndex));
			getAllCards().remove(randomCardIndex);
		}
	}

	private boolean donePlaying() {
		for (Player player : players) {
			if (player.hasBusted()) {
				return true;
			}
		}
		return false;
	}

	private Player alternate(Player previousPlayer) {
		if (players.get(players.size() - 1).getName().equals(previousPlayer.getName())
				&& players.get(players.size() - 1).stillPlaying()) {
			return players.get(0);
		}
		for (int i = 0; i < players.size() - 1; i++) {
			if (players.get(i).getName().equals(previousPlayer.getName())) {
				return players.get(i + 1);
			}
		}
		return null;
	}

	private String findWinnerByNonBust() {
		HashMap<String, Integer> playerValues = new HashMap<>();
		for (Player player : players) {
			if(!player.hasBusted()){
				playerValues.put(player.getName(), player.handValue());
			}
		}
		
		int maxValue = Collections.max(playerValues.values());
		for (String playerName : playerValues.keySet()) {
			if (playerValues.get(playerName).equals(maxValue)) {
				return playerName;
			}
		}
		return "";
	}

	public void play() {
		boolean endedByBust = true;
		try (Scanner input = new Scanner(System.in)) {
			requestPlayers(input);

			Player currPlayer = players.get(0);
			for (int count = 0; count < players.size() * 2; count++) {
				deal(currPlayer.getName());
				System.out.printf("Player %s's Hand: ", currPlayer.getName());
				for (Card card : currPlayer.getHand()) {
					System.out.printf(" %s", card.getCardValue());
				}
				System.out.printf("%nTotal Card Values for Player %s: %d%n%n", currPlayer.getName(), currPlayer.handValue());
				currPlayer = alternate(currPlayer);
			}
			while (!donePlaying()) {
				if (currPlayer == null) {
					endedByBust = false;
					break;
				}
				int choice = currPlayer.choice(currPlayer, input);
				switch (choice) {
				case 1:
					deal(currPlayer.getName());
					System.out.printf("Player %s's Hand: ", currPlayer.getName());
					for (Card card : currPlayer.getHand()) {
						System.out.printf(" %s", card.getCardValue());
					}
					System.out.printf("%nTotal Card Values for Player %s: %d%n%n", currPlayer.getName(), currPlayer.handValue());
					currPlayer = alternate(currPlayer);
					break;
				case 2:
					currPlayer.toggleKeepPlaying();
					currPlayer = alternate(currPlayer);
					break;
				default:
					break;
				}
			}
			if (endedByBust) {
				for (Player player : players) {
					if (player.hasBusted()) {
						System.out.printf("%s has busted and lost!%n", player.getName());
						break;
					}
				}
			}

			String playerName = findWinnerByNonBust();
			for (Player player : players) {
				if (player.getName().equals(playerName)) {
					System.out.printf("Player %s has won with %d!%n", player.getName(), player.handValue());
					return;
				}
			}

		}

	}

}