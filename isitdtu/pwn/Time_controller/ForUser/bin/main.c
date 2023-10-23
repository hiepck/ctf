#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int v2;
    time_t seed = 1697322000;
    // time_t current_time;
    // current_time = time(NULL);
    srand((unsigned)seed);
    v2 = rand();
    time_t v3 = seed;
    // printf("Current_time: %ld\n", current_time);
    printf("Seed: %d\n", seed);
    printf("Random number v2: %d\n", v2);
    printf("Time number v3: %d\n", v3);

    return 0;
}

// 0000000000000000000000000001011000110101000011000100110100000011
// 
// 1101111010101101101111101110111111011110101011011100000011011110 : res