#include <iostream>
#include "Stack.h"
#include "Tower.h"

void testStack(){
    Stack<int> s;
    s.push(1);
    s.print();
    s.push(2);
    s.print();
    s.push(3);
    s.print();
    std::cout << "Length: " << s.length() << std::endl;
    auto opt = s.pop();
    s.print();
    std::cout << "Opt valid: " << opt.has_value() << " with Value: " << opt.value() << std::endl;
    s.pop();
    s.pop();
    s.print();
    std::cout << "Length: " << s.length() << std::endl;
    opt = s.pop();
    std::cout << "Opt valid: " << opt.has_value() << std::endl;
}

void testTower(){
    Tower t(3);
    t.print();
    t.move(Tower::Pole::LEFT, Tower::Pole::RIGHT);
    t.print();
    t.move(Tower::Pole::LEFT, Tower::Pole::RIGHT); // won't move
    t.print();
    t.move(Tower::Pole::LEFT, Tower::Pole::MID); 
    t.print();
}

void moveStack(Tower &t, int n, Tower::Pole src, Tower::Pole dest) {
    if (n <= 0) return;
    Tower::Pole other = Tower::otherPole(src, dest);    
    moveStack(t, n-1, src, other);
    t.move(src, dest);
    //t.print(); // prints progress
    moveStack(t, n-1, other, dest);
}

int main(int argc, char **argv)
{
    //testStack();
    //testTower();
    Tower t(4);
    t.print();
    moveStack(t, 
              t.rings[Tower::Pole::LEFT]->length(), 
              Tower::Pole::LEFT, Tower::Pole::RIGHT);
    t.print();
    return 0;
}
