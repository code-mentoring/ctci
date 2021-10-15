#pragma once
#include <vector>
#include <iostream>
#include <cstdlib>
#include <time.h>
#include <algorithm>
#include <assert.h>
#include "Card.h"

enum class DeckInit { EMPTY, FULL };
//enum class DeckType { FACE_UP, FACE_DOWN }

class Deck
{
public:
    Deck() {};
    Deck(DeckInit deckType)
    {
        // default empty deck
        if (deckType == DeckInit::FULL)
        {
            cards_ = standardDeck();
        }
    }

    void add(const Card &card)
    {
        cards_.push_back(card);
    }

    Card peek()
    {
        assert(!cards_.empty());
        return cards_.at(0);
    }

    Card removeFirst()
    {
        assert(!cards_.empty());
        Card card = cards_.at(0);
        cards_.erase(std::find(cards_.begin(), cards_.end(), card));
        return card;
    }

    void clear()
    {
        cards_.erase(cards_.begin(), cards_.end());
    }

    void shuffle()
    {
        std::vector<Card> hat = cards_;
        cards_.clear();

        srand (time(nullptr));
        while (!hat.empty())
        {
            int i = rand() % hat.size();  
            auto iter = std::find(hat.begin(), hat.end(), hat.at(i));
            cards_.push_back(*iter);
            hat.erase(iter);
        }
    }

    void print()
    {
       for (const Card &c : cards_)
       {
           std::cout << c.toStringShort() << "\n";
       }
    }

    static std::vector<Card> standardDeck()
    {
        std::vector<Card> all;
        for ( const Suit &s : allSuits())
        {
            for (const Face &f: allFaces())
            {
                all.push_back(Card(s,f));
            }
        }
        return all;
    }

private:
    std::vector<Card> cards_;
};
