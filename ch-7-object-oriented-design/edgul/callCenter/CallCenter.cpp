#include "CallCenter.h"
#include <algorithm>

void CallCenter::start()
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

    dispatchLoop();

    std::cout << "Call center is closed!" << std::endl;
}

bool CallCenter::allHandlersFree()
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

int CallCenter::secondsSinceEpoch()
{
    auto now = std::chrono::system_clock::now().time_since_epoch();
    return std::chrono::duration_cast<std::chrono::seconds>(now).count();
}

void CallCenter::dispatchCall()
{
   if (!waitingCalls_.empty())
   {
        auto isFreeResponder = [this](const CallHandler &handler)
        {
           return handler.callLevel() == CallLevel::LOW &&
                  !handler.busy();
        };
       
        auto isFreeManager = [this](const CallHandler &handler)
        {
           return handler.callLevel() == CallLevel::MEDIUM &&
                  !handler.busy();
        };

        auto isFreeDirector = [this](const CallHandler &handler)
        {
           return handler.callLevel() == CallLevel::HIGH &&
                  !handler.busy();
        };

        auto freeResponder = std::find_if(handlers_.begin(), handlers_.end(), isFreeResponder);
        if (freeResponder == handlers_.end())
        {
            std::cout << "No responders, call waits" << std::endl;
            return;
        }

        const Call &call = waitingCalls_.front();
        waitingCalls_.pop();
        if (!(*freeResponder).process(call))
        {

            auto freeManager = std::find_if(handlers_.begin(), 
                                              handlers_.end(), 
                                              isFreeManager);
            // no free managers or manager fails 
            if (freeManager == handlers_.end() ||
                !(*freeManager).process(call))
            {
                auto freeDirector = std::find_if(handlers_.begin(), 
                        handlers_.end(), 
                        isFreeDirector);

                // no free directors or director fails
                if (freeDirector == handlers_.end() ||
                    !(*freeDirector).process(call))
                {
                    std::cout << "No director, back to waiting" << std::endl;
                    waitingCalls_.push(call);
                }
            }
        }
    }
}

void CallCenter::dispatchLoop()
{
    int secondsSinceLastCaller = secondsSinceEpoch();

    while (!incomingCalls_.empty() &&
           !waitingCalls_.empty()  &&
           !allHandlersFree())
    {
        // add next caller if available
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

        dispatchCall();

        std::chrono::milliseconds timespan(250);
        std::this_thread::sleep_for(timespan);
    }
}
