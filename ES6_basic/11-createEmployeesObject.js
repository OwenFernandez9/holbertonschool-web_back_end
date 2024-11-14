export default function createEmployeesObject(departmentName, employees) {
  const department = {
    [`$${departmentName}`]: employees.map((employee) => `$${employee}`),
  };
  return department;
}
