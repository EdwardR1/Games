import { Card, Player } from '.';
class CardGenerator {
  public static Generate = (): Array<Card> => {
    let deck: Array<Card> = new Array<Card>();
    let suits = ["♤", "♡", "♢", "♧"]
    let values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits.forEach(suit => {
      values.forEach(value => {
        deck.push(new Card(suit, value));
      })
    })
    return deck;
  }

}
export { CardGenerator };