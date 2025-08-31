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
  it('200 when :id is a number', (done) => {
    request.get(`${base}/cart/12`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Body when :id is a number', (done) => {
    request.get(`${base}/cart/12`, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('404 when :id is NOT a number', (done) => {
    request.get(`${base}/cart/hello`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

describe('/available_payments', () => {
  it('returns the correct JSON and status 200', (done) => {
    request.get(
      { url: `${base}/available_payments`, json: true },
      (err, res, body) => {
        expect(err).to.be.null;
        expect(res.statusCode).to.equal(200);
        expect(body).to.deep.equal({
          payment_methods: { credit_cards: true, paypal: false },
        });
        done();
      }
    );
  });
});

describe('/login', () => {
  it('Welcome with provided userName', (done) => {
    request.post(
      {
        url: `${base}/login`,
        json: true,
        body: { userName: 'Betty' },
      },
      (err, res, body) => {
        expect(err).to.be.null;
        expect(res.statusCode).to.equal(200);
        done();
      }
    );
  });

  it('Welcome with provided userName (raw body check)', (done) => {
    request.post(
      {
        url: `${base}/login`,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userName: 'Betty' }),
      },
      (err, res, body) => {
        expect(err).to.be.null;
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });
});
