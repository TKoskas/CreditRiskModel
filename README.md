# Monte Carlo Default Risk Simulation

This Python script simulates credit risk using the Merton model and Monte Carlo simulations to estimate the probability of default (PD) and the loss given default (LGD). It calculates the average loss for a given portfolio based on asset values, volatility, recovery rates, and debt levels.

## Overview

The script performs the following tasks:

1. **Calculate the Probability of Default (PD)**: Uses the Merton model to compute the probability of default based on asset values, debt levels, volatility, and time to maturity.
2. **Calculate the Loss Given Default (LGD)**: Computes the loss in case of default based on the recovery rate.
3. **Monte Carlo Simulation**: Simulates a large number of asset price paths to estimate the distribution of potential losses and the average loss for a portfolio.
4. **Visualization**: Generates a histogram showing the distribution of losses, with a vertical line indicating the average loss.

## Requirements

To run this project, you need Python 3.x and the following libraries:

- `numpy`
- `scipy`
- `matplotlib`

You can install the required libraries using `pip`:

```bash
pip install numpy scipy matplotlib
```

## Usage
Download or clone the repository.
Run the script in a Python environment.
```bash
python monte_carlo_default_risk.py
```
## Example Output:
Probability of Default (PD): 0.1028 (10.28% chance of default)

Loss Given Default (LGD): 0.6000 (60% loss on debt in case of default)

Average Loss on Portfolio (simulated via Monte Carlo): 48.10 (the average loss calculated from the Monte Carlo simulations)

A histogram will be displayed showing the distribution of potential losses. The red dashed line indicates the average loss for the portfolio, and the legend will display this value.

## License
This project is licensed under the MIT License 
