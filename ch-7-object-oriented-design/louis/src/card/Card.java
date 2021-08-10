package card;
public class Card {
public enum Suit{
	
	Diamonds(0),
	Hearth(1),
	Spades(2),
	Clubs(4);
	
	int v ;
	
	private Suit(int value) {
		this.v =value;
	}
	
}
int cardNumber;
public int getCardNumber() {
	return cardNumber;
}
public Suit getS() {
	return s;
}
private Suit s;
public Card(int n,Suit suit) {
	this.cardNumber = n;
	this.s = suit;
}
}
