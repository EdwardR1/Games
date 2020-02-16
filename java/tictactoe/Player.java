package tictactoe;

public class Player {
	private String name;
	private String marker;

	public Player(String name, String marker) {
		this.name = name;
		this.marker = marker;
	}

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getMarker() {
		return this.marker;
	}

	public void setMarker(String marker) {
		this.marker = marker;
	}
}