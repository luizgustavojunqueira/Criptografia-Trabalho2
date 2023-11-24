#include <stdio.h>

struct mdcStruct
{
    int a, s, t;
};

typedef struct mdcStruct MDC;

MDC EuclidesEstendido(int a, int b)
{
    MDC mdc;
    int s = 1, t = 0, x = 0, y = 1;

    while (b != 0)
    {
        int c = a % b;
        int q = a / b;
        int i = s - q * x;
        int j = t - q * y;

        a = b;
        b = c;
        s = x;
        t = y;
        x = i;
        y = j;
    }

    mdc.a = a;
    mdc.s = s;
    mdc.t = t;

    return mdc;
}

int inversoMultiplicativo(int a, int n){
    MDC mdc = EuclidesEstendido(a, n);

    if(mdc.a == 1){
        if(mdc.t >= 0){
            return mdc.t;
        }else{
            return n + mdc.t;
        }
    }else{
        return 0; // Falha
    }
}

int main()
{

    int a = 7, n = 5;

    int inverso = inversoMultiplicativo(a, n);

    printf("%d\n", inverso);

    return 0;
}