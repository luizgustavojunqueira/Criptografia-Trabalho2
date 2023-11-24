#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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

int inversoMultiplicativo(int a, int n)
{
    MDC mdc = EuclidesEstendido(a, n);

    if (mdc.a == 1)
    {
        if (mdc.t >= 0)
        {
            return mdc.t;
        }
        else
        {
            return n + mdc.t;
        }
    }
    else
    {
        return 0; // Falha
    }
}

int checarCongruenciaModN(int a, int b, int n)
{
    if (a % n == b)
    {
        return 1;
    }
    return 0;
}

int main()
{

    srand(time(NULL));

    int n = -1, s = 0, v = 0, opcMenu = -1, r = -1, respondido = 0;

    do
    {
        printf("\n");
        printf("Identificar - 1\n");
        printf("Iniciar - 2\n");
        printf("Preparar - 3\n");
        printf("Responder - 4\n");
        printf("Terminar - 0\n");
        scanf("%d", &opcMenu);

        switch (opcMenu)
        {
        case 1:
            printf("Insira os valores de n, s e v:\n");
            printf("n: ");
            scanf("%d", &n);
            printf("s: ");
            scanf("%d", &s);
            printf("v: ");
            scanf("%d", &v);

            if (checarCongruenciaModN(s * s * v, 1, n))
            {
                printf("CORRETO\n");
            }
            else
            {
                printf("ERRO: s^2*v≡1 (mod n) não é verdadeiro.\n");
            }
            break;
        case 2:
            if (n != 0)
            {

                MDC mdc;
                do
                {
                    r = rand() % n;
                    mdc = EuclidesEstendido(r, n);
                } while (mdc.a != 1);

                int x = r * r;

                printf("x: %d\n", x);
            }
            else
            {
                printf("ERRO: Não foi identificado ainda.\n");
            }
            break;
        case 3:
            if (n > 0)
            {
                printf("Insira r:");
                scanf("%d", &r);

                int x = r * r;

                printf("x: %d\n", x);
            }
            else if (n == -1)
            {
                printf("ERRO: Não foi identificado ainda.\n");
            }
            break;
        case 4:

            if (respondido == 1)
            {
                printf("ERRO: Uma resposta já foi executada.\n");
                break;
            }
            if (n == -1)
            {
                printf("ERRO: Não foi identificado ainda.\n");
                break;
            }

            printf("Insira o bit: ");
            int b;
            scanf("%d", &b);

            if (b != 0 && b != 1)
            {
                printf("ERRO: O bit fornecido não é válido.\n");
                break;
            }

            int xb = 0;
            if (b == 0)
            {
                xb = r;
            }
            else if (b == 1)
            {
                xb = (r * s) % n;
            }

            printf("xb: %d\n", xb);

            r = -1;
            respondido = 1;
            break;
        case 0:
            printf("Terminando o programa.\n");
            break;
        default:
            printf("Opção selecionada não existe.\n");
            break;
        }
    } while (opcMenu != 0);

    // if (checarCongruenciaModN(s ^ 2 * v, 1, n))
    // {
    //     printf("CORRETO");

    //     MDC mdc;
    //     int r;
    //     do
    //     {
    //         r = rand();
    //         mdc = EuclidesEstendido(r, n);
    //     } while (mdc.a != 1);

    //     int x = r * r;

    //     printf("%d", x);
    // }
    // else
    // {
    //     printf("ERRADO");
    // }

    // int inverso = inversoMultiplicativo(a, n);

    // printf("%d\n", inverso);

    return 0;
}