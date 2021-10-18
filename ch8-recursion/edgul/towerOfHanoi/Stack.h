#pragma once
#include <assert.h>
#include <iostream>
#include <optional>

template <class T>
class Node
{
public:
    Node(const T& val) : value(val) {}
    T value;
    Node<T>* next;
};

template <class T>
class Stack
{
public:
    Stack() : head_(nullptr) {} 
    void push(const T &item){
        Node<T> *n = new Node<T>(item);
        if (!head_) {
            head_ = n;
            return;
        }
        n->next = head_;
        head_ = n;
    }

    std::optional<T> pop(){
        if (!head_) return {}; 
        Node<T> *temp = head_;
        head_ = head_->next;
        return temp->value;
    }

    std::optional<T> peek(){
        if (!head_) return {};
        return head_->value;
    }

    int length()
    {
        int count = 0;
        Node<T> *i = head_;
        while (i){
            count++;
            i = i->next;
        }
        return count;
    }

    void print()
    {
        std::cout << "[ ";
        Node<T> *i = head_;
        while (i) {
            std::cout << i->value << " ";
            i = i->next;
        }
        std::cout << "]" << std::endl;
    }
private:
    Node<T> *head_;
};
