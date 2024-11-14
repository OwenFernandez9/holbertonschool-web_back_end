function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const CurrentYear = getCurrentYear();
  const budget = {
    [`income-${CurrentYear()}`]: income,
    [`gdp-${CurrentYear()}`]: gdp,
    [`capita-${CurrentYear()}`]: capita,

  };

  return budget;
}
