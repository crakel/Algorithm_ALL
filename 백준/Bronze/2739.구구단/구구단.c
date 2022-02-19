#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);
    
    for(int i=0; i<9; i++)
    {
        printf("%d * %d = %d\n", N, i+1, N*(i+1));
    }
    return 0;
}