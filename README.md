# Elliott Wave Dataset for CNN

## Introduction

This repository is dedicated to building an open-source contribution for recognizing Elliott Wave patterns in financial markets using Convolutional Neural Networks (CNNs). Elliott Wave theory is a method of technical analysis that looks for recurrent long-term price patterns associated with ongoing changes in investor sentiment and psychology.

The goal of this dataset is to provide a comprehensive set of impulse wave structures from various financial instruments for use in training machine learning models. 

## Dataset Structure

The dataset consists of chart images generated from historical price data that exhibit impulse wave structures according to Elliott Wave Theory. Each image is labeled with the sequence of the wave it represents.

<p align="center">
  <img src="https://github.com/A-J-Financial-Solutions/EW_Dataset/assets/98991855/d0d3583c-1e70-4014-a718-c5c536cd6167" width="400" alt="Example Impulse Wave">
</p>

## Contribution Guidelines

We welcome contributions from the community. To contribute to the dataset, you can fork this repository, apply your inputs to generate new data, and create a pull request with your additions.

### How to Contribute

1. **Fork this Repository:** Click the 'Fork' button at the top right of this page.
2. **Clone the Forked Repository:** Clone it to your local machine.
3. **Initialize Environment:** Run `pip install -r requirements.txt` to install dependencies. This repository is set up with Python 3.9.0.
4. **Generate Data:** Use the following script located within the ```Elliott Wave Dataset.ipynb``` or ```Elliott Wave Dataset.py``` file to download historical price data for your chosen stock symbol within a date range that includes a full impulse wave:

   ```python
   import yfinance as yf

   stock_symbol = 'YOUR_STOCK_SYMBOL'
   start_date = 'YYYY-MM-DD'
   end_date = 'YYYY-MM-DD'

   stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
   print(stock_data.head())
   stock_data.to_csv('data.csv')
   ```
   
  Replace `YOUR_STOCK_SYMBOL`, `YYYY-MM-DD` for `start_date`, and `YYYY-MM-DD` for `end_date` with the appropriate values for the financial instrument and time period you are analyzing.

5. **Identify Impulse Waves:** Manually identify segments in the data that show a clear impulse wave structure.
6. **Generate Chart Images:** Create chart images from the identified segments. Use a Python script or a Jupyter notebook, whichever you prefer, to process the images.
7. **Label the Images:** For each image you generate, set the `is_impulse` label appropriately:

   ```python
   # Set the label for the image (False for non-impulse, True for impulse)
   is_impulse = SET_LABEL_HERE  # Replace SET_LABEL_HERE with True or False
   ```
   
This label will be used to categorize the image as impulse or non-impulse in the dataset.

8. **Save and Commit Your Images:** Preprossessing of the image and data directory is already automated within the code!
9. **Push to Your Fork:** Push the changes to your forked repository on GitHub.
10. **Create a Pull Request:** Navigate back to the original repository and click on 'New pull request'. Select your fork and submit the request.



## Data Usage

The dataset can be used to train machine learning models to recognize and predict Elliott Wave patterns in financial markets. By contributing to this dataset, you are helping to advance the research in algorithmic trading and technical analysis.
