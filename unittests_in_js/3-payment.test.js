const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  it('uses Utils.calculateNumber("SUM", 100, 20) and logs the total', function () {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnceWithExactly(calcSpy, 'SUM', 100, 20);
    sinon.assert.calledOnceWithExactly(logSpy, 'The total is: 120');

    calcSpy.restore();
    logSpy.restore();
  });
});