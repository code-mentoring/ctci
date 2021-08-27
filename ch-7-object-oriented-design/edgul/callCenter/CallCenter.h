#pragma once

#include <vector>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <chrono>
#include <thread>
#include <optional>
#include "Call.h"
#include "CallHandler.h"


class CallCenter
{
public:
    void start();
    
private:
    std::vector<int> incomingCalls_;
    std::queue<Call> waitingCalls_;
    std::vector<CallHandler> handlers_;

    bool allHandlersFree();

    int secondsSinceEpoch();

    void dispatchCall();
    void dispatchLoop();

};
