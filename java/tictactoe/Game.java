package tictactoe;

import java.util.Scanner;

import tictactoe.exceptions.OccupiedError;

public class Game {
	Board board;

	public Game() {
		this.board = new Board();
	}

	private void initializePlayers(Player[] players, Scanner input) {
		for (int i = 0; i < 2; i++) {
			System.out.print("Please input your player name: ");
			String name = input.next();
			System.out.print("Please input your marker: ");
			String marker = input.next();
			players[i] = new Player(name, marker);
		}
	}

	private Player alternate(Player curr) {
		if (curr == this.board.getPlayers()[0]) {
			return this.board.getPlayers()[1];
		}
		return this.board.getPlayers()[0];
	}

	private int[] requestPlay(Scanner input) {
		int x = 0, y = 0;
		try {
			System.out.print("Please input your x coordinate: ");
			x = input.nextInt();
			System.out.print("Please input your y coordinate: ");
			y = input.nextInt();
		} catch (Exception e) {
			return requestPlay(input);
		}
		return new int[] { x, y };
	}

	public void play() {
		try (Scanner input = new Scanner(System.in)) {
			Player[] players = board.getPlayers();
			initializePlayers(players, input);
			Player currentPlayer = players[0];
			boolean validPlay = false;
			while (board.stillPlaying()) {
				board.printBoard();
				while(!validPlay){
					int[] play = requestPlay(input);
					try {
						board.draw(currentPlayer, play[0], play[1]);
						validPlay = true;
					} catch (OccupiedError e) {
						System.out.println("Invalid location! Try again!");
					}
				}
				currentPlayer = alternate(currentPlayer);
				validPlay = false;
			}
			Player winner = board.getWinner();
			if(winner == null){
				System.out.println("No winner! Tie!");
			} else {
				System.out.printf("Winner is: %s!%n", winner.getName());
			}
		}
	}
}