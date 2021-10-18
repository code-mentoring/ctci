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

int main(int argc, char **argv)
{
    //testStack();
    testTower();
    return 0;
}
