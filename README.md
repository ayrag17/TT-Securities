# TT-Securities

**TT-Securities** is a Python-based command-line program designed to help users analyze stock price data. Through a series of menu options, the program allows users to input, analyze, and calculate various financial metrics based on a list of stock prices. It supports a range of tasks such as calculating the average price, determining the highest and lowest prices, testing thresholds, and creating a simple investment plan for maximizing profits.

The program is structured around an interactive command-line interface (CLI), where users can choose from different options and perform actions step-by-step.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [User Interface Loop](#user-interface-loop)
- [How It Works](#how-it-works)
- [License](#license)

## Overview

**TT-Securities** enables users to perform various analyses on stock price data. Users can input a list of prices for different days and use the following features:

- **Print the list of prices**.
- **Find the latest price**.
- **Calculate the average price**.
- **Find the maximum price and the day it occurred**.
- **Find the minimum single-day price change and the day it occurred**.
- **Test if any price exceeds a given threshold**.
- **Create an investment plan to maximize profits** by identifying the best days to buy and sell.

The program works interactively through a simple text-based menu system, where the user can select options to perform different tasks. It is designed to simulate basic financial analysis and investment planning using historical stock prices.

## Features

1. **Input a New List of Prices**: Allows the user to input a new list of stock prices for analysis.
2. **Print Current Prices**: Displays the stock prices entered so far, along with the corresponding days.
3. **Find the Latest Price**: Shows the most recent stock price in the list.
4. **Find the Average Price**: Calculates the average of all stock prices entered.
5. **Find the Max Price and Its Day**: Identifies the highest price and the day it occurred.
6. **Find the Min Single-Day Change and Its Day**: Calculates the smallest single-day price change and the day it occurred.
7. **Test a Threshold**: Allows users to input a price threshold and checks if any stock price exceeds it.
8. **Investment Plan**: Identifies the best day to buy and sell in order to maximize profit and displays the corresponding profit.

## User Interface Loop

The program uses a menu-driven interface, where users can choose from a list of available options. Once the user selects an option, the program will prompt for any necessary inputs, perform the corresponding task, and display the results.

### Main Menu Options:

1. **(0) Input a new list of prices**: Prompts the user to enter a list of stock prices (one price per day).
2. **(1) Print the current prices**: Displays the list of stock prices that have been entered, along with the corresponding days.
3. **(2) Find the latest price**: Shows the most recent stock price in the list.
4. **(3) Find the average price**: Calculates and displays the average of the stock prices.
5. **(4) Find the max price and its day**: Identifies the highest stock price and the day it occurred.
6. **(5) Find the min single-day change and its day**: Displays the smallest single-day price change and the day it occurred.
7. **(6) Test a threshold**: Lets the user input a threshold and checks if any stock price is above this threshold.
8. **(7) Your investment plan**: Finds the best day to buy and sell stock for maximum profit, and displays the corresponding profit.
9. **(8) Quit**: Exits the program.

### Sample Interaction:

1. The user starts the program and is presented with the main menu.
2. They input a list of stock prices for multiple days.
3. The user can then choose different options from the menu, such as finding the average price, checking the latest price, or calculating the maximum price.
4. They can also input a price threshold and check if any stock price exceeds this threshold.
5. The program continues to run in a loop, allowing the user to perform multiple actions until they choose to quit.

## How It Works

### Menu Options:

- **Input a New List of Prices**: When the user selects this option, they will be prompted to enter a list of stock prices (e.g., `[100.0, 105.5, 102.3, 98.8, 110.0]`). These prices will be used for all subsequent analyses.
  
- **Print Current Prices**: This option displays the list of prices entered so far, showing the prices alongside their respective days.

- **Find the Latest Price**: This option will return the most recent price in the list, i.e., the last price entered.

- **Calculate the Average Price**: The program will calculate the average price from all the prices entered and display the result.

- **Find the Max Price and Its Day**: This option will identify the highest price from the list and return the day it occurred.

- **Find the Min Single-Day Change and Its Day**: This option looks at the changes in price between consecutive days and returns the smallest price change, along with the day it occurred.

- **Test a Threshold**: The user can input a threshold value (e.g., 105.0), and the program will check if any price in the list is greater than the threshold.

- **Your Investment Plan**: This feature calculates the best days to buy and sell in order to maximize the profit from the given stock prices. It returns the days to buy and sell, along with the total profit.

### Example Workflow:

1. The user starts by inputting a list of stock prices: `[100.0, 105.5, 102.3, 98.8, 110.0]`.
2. The user can choose to calculate the **average price**, which will return the result `103.72`.
3. The user might also choose to find the **max price**, which could return the highest price `110.0` on day 4.
4. The user could check for the **best investment plan**, which may suggest buying on day 2 at `105.5` and selling on day 4 at `110.0` for a profit of `4.5`.

The loop continues until the user decides to exit the program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
