import { Player, CardGenerator, Card } from '.';
class Game {
  private players: Array<Player>;
  private deck: Array<Card>;

  constructor(players: Array<Player>){
    this.players = players;
    this.deck = CardGenerator.Generate();
  }

  private deal = (player: Player): void => {
    let index: number = Math.random() * this.deck.length;
    player.addCard(this.deck[index]);
    console.log(this.deck[index]);
    this.deck.splice(index, 1);
  }

  public start = (): void => {
    this.players.forEach(player => {
      this.deal(player);
      this.deal(player);
    })
  }

  public showHands = (): void => {
    this.players.forEach(player => console.log(player.toString()));
  }
}
export { Game };