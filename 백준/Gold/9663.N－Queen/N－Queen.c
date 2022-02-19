#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int n;
int col[15];
int queen_count = 0;

bool isPromise(int i) {
    int j = 0;
    bool flag = true;
    while (j < i && flag) {
        if (col[i] == col[j] || abs(col[i] - col[j]) == (i - j)) {
            flag = false;
        }
        j += 1;
    }
    return flag;
}

void dfs(int i) {
    if (i == n) {
        queen_count += 1;
    }

    else {
        int j;
        for(j = 0; j < n; j++) {
            col[i] = j;
            if (isPromise(i)) {
                dfs(i + 1);
            }
        }
    }
}

int main() {
    scanf("%d", &n);
    dfs(0);
    printf("%d", queen_count);
    return 0;
}