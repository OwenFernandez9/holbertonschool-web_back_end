const request = require('request');
const { expect } = require('chai');

const base = 'http://localhost:7865';

describe('Index page', () => {
  it('Correct status code?', (done) => {
    request.get(`${base}/`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(`${base}/`, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Other? content-type header', (done) => {
    request.get(`${base}/`, (err, res) => {
      expect(err).to.be.null;
      expect(res.headers['content-type']).to.match(/text\/html/);
      done();
    });
  });
});

describe('Cart page', () => {
  it('Correct status code when :id is a number', (done) => {
    request.get(`${base}/cart/12`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct body when :id is a number', (done) => {
    request.get(`${base}/cart/12`, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('Correct status code when :id is NOT a number (404)', (done) => {
    request.get(`${base}/cart/hello`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});