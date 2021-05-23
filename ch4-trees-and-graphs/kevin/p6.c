#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define LIST_CAPACITY 5

typedef struct {
    char from;
    char to;
} Dependency;

typedef struct {
    size_t n;
    size_t capacity;
    char *ps;
} ProjectList;

ProjectList *make_plist() {
    char *ps = malloc(LIST_CAPACITY * (sizeof *ps));
    if (ps == NULL) {
        return NULL;
    }
    ProjectList *list = malloc(sizeof *list);
    if (list == NULL) {
        free(ps);
        return NULL;
    }
    list->n = 0;
    list->capacity = LIST_CAPACITY;
    list->ps = ps;
    return list;
}

void free_plist(ProjectList *list) {
    free(list->ps);
    free(list);
}

bool plist_push(ProjectList *list, char new_dep) {
    if (list->capacity == list->n) {
        list->capacity *= 2;
        list->ps = realloc(list->ps, list->capacity * sizeof *(list->ps));
        if (list->ps  == NULL) {
            return false;
        }
    }
    list->ps[list->n++] = new_dep;
    return true;
}

char plist_pop(ProjectList *list) {
    return list->ps[--(list->n)];
}

char plist_get(ProjectList *list, size_t index) {
    return list->ps[index];
}

bool plist_contains(ProjectList *list, char project) {
    for (size_t index = 0; index < list->n; ++index) {
        if (plist_get(list, index) == project) {
            return true;
        }
    }
    return false;
}

void fill_dependencies(char pid, ProjectList *dependencies, Dependency *direct_deps, size_t num_direct_deps) {
    ProjectList *stack = make_plist();
    plist_push(stack, pid);
    while (stack->n > 0) {
        char next = plist_pop(stack);
        for (size_t i = 0; i < num_direct_deps; ++i) {
            char from = direct_deps[i].from;
            char to = direct_deps[i].to;
            // The list of dependencies keeps track of which
            // 'nodes' (i.e. projects) we've visited before.
            if (to == next && !plist_contains(dependencies, from)) {
                plist_push(dependencies, from);
                plist_push(stack, from);
            }
        }
    }
}

int main() {
    ProjectList *projects = make_plist();
    // Look at me, not even checking for a failed allocation.
    // Such a rebel.
    plist_push(projects, 'a');
    plist_push(projects, 'b');
    plist_push(projects, 'c');
    plist_push(projects, 'd');
    plist_push(projects, 'e');
    plist_push(projects, 'f');
    Dependency deps[5] = {
        {'a', 'd'},
        {'f', 'b'},
        {'b', 'd'},
        {'f', 'a'},
        {'d', 'c'}
    };
    // Make a list of dependencies for each project.
    size_t n = projects->n;
    ProjectList **dependencies_per_project = malloc(n * sizeof (*dependencies_per_project));
    for (size_t i = 0; i < n; ++i) {
        char pid = plist_get(projects, i);
        dependencies_per_project[i] = make_plist();
        fill_dependencies(pid, dependencies_per_project[i], deps, sizeof(deps)/sizeof(deps[0]));
        if (plist_contains(dependencies_per_project[i], pid)) {
            printf("Error: project '%c' depends on itself!", pid);
            exit(1);
        }
    }

    ProjectList *visited = make_plist();
    while (visited->n <  projects->n) {
        for (size_t i = 0; i < n; ++i) {
            if (!plist_contains(visited, plist_get(projects, i))) {
                bool ready = true;
                for (size_t j = 0; j < dependencies_per_project[i]->n; ++j) {
                    if (!plist_contains(visited, plist_get(dependencies_per_project[i], j))) {
                        ready = false;
                        break;
                    }
                }
                if (ready) {
                    plist_push(visited, plist_get(projects, i));
                }
            }
        }
    }
    for (size_t i = 0; i < visited->n; ++i) {
        printf("%c ", plist_get(visited, i));
    }
    printf("\n");
}
