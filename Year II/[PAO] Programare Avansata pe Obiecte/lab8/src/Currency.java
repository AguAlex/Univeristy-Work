enum Currency {
    EUR(4.9),
    USD(4.3),
    GBP(5);

    private double exchangeRate;

    private Currency(double value) {
        exchangeRate = value;
    }

    public double getExchangeRate() {
        return exchangeRate;
    }
    public double convertToRON(double amount) {
        return amount * exchangeRate;
    }
}
