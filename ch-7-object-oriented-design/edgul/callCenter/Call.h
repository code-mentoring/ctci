#pragma once

#include <thread>
#include <chrono>

enum class CallLevel { LOW, MEDIUM, HIGH };

class Call
{
public:
    Call() = delete;
    Call(CallLevel level) : level_(level)
    {
        srand(time(0));
        duration_ = rand() % 20 + 10; // 10 -> 30
    }

    CallLevel level() const { return level_; }

    void process() const
    {
        std::chrono::milliseconds timespan(duration_ * 1000);
        std::this_thread::sleep_for(timespan);
        std::cout << "Processed call" << std::endl;
    }

private:
    CallLevel level_; // can only be solved by certain employee type
    int duration_; // seconds to solve issue
};
