package deckofcards;

import java.util.ArrayList;

public class Deck <T extends Card> {

	
	private ArrayList<T> Card;

	public Deck(ArrayList<T> c) {
		this.Card = c;
	}
}
