package card;

public class BlackJack extends Card {

	public BlackJack(int n, Suit suit) {
		super(n, suit);
		// TODO Auto-generated constructor stub
	}
	
	public int value() {
		int v = super.getCardNumber();
		if (v==1) {
			return 11;
		}
		else if(v<10) {
			return v;
		}
		return 10;
	}

}
