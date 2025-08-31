const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const baseUrl = 'http://localhost:7865/';

  it('Correct status code?', function (done) {
    request.get(baseUrl, (err, res, _body) => {
      expect(err).to.be.null;
      expect(res && res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', function (done) {
    request.get(baseUrl, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Other? content-type header', function (done) {
    request.get(baseUrl, (err, res, _body) => {
      expect(err).to.be.null;
      expect(res.headers['content-type']).to.match(/text\/html/);
      done();
    });
  });
});