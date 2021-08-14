package deckofcards;

public abstract class Card {
	
	private int faceValue;
	private Suit suit;
	
	
	public Card(int fv,Suit s) {
		
		this.faceValue = fv;
		this.suit = s;
		
	}
	
	public abstract int value();
	
	public Suit getSuit() {
		return suit;
	}

	

}
