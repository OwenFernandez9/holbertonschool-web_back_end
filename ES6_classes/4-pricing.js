import Currency from './3-currency';

class Pricing {
    constructor(amount, currency){
        if (typeof amount !== 'number') {
            throw TypeError('amount must be a number')
        }

        if (!(currency instanceof Currency)) {
            throw Error('The currency parameter must be an instance of the Currency class')
        }

        this.amount = amount;
        this.currency = currency
    }

    get amount() {
        return this.amount;
    }

    set amount(value) {
        if (typeof value !== 'number'){
            throw new TypeError ('amount must be a number');
        }
        this.amount = value;
    }

    get currency() {
        return this.currency;
    }

    set currency(value) {
        if (!(value instanceof Currency)) {
            throw Error('The currency parameter must be an instance of the Currency class')
        }
    }

    displayFullPrice() {
        return `${this._amount} ${this.currency.currency_name} (${this.currency.currency_code})`;
    }

    static convertPrice(amount, conversionRate){
        return amount * conversionRate
    }

}