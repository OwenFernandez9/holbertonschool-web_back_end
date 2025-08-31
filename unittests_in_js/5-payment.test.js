const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi - with hooks', function () {
  let logSpy;

  beforeEach(function () {
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    logSpy.restore();
  });

  it('logs "The total is: 120" and is called once for (100, 20)', function () {
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(logSpy);
    sinon.assert.calledWithExactly(logSpy, 'The total is: 120');
  });

  it('logs "The total is: 20" and is called once for (10, 10)', function () {
    sendPaymentRequestToApi(10, 10);

    sinon.assert.calledOnce(logSpy);
    sinon.assert.calledWithExactly(logSpy, 'The total is: 20');
  });
});