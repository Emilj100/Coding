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

