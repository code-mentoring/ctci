#pragma once
#include <string>
#include <vector>

enum class Suit { SPADE, CLUB, HEART, DIAMOND };
enum class Face { ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING };

std::vector<Suit> allSuits();
std::vector<Face> allFaces();

using stringPair = std::pair<std::string,std::string>;

class Card
{
public:
    Card() = delete;
    //Card(const Card &card) = delete; // copy constructor
    //Card &operator=(const Card &card) = delete; // copy assignment

    Card(Suit suit, Face face) : suit_(suit) , face_(face) {}

    Suit suit() const { return suit_; }
    Face face() const { return face_; } 

    std::string toString() const 
    {
        return faceToStringPair(face_).second + " of " + suitToStringPair(suit_).second;
    }

    std::string toStringShort() const
    {
        return faceToStringPair(face_).first + suitToStringPair(suit_).first;
    }

    stringPair faceToStringPair(Face face) const
    {
        switch (face)
        {
            case Face::ACE:   return stringPair("A", "ACE"); 
            case Face::TWO:   return stringPair("2", "TWO"); 
            case Face::THREE: return stringPair("3", "THREE"); 
            case Face::FOUR:  return stringPair("4", "FOUR"); 
            case Face::FIVE:  return stringPair("5", "FIVE"); 
            case Face::SIX:   return stringPair("6", "SIX"); 
            case Face::SEVEN: return stringPair("7", "SEVEN"); 
            case Face::EIGHT: return stringPair("8", "EIGHT"); 
            case Face::NINE:  return stringPair("9", "NINE"); 
            case Face::TEN:   return stringPair("X", "TEN"); 
            case Face::JACK:  return stringPair("J", "JACK"); 
            case Face::QUEEN: return stringPair("Q", "QUEEN"); 
            case Face::KING:  return stringPair("K", "KING"); 
        }
    }

    stringPair suitToStringPair(Suit suit) const
    {
        switch (suit)
        {
            case Suit::SPADE:   return stringPair("S", "SPADES");
            case Suit::CLUB:    return stringPair("C", "CLUBS");
            case Suit::HEART:   return stringPair("H", "HEARTS");
            case Suit::DIAMOND: return stringPair("D", "DIAMONDS");
        }
    }

private:
    Suit suit_;
    Face face_;
};

inline bool operator==(const Card &c1, const Card &c2)
{
    return c1.face() == c2.face() && c1.suit() == c2.suit();
}

inline bool operator!=(const Card &c1, const Card &c2)
{
    return !(c1==c2);
}
