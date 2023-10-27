bool isPalindrome(int x)
{
    if (x < 0) {
        return false;
    }

    char x_str[12];
    int n = snprintf(x_str, sizeof(x_str), "%d", x);

    for (int i = 0; i < n / 2; i++) {
        if (x_str[i] != x_str[n - i - 1]) {
            return false;
        }
    }

    return true;
}