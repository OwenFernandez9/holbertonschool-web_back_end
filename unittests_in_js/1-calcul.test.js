const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('...', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', function () {
    it('...', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4)
    });
  });

  describe('DIVIDE', function() {
    it('...', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2)
    });
  });
  describe('DIVIDE', function() {
    it('...', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error')
    });
  });

});

