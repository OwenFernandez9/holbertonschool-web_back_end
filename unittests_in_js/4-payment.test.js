const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi with stub', function () {
  it('stubs Utils.calculateNumber to return 10', function () {
    const calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnceWithExactly(calcStub, 'SUM', 100, 20);
    sinon.assert.calledOnceWithExactly(logSpy, 'The total is: 10');

    calcStub.restore();
    logSpy.restore();
  });
});