#pragma once
#include "Call.h"

class CallHandler
{
public:
    bool busy() const { return busy_; }
protected:
    CallLevel level_;    
    bool busy_;
};

class Responder : public CallHandler
{
    Responder() 
    { 
        level_ = CallLevel::LOW;
        busy_ = false;
    }
};

class Manager : public CallHandler
{
    Manager() 
    { 
        level_ = CallLevel::MEDIUM; 
        busy_ = false;
    }
};

class Director : public CallHandler
{
    Director() 
    { 
        level_ = CallLevel::HIGH; 
        busy_ = false;
    }
};
