#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdint.h>

int main() {
    int fd;
    uint64_t random_number = 0;
    uint8_t random_bytes[8];
    int i;

    // Mở /dev/urandom
    fd = open("/dev/urandom", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    // Đọc 8 byte ngẫu nhiên
    ssize_t bytes_read = read(fd, random_bytes, 8);
    if (bytes_read != 8) {
        perror("read");
        exit(1);
    }

    // Biểu diễn số ngẫu nhiên dưới dạng số nguyên 64 bit
    for (i = 0; i < 8; ++i) {
        random_number = (random_number << 8) + random_bytes[i];
    }

    // Đóng tệp /dev/urandom
    close(fd);

    printf("Số ngẫu nhiên: %llu\n", random_number);

    return 0;
}
