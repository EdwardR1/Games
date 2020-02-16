package tictactoe;

import java.util.ArrayList;

import tictactoe.exceptions.OccupiedError;

public class Board {
	private Player[] players;

	String[][] board;

	public Board() {
		players = new Player[2];
		board = new String[][] { { "_", "_", "_" }, { "_", "_", "_" }, { "_", "_", "_" } };
	}

	public Player[] getPlayers() {
		return players;
	}

	public String[][] getBoard() {
		return board;
	}

	public Player getPlayerByName(String name) {
		for (Player player : players) {
			if (player.getName().equals(name)) {
				return player;
			}
		}
		return null;
	}

	private boolean free(int x, int y) {
		if (board[x][y].equals("_")) {
			return false;
		}
		return true;
	}

	private boolean winHorizontal(Player player) {
		String marker = player.getMarker();
		for (int x = 0; x < 3; x++) {
			if (board[x][0].equals(marker) && board[x][1].equals(marker) && board[x][2].equals(marker)) {
				return true;
			}
		}
		return false;
	}

	private boolean winVertical(Player player) {
		String marker = player.getMarker();
		for (int y = 0; y < 3; y++) {
			if (board[0][y].equals(marker) && board[1][y].equals(marker) && board[2][y].equals(marker)) {
				return true;
			}
		}
		return false;
	}

	private boolean winDiagonal(Player player) {
		String marker = player.getMarker();
		if (board[0][0].equals(marker) && board[1][1].equals(marker) && board[2][2].equals(marker)) {
			return true;
		} else if (board[2][0].equals(marker) && board[1][1].equals(marker) && board[0][2].equals(marker)) {
			return true;
		}
		return false;
	}

	private boolean canStillPlay() {
		int count = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (board[i][j].equals("_")) {
					count++;
				}
			}
		}
		return count != 0;
	}

	public boolean stillPlaying() {
		for (Player player : players) {
			if (winHorizontal(player) || winVertical(player) || winDiagonal(player) || !canStillPlay()) {
				return false;
			}
		}
		return true;
	}

	public Player getWinner() {
		if (!stillPlaying()) {
			for (Player player : players) {
				if (winHorizontal(player) || winVertical(player) || winDiagonal(player)) {
					return player;
				}
			}
		}
		return null;
	}

	public void draw(Player player, int x, int y) throws OccupiedError {
		if (!free(x, y)) {
			throw new OccupiedError();
		} else {
			board[x][y] = player.getMarker();
		}
	}

	public void printBoard() {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(board[i][j] + " ");
			}
			System.out.println();
		}
	}
}