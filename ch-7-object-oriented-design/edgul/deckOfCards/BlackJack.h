#pragma once

#include "Deck.h"

class BlackJack
{
public:
    BlackJack(uint8_t players);
    void start();
private:
    Deck drawDeck_;
    Deck dealerDeck_;
    std::vector<Deck> playersDeck_;
};
