package connectfour;

public class Board {
  private char[][] board;
  int n;
  private int[] rows;
  public Board(int n){
    this.n = n;
    this.initializeBoard();
    this.initializeRows();
  }

  private void initializeRows(){
    this.rows = new int[n];
    for(int i=0; i<n; i++){
      rows[i] = n - 1;
    }
  }

  private void initializeBoard(){
    this.board = new char[n][n];
    for(int i = 0; i<n; i++){
      for(int j=0; j<n; j++){
        board[i][j] = '-';
      }
    }
  }

  private boolean isColFull(int columnNumber){
    return board[0][columnNumber] != '-';
  }

  private boolean hasAvailableSpace(){
    for(int i=0; i<n; i++){
      if(!isColFull(i)){
        return true;
      }
    }
    return false;
  }

  public boolean canStillPlay(){
    if(!hasAvailableSpace()){
      return false;
    }
    return true;
  }

  public char[][] getBoard(){
    return board;
  }
}