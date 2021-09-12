#pragma once
#include <vector>
#include <iostream>
#include <assert.h>
#include <algorithm>


template<class T>
class CircularArray
{
public:
    CircularArray(int size) {
        assert(size > 0);
        vec_ = std::vector<T>(size);
        head_ = 0;
    }
    
    T& head() { return vec_[head_]; }
    int headIndex() { return head_; } 
    void print(){
        std::for_each(vec_.begin(), vec_.end(), 
                [](T& i) { std::cout << i << " "; });
        std::cout << std::endl;
    }
   
    // access and overwrite with []
    T& operator[](int index){
        if (index >= vec_.size()){
            std::cout << "Error: indexing out of array\n";
        }
        return vec_[(index+head_)%vec_.size()];
    }

    void rotate(int offset){
        head_ = (head_ + offset) % vec_.size();
        assert(head_ <= vec_.size());
        assert(head_ > 0);
    }

    struct Iterator 
    {
        using iterator_category = std::forward_iterator_tag;
        using difference_type   = std::ptrdiff_t;
        using value_type        = T;
        using pointer           = T*;
        using reference         = T&;

        Iterator(pointer startPtr, pointer endPtr, pointer currentPtr, bool start) :
            m_startPtr(startPtr), 
            m_endPtr(endPtr),
            m_ptr(currentPtr),
            firstLap(start) 
        { 
        }
        
        reference operator*() const { return *m_ptr; }
        pointer operator->() { return m_ptr; }
        Iterator& operator++() { 
            m_ptr++; 
            if (m_ptr >= m_endPtr){
                m_ptr = m_startPtr;
                firstLap = false;
            }
            return *this; 
        }  

        // doesn't appear necessary for basic iteration
        //Iterator operator++(int) { Iterator tmp = *this; ++(*this); return tmp; }
        friend bool operator== (const Iterator& a, const Iterator& b) { 
            return a.m_ptr == b.m_ptr && a.firstLap == b.firstLap;
        };
        friend bool operator!= (const Iterator& a, const Iterator& b) { 
            return a.m_ptr != b.m_ptr || a.firstLap != b.firstLap;
        };  

    private:
        pointer m_ptr;
        pointer m_startPtr;
        pointer m_endPtr;
        bool firstLap; // needed to distinguish between head_ and (head_ as end)
    };

    Iterator begin() { return Iterator(&vec_[0], 
                                       &vec_[vec_.size()],
                                       &vec_[head_],
                                       true); }
    Iterator end() { return Iterator(&vec_[0], 
                                       &vec_[vec_.size()], 
                                       &vec_[head_],
                                       false);}

private:
    std::vector<T> vec_;
    int head_;
};
