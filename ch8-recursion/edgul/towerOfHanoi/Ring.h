#pragma once
#include <iostream>

struct Ring {
    Ring(int s) : size(s) {}
    int size;
};

inline bool operator==(const Ring& lhs, const Ring& rhs) {
    return lhs.size == rhs.size;
}
inline bool operator!=(const Ring& lhs, const Ring& rhs) {
    return lhs.size != rhs.size;
}
inline bool operator<(const Ring& lhs, const Ring& rhs) {
    return lhs.size < rhs.size;
}
inline bool operator>(const Ring& lhs, const Ring& rhs) {
    return lhs.size > rhs.size;
}
inline std::ostream &operator<<(std::ostream &output, const Ring& r) {
    output << "Ring(" << r.size << ")";
    return output;
}
