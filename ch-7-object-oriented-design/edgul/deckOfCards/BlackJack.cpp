#include "BlackJack.h"


BlackJack::BlackJack(uint8_t players) :
    drawDeck_(DeckInit::FULL)
{
    for (int i = 0; i < players; ++i) 
    {
        playersDeck_.push_back(std::move(Deck()));
    }
}

void BlackJack::start()
{
    // deal to all the players
    for (Deck &playerDeck : playersDeck_)
    {
        playerDeck.add(drawDeck_.removeFirst());
        playerDeck.add(drawDeck_.removeFirst());
    }
      
    // ask each player what to do until they pass
    
    // dealer hits
    
    // evaluate winner
}
