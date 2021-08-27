#pragma once
#include "Call.h"

class CallHandler
{
public:
    CallHandler(const CallLevel &level) : level_(level), busy_(false) {}
    bool busy() const { return busy_; }
    const CallLevel & callLevel() const { return level_; }
    bool process(const Call &call)
    {
       if (static_cast<int>(call.level()) > static_cast<int>(level_))
       {
           // not authorized to handle call 
           return false;
       }
       call.process();
       return true;
    }
protected:
    CallLevel level_;    
    bool busy_;
};

