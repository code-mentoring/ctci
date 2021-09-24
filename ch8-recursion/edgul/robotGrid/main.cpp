#include <iostream>
#include <vector>
#include <algorithm>

// coordinates on our grid for convenience
struct Pt{
   int x;
   int y;

   // handy functions to get neighbour points
   Pt right() const { return {x+1, y}; }
   Pt down() const  { return {x, y+1}; }
};
inline bool operator==(const Pt &l, const Pt &r) { return l.x == r.x && l.y == r.y; }
inline bool operator!=(const Pt &l, const Pt &r) { return !(l==r); }

// grid that has blocked coordinates
class Grid{
    int w_;
    int h_;
    std::vector<Pt> blocks_;
public:
    Grid(int w, int h) : w_(w), h_(h) {}
    void addBlock(const Pt &pt) { 
        if (pt.x < w_ && pt.y < h_ && pt.x >= 0 && pt.y >= 0)
            blocks_.push_back(pt); 
    }
    bool isBlocked(const Pt &pt) const {
        if (pt.x >= w_) return true; // off grid is considered a block
        if (pt.y >= h_) return true; // off grid is considered a block
        auto eqPt = [&](const Pt &other) {
            return pt.x == other.x && pt.y == other.y;
        };
        return std::find_if(blocks_.cbegin(), blocks_.cend(), eqPt) != blocks_.end();
    }
    Pt end() const { return {w_-1, h_-1}; }
};

enum Dir { DOWN, RIGHT };

// brute force a path from robot pt to the grid's bottom-right (if possible) 
std::vector<Dir> explore(const Pt &robot, const Grid &grid, std::vector<Dir> dirs)
{
    if (robot == grid.end())                    
    {
        return dirs;
    }
    if (!grid.isBlocked(robot.down())) 
    {
       dirs.push_back(Dir::DOWN);
       return explore(robot.down(), grid, dirs);
    }
    if (!grid.isBlocked(robot.right())) 
    {
       dirs.push_back(Dir::RIGHT);
       return explore(robot.right(), grid, dirs);
    }
  
    // return the empty vector if neither direction is possible from current location
    return std::vector<Dir>();
}

int main(int argc, char **argv)
{
    Pt robot{0,0};
    Grid grid(5,5);
    grid.addBlock({2,2});
    grid.addBlock({0,1});
    grid.addBlock({1,1});
  
    // go exploring!
    std::vector<Dir> result = explore(robot, grid, std::vector<Dir>());

    // check if no path exists
    if (result.empty())
    {
        std::cout << "No path exists!" << std::endl;
        return 0;
    }

    // just printing result path
    std::for_each(result.begin(), result.end(), [](auto &i){
            std::cout << i;
    });
    std::cout << std::endl;
    return 0;
}
