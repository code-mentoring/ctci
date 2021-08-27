#pragma once

#include <vector>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <chrono>
#include <thread>
#include "Call.h"
#include "CallHandler.h"


class CallCenter
{
public:
    void start()
    {
        // load incoming calls list        
        for (int i = 0; i < 10; ++i)
        {
            srand(time(0));
            int timeToNextCall = rand() % 10;
            incomingCalls_.push_back(timeToNextCall);
        }

        // init with some already waiting calls
        waitingCalls_.push(std::move(Call(CallLevel::LOW)));
        waitingCalls_.push(std::move(Call(CallLevel::MEDIUM)));
        waitingCalls_.push(std::move(Call(CallLevel::HIGH)));

        int secondsSinceLastCaller = secondsSinceEpoch();

        while (!incomingCalls_.empty() &&
               !waitingCalls_.empty()  &&
               !allHandlersFree())
        {
            // enough time has elapsed add next caller
            if (!incomingCalls_.empty())
            {
                int now = secondsSinceEpoch();
                if (incomingCalls_.back() > now - secondsSinceLastCaller)
                {
                    incomingCalls_.pop_back();
                    srand(time(0));
                    CallLevel newCallLevel = static_cast<CallLevel>(rand() % 3);
                    waitingCalls_.push(std::move(Call(newCallLevel)));
                    std::cout << "Caller added" << std::endl;
                    secondsSinceLastCaller = now;
                }
            }

            std::chrono::milliseconds timespan(250);
            std::this_thread::sleep_for(timespan);
        }
        std::cout << "Call center is closed!" << std::endl;
    }
private:
    std::vector<int> incomingCalls_;
    std::queue<Call> waitingCalls_;
    std::vector<CallHandler> handlers_;

    bool allHandlersFree()
    {
        for (const CallHandler &handler : handlers_)
        {
            if (handler.busy())
            {
                return false;
            }
        }
        return true;
    }

    int secondsSinceEpoch()
    {
        auto now = std::chrono::system_clock::now().time_since_epoch();
        return std::chrono::duration_cast<std::chrono::seconds>(now).count();
    }
};
