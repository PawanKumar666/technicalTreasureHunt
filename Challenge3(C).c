#include<stdio.h>
void func1();
void _func1();
void func3();
void func4();
void func5();
int height = 5;
int width = 9;
int abs(int d)
{
    return d < 0 ? -1 * d : d;
}
//Pi is an important numeric in math
void main(){

func1();
func3();
_func1();
func4();
func5();

}
void func4()
{
    int i, j, counter = 0;
    for (i = 0; i < height; i++) {
        for (j = 0; j <= width; j++) {
            if (j == counter
                || j == width - counter - 1)
                printf("*");
            else
                printf(" ");
        }
        counter++;
        printf("\n");
    }
}
void _func1()
{
    int i, j;
    for (i = 0; i < height; i++) {
        printf("*");
        for (j = 0; j < height; j++) {
            if ((i == 0 || i == height - 1)
                || (i == height / 2
                    && j <= height / 2))
                printf("*");
            else
                continue;
        }
        printf("\n");
    }
}
void func3()
{
    int i, j, counter = 0;
    for (i = 0; i < height; i++) {
        printf("*");
        for (j = 0; j <= height; j++) {
            if (j == height)
                printf("*");
            else if (j == counter)
                printf("*");
            else
                printf(" ");
        }
        counter++;
        printf("\n");
    }
}
void func5()
{
    int i, j, half = (height / 2);
    for (i = 0; i < height; i++) {
        printf("*");
        for (j = 0; j < width; j++) {
            if ((i == 0 || i == half)
                && j < (width - 2))
                printf("*");
            else if (j == (width - 2)
                     && !(i == 0 || i == half))
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}
void func1()
{
    int i, j;
    for (i = 0; i < height; i++) {
        printf("*");
        for (j = 0; j < height; j++) {
            if ((i == 0 || i == height - 1)
                || (i == height / 2
                    && j <= height / 2))
                printf("*");
            else
                continue;
        }
        printf("\n");
    }
}
