#include <stdio.h>

int arr[3];
int result[3];
int tmp[3];
int Min(int a, int b)
{
    return a < b ? a : b;
}
void myresult(int N)
{
    int i;
    result[0] = result[1] = result[2] = 0;
    for (i = 1; i <= N; i++)
    {
        scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);
        
            tmp[0] = result[0];
            tmp[1] = result[1];
            tmp[2] = result[2];
            
            result[0] = Min(tmp[1], tmp[2]) + arr[0];
            result[1] = Min(tmp[0], tmp[2]) + arr[1];
            result[2] = Min(tmp[0], tmp[1]) + arr[2];
    }
    int min = Min(Min(result[0], result[1]), result[2]);
    printf("%d", min);
}
int main()
{
    int i;
    int N;
    scanf("%d", &N);
    myresult(N);
}
