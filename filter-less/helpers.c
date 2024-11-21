#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Update pixel values
            int average = round((red + green + blue) / 3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;

        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
     // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Compute sepia values
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Update pixel with sepia values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    int center = width / 2;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < center; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    // For hver række
    for (int i = 0; i < height; i++)
    {
        // For hver pixel i rækken
        for (int j = 0; j < width; j++)
        {
            if (i == 0 || j == 0)
            {

            }
            else
            {
                copy[i][j] = image[i][j];
                RGBTRIPLE middle_pixel = copy[i][j];
                RGBTRIPLE right_pixel = copy[i][j + 1];
                RGBTRIPLE left_pixel = copy[i][j - 1];
                RGBTRIPLE left_up_cornor = copy[i - 1][j - 1];
                RGBTRIPLE up_pixel = copy[i - 1][j];
                RGBTRIPLE right_up_cornor = copy[i - 1][j + 1];
                RGBTRIPLE left_down_cornor = copy[i + 1][j - 1];
                RGBTRIPLE down_pixel = copy[i + 1][j];
                RGBTRIPLE right_down_cornor = copy[i + 1][j + 1];

                RGBTRIPLE average = (middle_pixel + right_pixel + left_pixel + left_up_cornor + up_pixel + right_up_cornor + left_down_cornor + down_pixel + right_down_cornor) / 9;
            }
        }
    }
    return;
}
