import os

def main():
    generate_paths_c()

def generate_paths_c():
    base_path = os.path.abspath(os.getcwd())

    with open('bokuro/path.c', 'w') as f:
        c_code = [
            '#define BOKURO_SRC_PATH "{}"'.format(base_path),
            """
#include <stdlib.h>
#include <string.h>
#include "path.h"

#include <stdio.h>

char *bokuro_path_ptr(char *rel_path) {
    static char *base_path = BOKURO_SRC_PATH;
    char *s;
    size_t l;

    l = strlen(BOKURO_SRC_PATH) + strlen(rel_path) + 2;

    s = (char *) malloc(sizeof(char) * l);

    strcpy(s, base_path);
    strcat(s, "/");
    strcat(s, rel_path);
    strcat(s, "\\0");

    return s;
}

const char *bokuro_path(char *rel_path) {
    int a_i = 0;
    int a_n = strlen(BOKURO_SRC_PATH);
    int b_i = 0;
    int b_n = strlen(rel_path);
    int i = 0;
    int l = a_n + b_n + 1;

    static char *base_path = BOKURO_SRC_PATH;
    char s[l+1];

    for (i = 0; i <= l; i++) {
        if (i < a_n) {
            s[i] = (char) base_path[a_i++];

            printf("a[%d] (%c) -> s[%d] (%s)\\n", a_i - 1, base_path[a_i - 1], i, s);

            continue;
        } else if (i == a_n) {
            s[i] = '/';

            continue;
        }

        s[i] = (char) rel_path[b_i++];

        printf("a[%d] (%c) -> s[%d] (%s)\\n", b_i - 1, base_path[b_i - 1], i, s);
    }

    s[l] = '\\0';

    printf("Final String: %s\\n", s);
    printf("Actual Total Length: %d\\n", (int) strlen(s));
    printf("Expected Total Length: %d\\n", l);

    return s;
}
"""
        ]

        f.writelines(c_code);

if __name__ == '__main__':
    main()
