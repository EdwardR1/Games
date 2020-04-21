import { Card } from ".";
class Player {
  private hand: Array<Card>;
  private name: string;
  constructor(name: string) {
    this.name = name;
    this.hand = new Array<Card>();
  }
  get score(): number {
    let total: number = 0;
    this.hand.forEach((card) => (total += card.value));
    return total;
  }

  get bust(): boolean {
    return this.score > 21;
  }

  public addCard = (card: Card): void => {
    this.hand.push(card);
  };

  public toString = (): string => {
    let str = this.name;
    str += ":";
    this.hand.forEach((card) => {
      str += " ";
      str += `${card}`;
    });
    return str;
  };
}

export { Player };
