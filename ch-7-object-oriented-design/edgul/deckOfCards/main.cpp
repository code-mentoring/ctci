#include <iostream>
#include <assert.h>
#include "Card.h"
#include "Deck.h"

void basicTesting();

int main(int argc, char *argv[])
{
    
    basicTesting();
        
    return 0;
}

void basicTesting()
{
    Card ace(Suit::SPADE, Face::ACE);
    Card two(Suit::SPADE, Face::TWO);
    Card three(Suit::SPADE, Face::THREE);
    Card fourHearts(Suit::HEART, Face::FOUR);

    Deck d;
    d.add(ace);
    d.add(two);
    d.add(three);
    d.add(fourHearts);
    d.print();

    d.shuffle();
    std::cout << "After shuffle:\n";
    d.print();
   
    d.removeFirst();
    std::cout << "After remove first\n";
    d.print();
    std::cout << "Peeking: " << d.peek().toStringShort() << "\n";
}
