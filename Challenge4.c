#include <stdio.h>

#include <stdlib.h>

int main() {

        char *user = getenv("TERM");

        printf("your TERM=%s\n", user);

        return 0;

}
