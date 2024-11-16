import Currency from './3-currency';

class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw TypeError('amount must be a number');
    }

    if (!(currency instanceof Currency)) {
      throw Error('The currency parameter must be an instance of the Currency class');
    }

    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('amount must be a number');
    }
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (!(value instanceof Currency)) {
      throw Error('The currency parameter must be an instance of the Currency class');
    }
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.currency_name} (${this._currency.currency_code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
export default Pricing;
