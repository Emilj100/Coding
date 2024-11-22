#include "helpers.h"
#include <math.h>

int threshold(int value);


void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gray = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;

            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
}

void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redSum = 0, greenSum = 0, blueSum = 0;
            int count = 0;

            // The blurring kernel
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int newI = i + k;
                    int newJ = j + l;

                    if (newI >= 0 && newI < height && newJ >= 0 && newJ < width)
                    {
                        redSum += image[newI][newJ].rgbtRed;
                        greenSum += image[newI][newJ].rgbtGreen;
                        blueSum += image[newI][newJ].rgbtBlue;
                        count++;
                    }
                }
            }

            temp[i][j].rgbtRed = round((float)redSum / count);
            temp[i][j].rgbtGreen = round((float)greenSum / count);
            temp[i][j].rgbtBlue = round((float)blueSum / count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}

void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Opret et midlertidigt billede for at gemme de nye pixelværdier
    RGBTRIPLE temp[height][width];

    // Sobel-masker til beregning af gradienter i x- og y-retninger
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Iterer gennem hver pixel i billedet
    for (int i = 0; i < height; i++) // Loop over rækker
    {
        for (int j = 0; j < width; j++) // Loop over kolonner
        {
            // Initialiser gradientværdier for hver farvekanal
            int GxRed = 0, GxGreen = 0, GxBlue = 0;
            int GyRed = 0, GyGreen = 0, GyBlue = 0;

            // Iterer gennem nabolaget (3x3 område omkring pixel)
            for (int k = -1; k <= 1; k++) // Række-offset
            {
                for (int l = -1; l <= 1; l++) // Kolonne-offset
                {
                    // Beregn koordinater for nabopixel
                    int newI = i + k;
                    int newJ = j + l;

                    // Tjek, om nabopixel er inden for billedets grænser
                    if (newI >= 0 && newI < height && newJ >= 0 && newJ < width)
                    {
                        // Beregn vægtet bidrag fra nabopixel til Gx og Gy for hver farvekanal
                        GxRed += Gx[k + 1][l + 1] * image[newI][newJ].rgbtRed;
                        GxGreen += Gx[k + 1][l + 1] * image[newI][newJ].rgbtGreen;
                        GxBlue += Gx[k + 1][l + 1] * image[newI][newJ].rgbtBlue;

                        GyRed += Gy[k + 1][l + 1] * image[newI][newJ].rgbtRed;
                        GyGreen += Gy[k + 1][l + 1] * image[newI][newJ].rgbtGreen;
                        GyBlue += Gy[k + 1][l + 1] * image[newI][newJ].rgbtBlue;
                    }
                }
            }

            // Beregn den samlede gradient ved hjælp af Pythagoras' sætning
            temp[i][j].rgbtRed = threshold(round(sqrt(GxRed * GxRed + GyRed * GyRed)));
            temp[i][j].rgbtGreen = threshold(round(sqrt(GxGreen * GxGreen + GyGreen * GyGreen)));
            temp[i][j].rgbtBlue = threshold(round(sqrt(GxBlue * GxBlue + GyBlue * GyBlue)));
        }
    }

    // Kopier de beregnede værdier fra temp tilbage til det originale billede
    for (int i = 0; i < height; i++) // Loop over rækker
    {
        for (int j = 0; j < width; j++) // Loop over kolonner
        {
            image[i][j] = temp[i][j];
        }
    }
}

// Funktion til at sikre, at værdier ligger inden for intervallet [0, 255]
int threshold(int value)
{
    return value > 255 ? 255 : (value < 0 ? 0 : value);
}
