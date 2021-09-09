#include<stdio.h>

// Hint : Your key is of size 13

int main()
{
    int a=10;
    char k='k';
    char e='e';
    char y='y';
    if(a){
    switch(a)
          {
            case 1:
                printf("%x",y);
                break;
            case 2:
                printf("%i",e);
                break;
            case 3:
                printf("%c",k);
                break;
            default:
                printf("%d",--a);
                break;
          }
        main(); //Don't even think of removing me
    }
    return 0;
  }
