#pragma once
enum class CallLevel { LOW, MEDIUM, HIGH };

class Call
{
public:
    Call() = delete;
    Call(CallLevel level);
    void process();
private:
    CallLevel level; // can only be solved by certain employee type
    int duration; // seconds to solve issue
};
