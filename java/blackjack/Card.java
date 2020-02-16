package blackjack;

public class Card {
	private String suit;
	private String value;

	public Card(String suit, String value) {
		this.suit = suit;
		this.value = value;
	}

	public String getSuit() {
		return suit;
	}

	public void setSuit(String suit) {
		this.suit = suit;
	}

	public String getValue() {
		return value;
	}

	public void setValue(String value) {
		this.value = value;
	}

	public String getCardValue() {
		return this.suit + " " + this.value;
	}

	public int parseValue() {
		switch (value) {
		case "A":
			return 1;
		case "K":
		case "Q":
		case "J":
			return 10;
		default:
			return Integer.parseInt(value);
		}
	}
}