const { expect } = require('chai');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('...', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6)
    });
  });

  describe('SUBTRACT', function () {
    it('...', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4)
    });
  });

  describe('DIVIDE', function() {
    it('...', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2)
    });
  });
  describe('DIVIDE', function() {
    it('...', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error')
    });
  });

});

