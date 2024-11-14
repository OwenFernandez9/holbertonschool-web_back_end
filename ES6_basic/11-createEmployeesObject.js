export default function createEmployeesObject(departmentName, employees) {
  const department = {
    [departmentName.toLowerCase()]: employees,
  };
  return department;
}
