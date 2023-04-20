#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int rec(int x){  
    if ((x == 0) || (x == 1)) return 0; 
    else return rec(x - 1) * x + rec(x - 2); 
} 

main()
{
    printf("%d", rec(5));
    
}


