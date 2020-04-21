import { Player, Game } from ".";
class Driver {
  public static main = (): void => {
    let player1 = new Player("Edward");
    let player2 = new Player("Kevin");
    let game = new Game([player1, player2]);

    game.start();
    game.showHands();
  };
}

Driver.main();
