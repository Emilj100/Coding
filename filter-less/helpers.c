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


                copy[i][j] = image[i][j];
                int middle_pixel_blue = copy[i][j].rgbtBlue;
                int middle_pixel_red = copy[i][j].rgbtRed;
                int middle_pixel_green = copy[i][j].rgbtGreen;


                int right_pixel_blue = copy[i][j + 1].rgbtBlue;
                int right_pixel_red = copy[i][j + 1].rgbtRed;
                int right_pixel_green = copy[i][j + 1].rgbtGreen;


                int left_pixel_blue = copy[i][j - 1].rgbtBlue;
                int left_pixel_red = copy[i][j - 1].rgbtRed;
                int left_pixel_green = copy[i][j - 1].rgbtGreen;

                int left_up_cornor_blue = copy[i - 1][j - 1].rgbtBlue;
                int left_up_cornor_red = copy[i - 1][j - 1].rgbtRed;
                int left_up_cornor_green = copy[i - 1][j - 1].rgbtGreen;

                int up_pixel_blue = copy[i - 1][j].rgbtBlue;
                int up_pixel_red = copy[i - 1][j].rgbtRed;
                int up_pixel_green = copy[i - 1][j].rgbtGreen;

                int right_up_cornor_blue = copy[i - 1][j + 1].rgbtBlue;
                int right_up_cornor_red = copy[i - 1][j + 1].rgbtRed;
                int right_up_cornor_green = copy[i - 1][j + 1].rgbtGreen;

                int left_down_cornor_blue = copy[i + 1][j - 1].rgbtBlue;
                int left_down_cornor_red = copy[i + 1][j - 1].rgbtRed;
                int left_down_cornor_green = copy[i + 1][j - 1].rgbtGreen;

                int down_pixel_blue = copy[i + 1][j].rgbtBlue;
                int down_pixel_red = copy[i + 1][j].rgbtRed;
                int down_pixel_green = copy[i + 1][j].rgbtGreen;

                int right_down_cornor_blue = copy[i + 1][j + 1].rgbtBlue;
                int right_down_cornor_red = copy[i + 1][j + 1].rgbtRed;
                int right_down_cornor_green = copy[i + 1][j + 1].rgbtGreen;

                int average_blue = (middle_pixel_blue + right_pixel_blue + left_pixel_blue + left_up_cornor_blue + up_pixel_blue + right_up_cornor_blue + left_down_cornor_blue + down_pixel_blue + right_down_cornor_blue) / 9;
                int average_red = (middle_pixel_red + right_pixel_red + left_pixel_red + left_up_cornor_red + up_pixel_red + right_up_cornor_red + left_down_cornor_red + down_pixel_red + right_down_cornor_red) / 9;
                int average_green = (middle_pixel_green + right_pixel_green + left_pixel_green + left_up_cornor_green + up_pixel_green + right_up_cornor_green + left_down_cornor_green + down_pixel_green + right_down_cornor_green) / 9;


                image[i][j].rgbtBlue = average_blue;
                image[i][j].rgbtRed = average_red;
                image[i][j].rgbtGreen = average_green;

        }
    }
    
}
