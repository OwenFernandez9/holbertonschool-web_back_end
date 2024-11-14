export default function createReportObject(employeesList) {
  const list = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartaments() {
      return Object.keys(this.allEmployees).length;
    },
  };
  return list;
}
