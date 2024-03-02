# %%
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
# %%
stock_symbol = 'DJI'
start_date = '2009-03-09'
end_date = '2010-04-26'

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

print(stock_data.head())
stock_data.to_csv('data.csv')

# %%
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'])
plt.title(f'{stock_symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.savefig(f'./mnt/data/{stock_symbol}_{start_date}_to_{end_date}.png')
plt.close()

# %%
# Load the image
image = cv2.imread(f'./mnt/data/{stock_symbol}_{start_date}_to_{end_date}.png')

x_start, y_start = 130, 80 
x_end, y_end = 900, 530

# Crop the image
cropped_image = image[y_start:y_end, x_start:x_end]

# grayscale the image
grayscale_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

# Save or display the cropped image
cv2.imwrite(f'./mnt/data/{stock_symbol}_{start_date}_to_{end_date}.png', grayscale_image)


