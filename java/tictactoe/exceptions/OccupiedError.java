package tictactoe.exceptions;
public class OccupiedError extends Exception {
	private String message;

	public OccupiedError(String message){
		this.message = message;
	}
	public OccupiedError(){
		this("Space is Occupied!");
	}

	public String toString(){
		return this.message;
	}

	
}