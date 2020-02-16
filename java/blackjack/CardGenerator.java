package blackjack;

import java.util.ArrayList;

public class CardGenerator {
	private ArrayList<Card> cards;

	public CardGenerator() {
		this.cards = this.generateCards();
	}

	public ArrayList<Card> generateCards() {
		String[] suits = new String[] { "♠", "♥", "♦", "♣" };
		String[] values = new String[] { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
		ArrayList<Card> deck = new ArrayList<>();
		for (String suit : suits) {
			for (String value : values) {
				deck.add(new Card(suit, value));
			}
		}
		return deck;
	}

	public ArrayList<Card> getCards() {
		return this.cards;
	}

	private void swap(int origin, int swapped) throws IndexOutOfBoundsException {
		if (origin < 0 || swapped > 52) {
			throw new IndexOutOfBoundsException();
		}
		Card temp = cards.get(origin);
		cards.set(origin, cards.get(swapped));
		cards.set(swapped, temp);
	}

	public void shuffleCards() {
		try {
			for (int i = 0; i < 52; i++) {
				this.swap(i, (int) (Math.random() * 52));
			}
		} catch (IndexOutOfBoundsException e) {
			return;
		}
	}
}