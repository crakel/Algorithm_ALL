#include <stdio.h>
int main(void)
{
    char a[101];
    
    while(gets(a)){
    	if(a[0]=='\0')
    		break;
        puts(a);
    }

    return 0;
    
}