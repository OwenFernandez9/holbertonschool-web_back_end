export default function createReportObject(employeesList) {
  const list = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments: () => Object.keys(employeesList).length,
  };
  return list;
}
