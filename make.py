import itertools

from finec.moex import Index, Stock, save_tickers
from finec.dividend import get_dividend_all

# Create dividend file
get_dividend_all(directory="datasets", filename="dividend.csv", overwrite=True)

# Create IMOEX memeber comnpany CLOSE prices - runs several minutes
save_tickers(
    path="datasets/IMOEX_CLOSE.csv",
    security_class=Stock,
    tickers=Index("IMOEX").tickers(),
    field="CLOSE",
)
