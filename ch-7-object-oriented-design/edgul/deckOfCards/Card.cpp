#include "Card.h"

std::vector<Suit> allSuits()
{
    return { Suit::SPADE, Suit::CLUB, Suit::HEART, Suit::DIAMOND };
}

std::vector<Face> allFaces()
{
    return { Face::ACE, 
             Face::TWO, 
             Face::THREE, 
             Face::FOUR, 
             Face::FIVE, 
             Face::SIX, 
             Face::SEVEN, 
             Face::EIGHT, 
             Face::NINE, Face::TEN, Face::JACK, Face::QUEEN, Face::KING }; 
}
