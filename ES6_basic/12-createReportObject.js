export default function createReportObject(employeesList) {
  const list = {
    allEmployees: {
      ...employeesList,
    },
    objemployee: () => Object.keys(employeesList).length,
  };
  return list;
}
