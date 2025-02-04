#include <stdio.h>
#include <unistd.h>

#define BUF_SIZE 1 << 20  // 1MB 버퍼

char buf[BUF_SIZE];
int N, count = 0;
long long sum = 0;

int main() {
    // 표준 입력을 fread로 한 번에 읽기
    int bytesRead = read(STDIN_FILENO, buf, BUF_SIZE);
    char *ptr = buf;

    // 첫 번째 줄: N 읽기
    while (*ptr >= '0' && *ptr <= '9') {
        N = N * 10 + (*ptr - '0');
        ptr++;
    }
    ptr++;  // 개행 문자 넘기기

    // 두 번째 줄부터 자연수 읽기
    int num = 0;
    while (ptr < buf + bytesRead) {
        if (*ptr >= '0' && *ptr <= '9') {
            num = num * 10 + (*ptr - '0');
        } else {  // 개행 문자 '\n'이면 숫자 확정
            sum += num;
            count++;
            num = 0;
        }
        ptr++;
    }

    // M과 합 출력
    printf("%d\n%lld\n", count, sum);

    return 0;
}
