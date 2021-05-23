#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define NO_BOUND 0
#define LEFT_BOUND 1
#define RIGHT_BOUND 2
#define BOTH_BOUNDS 3

int min(int a, int b) {
    return a < b ? a : b;
}

int max(int a, int b) {
    return a > b ? a : b;
}

struct Node {
    int value;
    struct Node *left;
    struct Node *right;
};

struct Node *make_node(int value) {
    struct Node *node;
    if ((node = malloc(sizeof *node)) == NULL) {
        fprintf(stderr, "failed to allocate space for a node, exiting");
        exit(1);
    }
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void free_node(struct Node *node) {
    if (node != NULL) {
        free_node(node->left);
        free_node(node->right);
        free(node);
    }
}

void display_edges(struct Node *tree) {
    if (tree->left != NULL) {
        printf("%d -> %d\n", tree->value, tree->left->value);
        display_edges(tree->left);
    }
    if (tree->right != NULL) {
        printf("%d -> %d\n", tree->value, tree->right->value);
        display_edges(tree->right);
    }
}

typedef struct {
    int type;
    int lb;
    int ub;
} Range;

bool within_range(int n, Range *range) {
    switch(range->type) {
        case LEFT_BOUND: return n > range->lb;
        case RIGHT_BOUND: return n < range->ub;
        case BOTH_BOUNDS: return n > range->lb && n < range->ub;
    }
    return true;
}

void init_range_with_ub(Range *range, int n, Range *original) {
    // Oof. I'm sure there's a better way to do all of this.
    if (original->type == NO_BOUND) {
        range->type = RIGHT_BOUND;
        range->ub = n;
    } else if (original->type == RIGHT_BOUND) {
        range->type = RIGHT_BOUND;
        range->ub = min(n, original->ub);
    } else if (original->type == LEFT_BOUND) {
        range->type = BOTH_BOUNDS;
        range->lb = original->lb;
        range->ub = n;
    } else {
        range->type = BOTH_BOUNDS;
        range->lb = original->lb;
        range->ub = min(n, original->ub);
    }
}

void init_range_with_lb(Range *range, int n, Range *original) {
    if (original->type == NO_BOUND) {
        range->type = LEFT_BOUND;
        range->lb = n;
    } else if (original->type == RIGHT_BOUND) {
        range->type = BOTH_BOUNDS;
        range->lb = n;
        range->ub = original->ub;
    } else if (original->type == LEFT_BOUND) {
        range->type = LEFT_BOUND;
        range->lb = max(n, original->lb);
    } else {
        range->type = BOTH_BOUNDS;
        range->lb = max(n, original->lb);
        range->ub = original->ub;
    }
}

bool is_bst_with_range(struct Node *tree, Range *range) {
    if (!within_range(tree->value, range)) {
        return false;
    }
    if (tree->left != NULL) {
        // The value of the current node acts as an upper bound
        // for the left branch of the tree...
        Range left_range;
        init_range_with_ub(&left_range, tree->value, range);
        if (!is_bst_with_range(tree->left, &left_range)) {
            return false;
        }
    }
    if (tree->right != NULL) {
        // ...and as a lower bound for the right branch.
        Range right_range;
        init_range_with_lb(&right_range, tree->value, range);
        if (!is_bst_with_range(tree->right, &right_range)) {
            return false;
        }
    }
    return true;
}
    
bool is_binary_search_tree(struct Node *tree) {
    Range initial_range;
    initial_range.type = NO_BOUND;
    return is_bst_with_range(tree, &initial_range);
}

int main() {
    // Should really make it easier to create test cases...
    // BUT ANYWAY.
    struct Node *root = make_node(3);
    struct Node *right = make_node(5);
    struct Node *right_left = make_node(2);
    root->right = right;
    right->left = right_left;
    display_edges(root);

    printf(is_binary_search_tree(root) ? "bst" : "NOT bst");
    printf("\n");
    free_node(root);
}
