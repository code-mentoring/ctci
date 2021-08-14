package deckofcards;

public enum Suit {
	
	Heart(0), Spade(1),Diamond(2),Club(3);
	
	private int value;

	Suit(int v) {
		// TODO Auto-generated constructor stub
		
		this.value = v;
	}

	public int getValue() {
		return value;
	}

	
}
