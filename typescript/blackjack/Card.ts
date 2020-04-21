class Card {
  private _suit: string;
  private _value: string;

  constructor(suit: string, value: string) {
    this._suit = suit;
    this._value = value;
  }

  get value(): number {
    switch (this._value) {
      case "K":
      case "Q":
      case "J":
        return 10;
      case "A":
        return 1;
      default:
        parseInt(this._value);
    }
  };

  public toString = (): string => this._suit + this._value;
}

export { Card };
