#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define BUF_SIZE 1 << 26

int main() {
    int fd = STDIN_FILENO;
    char *ptr = mmap(NULL, BUF_SIZE, PROT_READ, MAP_PRIVATE, fd, 0);
    
    char *end = ptr;
    while (*end) end++;

    int N = 0;
    while (*ptr >= '0' && *ptr <= '9') {
        N = N * 10 + (*ptr - '0');
        ptr++;
    }
    ptr++;

    int count = 0;
    long long sum = 0;
    int num = 0;

    while (ptr < end) {
        if (*ptr >= '0' && *ptr <= '9') {
            num = num * 10 + (*ptr - '0');
        } else {
            sum += num;
            count++;
            num = 0;
        }
        ptr++;
    }

    char out_buf[32];
    int len = sprintf(out_buf, "%d\n%lld\n", count, sum);
    write(STDOUT_FILENO, out_buf, len);

    return 0;
}
